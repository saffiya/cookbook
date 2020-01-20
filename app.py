import os
import json
from flask import Flask, render_template, redirect, request, session, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from slugify import slugify
from werkzeug.security import generate_password_hash, check_password_hash



app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = 'mongodb+srv://saffiya:St4rl1ght@myfirstcluster-ysd9s.mongodb.net/cookbook?retryWrites=true&w=majority'
app.config['SECRET_KEY'] = "secretkey"

mongo = PyMongo(app)

@app.route('/')
    
@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/products")
def products():
    return render_template("products.html", page_title="Our Products")
    
@app.route("/addrecipe.html")
def addrecipe():
    return render_template("addrecipe.html", 
    categories=mongo.db.categories.find(), page_title="Add A Recipe") 
    
@app.route('/edit_recipe/<recipe_id>')  
def edit_recipe(recipe_id):
	the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
	all_categories = mongo.db.categories.find()
	return render_template('editrecipe.html', recipe=the_recipe, categories=all_categories, page_title="Edit Recipe")
	
@app.route('/update_recipe/<recipe_id>', methods=["POST"])	
def update_recipe(recipe_id):
	recipes = mongo.db.recipes
	recipes.update( {'_id': ObjectId(recipe_id)},
	{
		'name':request.form.get['recipe.name'],
		'time':request.form.get['recipe.time'],
		'serves':request.form.get['recipe.serves'],
		'difficulty':request.form.get['recipe.difficulty'],
		'category_name':request.form.get['recipe.category_name'],
		'description':request.form.get['recipe.description'],
		'image_source':request.form.get['recipe.image_source'],
		'ingredients':request.form.get['recipe.ingredients'],
		'method_one':request.form.get['recipe.method_one'],
		'method_two':request.form.get['recipe.method_two'],
		'method_three':request.form.get['recipe.method_three'],
		'method_four':request.form.get['recipe.method_four'],
	})
	return redirect(url_for('recipes'))
    
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
	mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
	return redirect(url_for('recipes'))

@app.route('/search', methods=['GET', 'POST'])
def search():
	search = mongo.db.recipes
	

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

# Login
@app.route('/login', methods=['GET'])
def login():
	# Check if user is not logged in already
	if 'user' in session:
		user_in_db = mongo.db.users.find_one({"username": session['user']})
		if user_in_db:
			# If so redirect user to his profile
			flash("You are logged in already!")
			return redirect(url_for('profile', user=user_in_db['username']))
	else:
		# Render the page for user to be able to log in
		return render_template("login.html")
		
# Check user login details from login form
@app.route('/user_auth', methods=['POST'])
def user_auth():
	form = request.form.to_dict()
	user_in_db = mongo.db.users.find_one({"username": form['username']})
	# Check for user in database
	if user_in_db:
		# If passwords match (hashed / real password)
		if check_password_hash(user_in_db['password'], form['user_password']):
			# Log user in (add to session)
			session['user'] = form['username']
			# If the user is admin redirect him to admin area
			if session['user'] == "admin":
				return redirect(url_for('admin'))
			else:
				flash("You were logged in!")
				return redirect(url_for('profile', user=user_in_db['username']))
			
		else:
			flash("Wrong password or user name!")
			return redirect(url_for('login'))
	else:
		flash("You must be registered!")
		return redirect(url_for('register'))
		
# Sign up
@app.route('/register', methods=['GET', 'POST'])
def register():
	# Check if user is not logged in already
	if 'user' in session:
		flash('You are already sign in!')
		return redirect(url_for('index'))
	if request.method == 'POST':
		form = request.form.to_dict()
		# Check if the password and password1 actualy match 
		if form['user_password'] == form['user_password1']:
			# If so try to find the user in db
			user = mongo.db.users.find_one({"username" : form['username']})
			if user:
				flash(f"{form['username']} already exists!")
				return redirect(url_for('register'))
			# If user does not exist register new user
			else:				
				# Hash password
				hash_pass = generate_password_hash(form['user_password'])
				#Create new user with hashed password
				mongo.db.users.insert_one(
					{
						'username': form['username'],
						'email': form['email'],
						'password': hash_pass
					}
				)
				# Check if user is actualy saved
				user_in_db = mongo.db.users.find_one({"username": form['username']})
				if user_in_db:
					# Log user in (add to session)
					session['user'] = user_in_db['username']
					return redirect(url_for('profile', user=user_in_db['username']))
				else:
					flash("There was a problem savaing your profile")
					return redirect(url_for('register'))

		else:
			flash("Passwords dont match!")
			return redirect(url_for('register'))
		
	return render_template("register.html")
	
# Log out
@app.route('/logout')
def logout():
	# Clear the session
	session.clear()
	flash('You were logged out!')
	return redirect(url_for('index'))
	
# Profile Page
@app.route('/profile/<user>')
def profile(user): 
	# Check if user is logged in
	if 'user' in session:
		# If so get the user and pass him to template for now
		user_in_db = mongo.db.users.find_one({"username": user})
		return render_template('profile.html', user=user_in_db)
	else:
		flash("You must be logged in!")
		return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        