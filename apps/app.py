# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 20:17:38 2020

@author: par64530
"""

from flask import Flask, render_template
from flask_pymongo import PyMongo
import scraping

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    marshemi = mongo.db.marshemi.find_one()
    return render_template("index.html", mars=mars, marshemi=marshemi) # Setting mars variable to mars in html

@app.route("/scrape")
def scrape():
    print("TestA")
    mars = mongo.db.mars
    # Add Hemi
    marshemi = mongo.db.marshemi
    mars_data, marshemi_data = scraping.scrape_all()
    mars.update({}, mars_data, upsert=True)
    marshemi.update({}, marshemi_data, upsert=True)
    return "Scraping Successful!"

if __name__ == "__main__":
    app.run()