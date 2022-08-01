from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.products import ProductModel


class Product(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "price", type=float, required=True, help="This field cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        product = ProductModel.find_by_name(name)
        if product:
            return product.json()
        return {"message": "product not found"}, 404

    def post(self, name):
        if ProductModel.find_by_name(name):
            return {
                "message": "An product with name '{}' already exists.".format(name)
            }, 400

        data = Product.parser.parse_args()

        product = ProductModel(name, **data)

        try:
            product.save_to_db()
        except:
            return {"message": "An error occurred inserting the product."}, 500

        return product.json(), 201

    @jwt_required()
    def delete(self, name):
        product = ProductModel.find_by_name(name)
        if product:
            product.delete_from_db()
            return {"message": "product deleted."}
        return {"message": "product not found."}, 404

    def put(self, name):
        data = Product.parser.parse_args()

        product = ProductModel.find_by_name(name)

        if product:
            product.price = data["price"]
        else:
            product = ProductModel(name, **data)

        product.save_to_db()

        return product.json()


class productList(Resource):
    @jwt_required()
    def get(self):
        return {"products": list(map(lambda x: x.json(), ProductModel.query.all()))}
