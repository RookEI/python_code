from flask import Flask, render_template
from pymongo import MongoClient
import connexion
import os
from pprint import pprint

client = MongoClient(port=27017)
db=client.test
app = connexion.App(__name__, specification_dir='./')

app.add_api('swagger.yml')


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

@app.route('/blog')
def blog():
	return render_template("blog.html")


if __name__ == "__main__":
	app.run(host= '0.0.0.0', port=5000, debug=True)