from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.sqlite")

db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)

class Item(db.Model):
    id = 
    name = 
    description = 
    price = 
    size = 
    color = 

    def __init__(self, name, description, price, size, color):
        self.name = name
        self.description = description
        self.price = price
        self.size = size
        self.color = color

class ItemSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "description", "price")

item_schema = ItemSchema()
multiple_items_schema = ItemSchema(many=True)

class User(db.Model):
    id = 
    username = 
    password = 
    email = 

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username", "email")

user_schema = UserSchema()
multiple_users_schema = UserSchema(many=True)

@app.route("/user/add", methods=["POST"])
def add_user():
    if request.content_type != "application/json":
        return "Error: Data must be sent as JSON."
    
    post_data = request.get_json()
    username = post_data.get("username")
    password = post_data.get("password")
    email = post_data.get("email")

    record = User(username, password, email)
    db.session.add(record)
    db.session.commit()

    return jsonify("Data added successfully")

@app.route("/item/add", methods=["POST"])
def add_item():
    if request.content_type != "application/json":
        return "Error: Data must be sent as JSON."
    
    post_data = request.get_json()
    name = post_data.get("name")
    description = post_data.get("description")
    price = post_data.get("price")
    

    record = Item(name, description, price)
    db.session.add(record)
    db.session.commit()

    return jsonify("Data added successfully")

@app.route("/item/add-custom", methods=["POST"])
def add_item-custom():
    if request.content_type != "application/json":
        return "Error: Data must be sent as JSON."
    
    post_data = request.get_json()
    size = post_data.get("size")
    color = post_data.get("color")
    

    record = Item(name, description, price)
    db.session.add(record)
    db.session.commit()

    return jsonify("Data added successfully")