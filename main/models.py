import os
from sqlalchemy import Column, String, Integer, UniqueConstraint, create_engine
from flask_sqlalchemy import SQLAlchemy
import json


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


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))

    def __init__(self, id, title, image):
        self.title = title
        self.id = id
        self.image = image

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.image,
        }


class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint("user_id", "product_id", name="user_product_unique")
