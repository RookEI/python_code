from flask import Flask, render_template
from pymongo import MongoClient
import os

client = MongoClient(port=27017)
db=client.test
app = Flask(__name__)




@app.route('/')
def home():
	return render_template("home.html")

@app.route("/about")
def about():
		return render_template("about.html")

@app.route("/template")
def template():
	return render_template("template.html")

@app.route('/index')
def index():
	return render_template("index.html")

if __name__ == "__main__":
	app.run(debug=True)