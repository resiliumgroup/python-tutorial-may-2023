from flask import Flask, render_template
from . import api

app = Flask(__name__)

@app.route("/")
def hello_world():
    assessments = api.get_assessments().json()
    return render_template("index.html", assessments=assessments)
