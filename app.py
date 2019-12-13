import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = 'mongodb+srv://saffiya:St4rl1ght@myfirstcluster-ysd9s.mongodb.net/cookbook?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')

@app.route('/get_recipes')
def get_recipes():
    recipes=mongo.db.recipes.find()
    print(recipes)
    return render_template("recipes.html", recipes=recipes)
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        