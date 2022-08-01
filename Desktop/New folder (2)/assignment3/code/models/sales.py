from db import db
from datetime import date


class SaleModel(db.Model):
    __tablename__ = "sales"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    amount = db.Column(db.Float(precision=2))
    date = db.Column(db.String(80))

    def __init__(self, user_id, product_id, amount):
        self.user_id = user_id
        self.product_id = product_id
        self.amount = amount
        self.date = date.today()

    def json(self):
        return {
            "user_id": self.user_id,
            "product_id": self.product_id,
            "amount": self.amount,
            "date": self.date,
        }

    @classmethod
    def find_by_user_id(cls, user_id):
        today = date.today()
        return cls.query.filter_by(user_id=user_id, date=today).first()

    @classmethod
    def todays_sales(cls):
        today = date.today()
        rows = cls.query.filter_by(date=today).all()
        total_sales = 0
        if rows:
            for row in rows:
                total_sales = total_sales + row.amount
            return {"today's sales": total_sales}
        return {"today's sales": 0}

    @classmethod
    def unique_visitors(cls):
        today = date.today()
        return cls.query.filter_by(date=today).count()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
