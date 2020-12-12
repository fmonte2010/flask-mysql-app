from flask import Flask, request, jsonify
import json
#import flask_mysqldb
from flask_mysqldb import MySQL
from flask_cors import CORS
import os
import uuid
from werkzeug.utils import secure_filename
#import firebase
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






if __name__ == "__main__":
    app.run(debug=True)