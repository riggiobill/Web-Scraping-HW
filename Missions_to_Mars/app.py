from flask import Flask, jsonify, render_template, redirect
from flask_pymongo import PyMongo


#####
## Pull in the scrape_mars.py page to access the scrape function
#####
import scrape_mars

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Web-Scraping-HW"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_dict = scrape_mars.scrape()
    #mars.updateMany({}, mars_dict, upsert=True)
    mongo.db.mars.update({}, mars_dict, upsert=True)
    return redirect("http://localhost:5000/",code=302)


if __name__ == "__main__":
    app.run(debug=True)

