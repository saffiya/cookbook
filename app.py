import os
import json
from flask import Flask, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from slugify import slugify
import bcrypt

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = 'mongodb+srv://saffiya:St4rl1ght@myfirstcluster-ysd9s.mongodb.net/cookbook?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
    
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/login', methods=['POST'])    
def  login():
    users = mongo.db.users
    login_user = users.find_one({'username' : request.form['username']})
    
    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('index.html'))
            
    return 'Invalid username/password combination'

@app.route('/register', methods=['POST', 'GET']) 
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username' : request.form['username']})
        
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'username' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index.html'))
            
        return 'That username already exists!'  
        
    return render_template('register.html')    
    
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

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    sluggify_url = slugify(request.form.get("name"))
    recipes = mongo.db.recipes
    recipe_id = recipes.insert_one(request.form.to_dict())
    myrecipe = { }
    recipe = mongo.db.recipes.find_one_and_update({'_id': ObjectId(recipe_id.inserted_id)}, {'$set': {'sluggify_url': sluggify_url}})
    return redirect(url_for('recipes_recipe', recipe_id = recipe_id.inserted_id, sluggify_url = sluggify_url))
    
@app.route("/recipes")
def recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", page_title="Recipes", recipes=recipes)
    
@app.route("/recipes/<recipe_id>/<sluggify_url>") 
def recipes_recipe(recipe_id, sluggify_url):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipe.html", recipe=recipe)           
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        