from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, ProductUser, Product

app = Flask(__name__)


def create_app(test_config=None):
    # create and configure the app
    setup_db(app)
    CORS(app)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.route("/")
    def index():
        return 'hello'

    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', debug=True)
