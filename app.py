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


# new_recipe = {'name': recipe_name.lower(), 'description': description, 'prepminutes': int(prepminutes), 'image': image_file_name, 'sort': food_type}

@app.route('/')
def index():
    return render_template('recipes.html', recipes=mongo.db.recipes.find())

@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html', recipes=mongo.db.recipes.find())

@app.route('/upload', methods=["POST"])
def upload():
		if 'food_image' in request.files:
			food_image = request.files['food_image']
			mongo.save_file(food_image.filename, food_image)
			return "<H1>Your recipe has been uploaded!</H1>"

@app.route('/edit_recipe')
def edit_recipe():
    return render_template('edit_recipe.html', recipes=mongo.db.recipes.find())

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

@app.route('/file/<filename>')
def file(filename):
	return mongo.send_file(filename)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)