from ..db.db import db
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime as dt


class Payment(db.Model):
    __abstract__ = True
    _payment_id = db.Column('payment_id', db.Integer, primary_key=True, autoincrement=True)
    _amount = db.Column('amount', db.Float(precision=15, decimal_return_scale=2), nullable=False)
    _payment_date = db.Column('payment_date', db.DateTime, nullable=False)

    # Constructor
    def __init__(self, payment_id: int, amount: float, payment_date: dt):
        self._payment_id = payment_id
        self._amount = amount
        self._payment_date = payment_date

    # Define getter and setter property
    @hybrid_property
    def payment_id(self):
        return self._payment_id

    @hybrid_property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @hybrid_property
    def payment_date(self):
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date):
        self._payment_date = payment_date

    # Get payment_date in text format
    @hybrid_property
    def text_payment_date(self):
        return dt.strftime(self._payment_date, "%Y-%m-%d")

    # Put input payment_date in datetime format
    @classmethod
    def convert_payment_date(cls, text_payment_date):
        payment_date = dt.strptime(text_payment_date, "%Y-%m-%d")
        return payment_date
