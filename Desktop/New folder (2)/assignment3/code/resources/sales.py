from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.sales import SaleModel


class Sale(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument(
        "product_id",
        type=str,
        required=True,
        help="This field cannot be left blank!",
    )
    parser.add_argument(
        "amount", type=float, required=True, help="This field cannot be left blank!"
    )

    @jwt_required()
    def get(self, user_id):
        sale = SaleModel.find_by_user_id(user_id)
        if sale:
            return sale.json()
        return {"message": "sale not found"}

    def post(self, user_id):
        sale = SaleModel.find_by_user_id(user_id)
        if sale:
            return {
                "message": "A sale with user_id '{}' already exists.".format(user_id)
            }, 400

        data = Sale.parser.parse_args()
        sale = SaleModel(user_id, **data)

        try:
            sale.save_to_db()
        except:
            return {"message": "An error occurred inserting the sale."}, 500
        return sale.json(), 201

    def delete(self, user_id):
        sale = SaleModel.find_by_user_id(user_id)
        if sale:
            sale.delete_from_db()
            return {"message": "sale deleted."}
        return {"message": "sale not found."}, 404

    def put(self, user_id):
        data = Sale.parser.parse_args()
        sale = SaleModel.find_by_user_id(user_id)

        if sale:
            sale.product_id = data["product_id"]
            sale.amount = data["amount"]
        else:
            sale = SaleModel(user_id, **data)

        sale.save_to_db()

        return sale.json()


class SalesToday(Resource):
    def get(self):
        return SaleModel.todays_sales()


class UniqueVistors(Resource):
    def get(self):
        return SaleModel.unique_visitors()
