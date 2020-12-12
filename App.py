from flask import Flask, request, jsonify
import json
#import flask_mysqldb
from flask_cors import CORS
import os
import uuid
from werkzeug.utils import secure_filename
#import firebase

#local uploads or temp
UPLOAD_FOLDER = "./uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

app = Flask(__name__)

if __name__ == "__main__"
    app.run()