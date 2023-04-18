from ..db.db import db
from sqlalchemy.ext.hybrid import hybrid_property


class Price(db.Model):
    __tablename__ = "Price"
    _price_id = db.Column('price_id', db.Integer, primary_key=True, autoincrement=True)
    _rent = db.Column('rent', db.Float(precision=15, decimal_return_scale=2), nullable=False)
    _charge = db.Column('charge', db.Float(precision=15, decimal_return_scale=2), nullable=False)
    _security_deposit = db.Column('security_deposit', db.Float(precision=15, decimal_return_scale=2), nullable=False)
    _apartment_id = db.Column('apartment_id', db.Integer, db.ForeignKey('Apartment.property_id'),
                              nullable=False)

    # Constructor
    def __init__(self, price_id: int, rent: float, charge: float, security_deposit: float, apartment_id: int):
        self._price_id = price_id
        self._rent = rent
        self._charge = charge
        self._security_deposit = security_deposit
        self._apartment_id = apartment_id

    # Define getter and setter property
    @hybrid_property
    def price_id(self):
        return self._price_id

    @hybrid_property
    def rent(self):
        return self._rent

    @rent.setter
    def rent(self, rent):
        self._rent = rent

    @hybrid_property
    def charge(self):
        return self._charge

    @charge.setter
    def charge(self, charge):
        self._charge = charge

    @hybrid_property
    def security_deposit(self):
        return self._security_deposit

    @security_deposit.setter
    def security_deposit(self, security_deposit):
        self._security_deposit = security_deposit

    @hybrid_property
    def apartment_id(self):
        return self._apartment_id

    @apartment_id.setter
    def apartment_id(self, apartment_id):
        self._apartment_id = apartment_id


