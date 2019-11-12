#to run flask in Sublime Text 3 > CTRL+SHIFT+T (to open PowerShell if installed) > 'env\Scripts\activate' > 'flask run'

import os
import env
import random
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["MONGO_DBNAME"] = os.getenv("MONGO_DBNAME")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/recipes')
def index():
	return render_template('recipes.html', methods=["POST", "GET"], recipes=mongo.db.recipes.find())

@app.route('/add_recipe')
def add_recipe():
	return render_template('add_recipe.html', recipes=mongo.db.recipes.find())

@app.route('/file/<filename>', methods=["POST", "GET"])
def file(filename):
	return mongo.send_file(filename)

@app.route('/upload', methods=["POST", "GET"])
def upload():
	recipe_name = request.form['recipe_name']
	description = request.form['description']
	prepminutes = request.form['prepminutes']
	image_file_name = request.form['image_file_name']
	food_type = request.form['food_type']
	the_recipe = request.form['the_recipe']

	if image_file_name[-4:] == ".jpg" or image_file_name[-5:] == ".jpeg":
		new_recipe = {'name': recipe_name.lower(), 'description': description, 'image': image_file_name, 'sort': food_type, 'prepminutes': prepminutes, 'the_recipe': the_recipe}
		food_image = request.files['food_image']
		mongo.save_file(food_image.filename, food_image)
		mongo.db.recipes.insert_one(new_recipe)
		return redirect((url_for("index")))

@app.route('/edit_recipe')
def edit_recipe():
	return render_template('edit_recipe.html', recipes=mongo.db.recipes.find())

@app.route('/recipe/<recipeid>', methods=["POST", "GET"])
def recipe(recipeid):
	recipeid = str(recipeid)
	ObjectIdKey = ObjectId(recipeid)
	return render_template('recipe_page.html', recipe = mongo.db.recipes.find_one({ "_id" : ObjectIdKey } ))


@app.route('/randomrecipe', methods=["POST", "GET"])
def randomrecipe():
    count = mongo.db.recipes.count()
    random_recipe = mongo.db.recipes.find()[random.randrange(count)]
    random_recipe_id = random_recipe['_id']
    return recipe(random_recipe_id)


@app.errorhandler(404)
def not_found(e):
	return render_template("404.html")


if __name__ == '__main__':
	app.run(host=os.environ.get('IP'),
			port=int(os.environ.get('PORT')),
			debug=True)