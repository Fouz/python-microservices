import os
from sqlalchemy import Column, String, Integer, UniqueConstraint, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
from dataclasses import dataclass

POSTGRES = {
    'user': 'postgres',
    'password': 'postgres',
    'database': 'main',
    'host': 'db',
    'port': '5432',
}
database_path = "postgresql://{}:{}@{}:{}/{}".format(
    POSTGRES["user"], POSTGRES["password"], POSTGRES["host"], POSTGRES["port"], POSTGRES["database"])

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

# Models


@dataclass
class Product(db.Model):
    __tablename__ = 'products'
    id: int
    title: str
    image: str
    likes: int

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))
    likes = db.Column(db.Integer, default=0)


    def __init__(self, id, title, image):
        self.title = title
        self.id = id
        self.image = image

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.image,
        }

    def __str__(self):
        return "{0} , {1}, {2}".format(self.id, self.title, self.image)


@dataclass
class ProductUser(db.Model):

    id: int
    user_id: int
    product_id: int
    __table_args__ = (
        db.UniqueConstraint('user_id', 'product_id', name='user_product_unique'),
    )
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    # id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer)
    # product_id = db.Column(db.Integer)

    # UniqueConstraint("user_id", "product_id", name="user_product_unique")
