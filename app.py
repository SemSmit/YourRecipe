#to run flask in Sublime Text 3 > CTRL+SHIFT+T (to open PowerShell if installed) > 'env\Scripts\activate' > 'flask run'

import os
import env
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["MONGO_DBNAME"] = os.getenv("MONGO_DBNAME")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('recipes.html', recipes=mongo.db.recipes.find())



# @app.route('/<name>')
# def hello(name):
#     return '<h1>Hello {}!</h1>'.format(name)



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)