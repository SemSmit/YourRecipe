#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

# import env

import random
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['MONGO_DBNAME'] = os.getenv('MONGO_DBNAME')
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
def home():
    """ displays the homepage by rendering home.html """

    return render_template('home.html')


@app.route('/recipes')
def index():
    """ displays the recipes page by rendering recipes.html, and sends the records of the recipes to it."""

    return render_template('recipes.html',
                           recipes=mongo.db.recipes.find())


@app.route('/add_recipe')
def add_recipe():
    """ displays add_recipe page by rendering add_recipe.html """

    return render_template('add_recipe.html')


@app.route('/file/<filename>', methods=['POST', 'GET'])
def file(filename):
    """ displays the requested file by inserting the filename as parameter """

    return mongo.send_file(filename)


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    """ uploads a recipe/record to the database
........-first it gets the forms.
........-secondly adds it to a array called new_recipe
........-then it checks if the given image is a jpg/jpeg
........-if true > it saves the images to the database and links it with the recipe record
........-it then saves the whole record.
........-at last it will redirect the user to the recipes page where their recipe is shown at the top. """

    recipe_name = request.form['recipe_name']
    description = request.form['description']
    prepminutes = request.form['prepminutes']
    image_file_name = request.form['image_file_name']
    food_type = request.form['food_type']
    the_recipe = request.form['the_recipe']
    new_recipe = {
        'name': recipe_name.lower(),
        'description': description,
        'image': image_file_name,
        'sort': food_type,
        'prepminutes': prepminutes,
        'the_recipe': the_recipe,
        }

    if image_file_name[-4:] == '.jpg' or image_file_name[-5:] \
        == '.jpeg':
        food_image = request.files['food_image']
        mongo.save_file(food_image.filename, food_image)
        mongo.db.recipes.insert_one(new_recipe)
        return redirect(url_for('index'))
    else:
        return 'The given image has to be a .jpg or .jpeg'


@app.route('/edit_recipe/<recipe_id>', methods=['POST', 'GET'])
def edit_recipe(recipe_id):
    """ After "editbutton" is clicked on recipe_page this function sends the correct record to the edit page """

    recipe_id = str(recipe_id)
    return render_template('edit_recipe.html',
                           recipe=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}))


@app.route('/recipe/<recipeid>', methods=['POST', 'GET'])
def recipe(recipeid):
    """ displays the homepage by rendering home.html """

    recipeid = str(recipeid)
    ObjectIdKey = ObjectId(recipeid)
    return render_template('recipe_page.html',
                           recipe=mongo.db.recipes.find_one({'_id': ObjectIdKey}))


@app.route('/randomrecipe', methods=['POST', 'GET'])
def randomrecipe():
    """ This function counts all records and then selects one random record of which it returns the page of"""

    count = mongo.db.recipes.count()
    random_recipe = mongo.db.recipes.find()[random.randrange(count)]
    random_recipe_id = random_recipe['_id']
    return recipe(random_recipe_id)


@app.route('/edit_or_delete/<object_id>', methods=['POST', 'GET'])
def edit_or_delete(object_id):
    """ See "def upload"
....In addition to that it won't insert/create records.
....But it updates them. """

    button = request.form['button']
    if button == ' ':

        # one space is the value of the edit button

        recipe_name = request.form['recipe_name']
        description = request.form['description']
        prepminutes = request.form['prepminutes']
        image_file_name = request.form['image_file_name']
        food_type = request.form['food_type']
        the_recipe = request.form['the_recipe']
        new_recipe = {
            'name': recipe_name.lower(),
            'description': description,
            'image': image_file_name,
            'sort': food_type,
            'prepminutes': prepminutes,
            'the_recipe': the_recipe,
            }
        if image_file_name[-4:] == '.jpg' or image_file_name[-5:] \
            == '.jpeg':
            food_image = request.files['food_image']
            mongo.save_file(food_image.filename, food_image)
            mongo.db.recipes.update({'_id': ObjectId(object_id)},
                                    new_recipe)
            return redirect(url_for('index'))
    elif button == '  ':

        # two spaces is the value of the delete button

        return render_template('delete_recipe.html',
                               recipe=mongo.db.recipes.find_one({'_id': ObjectId(object_id)}))
    else:
        return not_found()


@app.route('/delete/<object_id>', methods=['POST', 'GET'])
def delete_confirm(object_id):
    """ Deletes a record by ID """

    mongo.db.recipes.remove({'_id': ObjectId(object_id)})
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found(e):
    """ displays 404.html if a page is not found. """

    return render_template('404.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT'
            )), debug=False)

			