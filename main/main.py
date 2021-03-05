from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
import traceback
from producer import publish
from models import setup_db, ProductUser, Product, db
import requests


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.route("/api/products", methods=['GET'])
    def index():
        return jsonify(Product.query.all())

    @app.route("/api/products/<int:id>/like", methods=['POST'])
    def like(id):
        req = requests.get("http://172.27.0.1:8000/api/user")
        json = req.json()

        try:
            productUser = ProductUser(user_id=json["id"], product_id=id)
            db.session.add(productUser)
            db.session.commit()

            product = Product.query.get(id)
            product.likes += 1
            db.session.commit()
            print('Updated likes count')
            
            publish("product_liked", id)
        except:
            abort(400, "you already liked this")
        return jsonify({
            "message": "success"
        })

    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', debug=True)
