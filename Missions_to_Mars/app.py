from flask import Flask, jsonify, render_template
from flask_pymongo import PyMongo


#####
## Pull in the scrape_mars.py page to access the scrape function
#####
import scrape_mars

app = Flask(__name__)
mongo = PyMongo(app)















if __name__ == "__main__":
    app.run(debug=True)

