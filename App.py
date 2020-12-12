from flask import Flask, request, jsonify
import json
#import flask_mysqldb
from flask_mysqldb import MySQL
from flask_cors import CORS
import os
import uuid
from werkzeug.utils import secure_filename
#import firebase

#local uploads or temp
UPLOAD_FOLDER = "./uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

#filter mime-types
def allowed_files(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)

@app.route("/api/posts", methods=["GET"])
def index():
    if request.method == "GET":
        return jsonify(data="posts main response")






if __name__ == "__main__":
    app.run(debug=True)