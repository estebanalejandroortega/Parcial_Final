from flask import Flask

app = Flask(__name__)

from src.controller import *

def create_app():
    app.run(debug=True)