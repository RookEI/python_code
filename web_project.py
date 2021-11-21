from flask import Flask, render_template
from pymongo import MongoClient
import os
from pprint import pprint

client = MongoClient(port=27017)
db=client.test
app = Flask(__name__)

serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)


@app.route('/')
def home():
	return render_template("home.html")

@app.route("/about")
def about():
		return render_template("about.html")

@app.route("/newsletter")
def newsletter():
	return render_template("newsletter.html")

@app.route('/index')
def index():
	return render_template("index.html")

@app.route('/contact')
def contact():
	return render_template("contact.html")


if __name__ == "__main__":
	app.run(debug=True)