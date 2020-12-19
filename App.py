from flask import Flask, request, jsonify
import json
from flask_mysqldb import MySQL
from flask_cors import CORS
import os
import uuid
from werkzeug.utils import secure_filename
import pyrebase

#local uploads or temp
UPLOAD_FOLDER = "./uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

#filter mime-types
def allowed_files(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)

#config to conect a database
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "12345"
app.config["MYSQL_DB"] = "flaskpoststuto"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
mysql = MySQL(app)
CORS(app)

#firebase config
config = {
    "apiKey": "AIzaSyCyK9dY7nMdYD8lHDF0cAzhNcjCrNUvqVw",
    "authDomain": "flask-posts-tuto.firebaseapp.com",
    "projectId": "flask-posts-tuto",
    "storageBucket": "flask-posts-tuto.appspot.com",
    "messagingSenderId": "507753716588",
    "appId": "1:507753716588:web:be9b7950fac20c578bf149",
    "measurementId": "G-QBLZ2J4T80",
    "serviceAccount": "./keyfile.json"    
}

#init firebase app
firebase = pyrebase.initialize_app(config)

#firebase storage
storage = firebase.storage()

@app.route("/api/posts", methods=["GET"])
def index():
    if request.method == "GET":
        return jsonify(data="posts main response")

@app.route("/api/addpost", methods=["POST"])
def addpost():
    if request.method == "POST":
        print(request.form, flush=True)

        title = request.form.get("title")
        content = request.form.get("content")
        cover = request.files["cover"]

        if cover and allowed_files(cover.filename):
            filename = str(uuid.uuid4())
            filename += "."
            filename += cover.filename.split(".")[1]

            #create secure name
            filename_secure = secure_filename(filename)
            
            #save the file inside the uploads folder
            cover.save(os.path.join(app.config["UPLOAD_FOLDER"], filename_secure))

            #Local file
            local_filename = "./uploads"
            local_filename += filename_secure

            #firebase filename
            firebase_filename = "uploads/"
            firebase_filename += filename_secure

            #upload the file
            storage.child(firebase_filename).put(local_filename)
            #get the url of the file
            cover_image = storage.child(firebase_filename).get_url(None)
            
            #get cursor to exec the mysql functions
            cur = mysql.connection.cursor()
            cur.execute(""" INSERT INTO flaskpoststuto (title, content, cover, covername) VALUES (%s, %s, %s, %s) """, 
                (title, content, cover_image, filename_secure)
            )

            os.remove(os.path.join(app.config["UPLOAD_FOLDER"], filename_secure))

            return jsonify(data = "the post was created successfully")




if __name__ == "__main__":
    app.run(debug=True)