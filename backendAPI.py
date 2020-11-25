from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.sqlite")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    # size = user chooses from small, m, L, and XL
    # color = user chooses from a list of colors

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price


        # self.size = size
        # self.color = color

class ItemSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "description", "price")

item_schema = ItemSchema()
multiple_items_schema = ItemSchema(many=True)


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



# @app.route("/item/add-custom", methods=["POST"])
# def add_item-custom():
#     if request.content_type != "application/json":
#         return "Error: Data must be sent as JSON."
    
#     post_data = request.get_json()
#     size = post_data.get("size")
#     color = post_data.get("color")
    

#     record = Item(name, description, price)
#     db.session.add(record)
#     db.session.commit()

#     return jsonify("Data added successfully")

if __name__ == "__main__":
    app.run(debug=True)
    

    