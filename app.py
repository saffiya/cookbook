import os
import json
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = 'mongodb+srv://saffiya:St4rl1ght@myfirstcluster-ysd9s.mongodb.net/cookbook?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html", page_title="About Us")
    
@app.route("/products")
def products():
    return render_template("products.html", page_title="Our Products")
    
@app.route("/addrecipe.html")
def addrecipe():
    return render_template("addrecipe.html", 
    categories=mongo.db.categories.find(), page_title="Add A Recipe")  
    
@app.route("/recipes")
def recipes():
    data = []
    with open("data/recipes.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("recipes.html", page_title="Recipes", recipes=data)
    
@app.route("/recipes/<recipe_name>") 
def recipes_recipe(recipe_name):
    recipe = {}
    
    with open("data/recipes.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == recipe_name:
                recipe = obj
                
    return render_template("recipe.html", recipe=recipe)           
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        