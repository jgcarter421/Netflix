
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import splinter

app = Flask(__name__)


# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/Netflex_app"
mongo = PyMongo(app)

@app.route("/")
def index():
   Netflex = mongo.db.mars.find_one()
   return render_template("index.html", Netflex=Netflex)


if __name__ == "__main__":
    app.run(debug=True)