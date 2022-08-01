from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.products import Product, productList
from resources.sales import Sale, SalesToday, UniqueVistors

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.secret_key = "revanth"
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
    return response


jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Sale, "/sale/<string:user_id>")
api.add_resource(SalesToday, "/salesToday")
api.add_resource(productList, "/productList")
api.add_resource(UniqueVistors, "/Uniquevisitors")
api.add_resource(Product, "/Product/<string:name>")
api.add_resource(UserRegister, "/register")

if __name__ == "__main__":
    from db import db

    db.init_app(app)
    app.run(port=5000, debug=True)
