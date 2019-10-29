#to run flask in Sublime Text 3 > CTRL+SHIFT+T (to open PowerShell if installed) > 'env\Scripts\activate' > 'flask run'

import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
# app.secret_key = os.getenv('SECRET_KEY')

# client = pymongo.MongoClient("mongodb+srv://semsmit:<password>@yourrecipe-ngnut.mongodb.net/YourRecipe?retryWrites=true&w=majority")
# db = client.get_database('YourRecipe')

@app.route('/')
def index():
    return render_template('base.html')


# @app.route('/<name>')
# def hello(name):
#     return '<h1>Hello {}!</h1>'.format(name)



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)