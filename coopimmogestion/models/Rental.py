from ..db.db import db
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime as dt
from .Tenant import Tenant
from .Apartment import Apartment


class Rental(db.Model):
    # Mapping Class with db table
    __tablename__ = "Rental"
    _rental_id = db.Column('rental_id', db.Integer, primary_key=True, autoincrement=True)
    _start_date = db.Column('start_date', db.DateTime, nullable=False)
    _end_date = db.Column('end_date', db.DateTime, nullable=False)
    _rental_balance = db.Column('rental_balance', db.Float(precision=15, decimal_return_scale=2), nullable=False)
    _tenant_id = db.Column('tenant_id', db.Integer, db.ForeignKey('Tenant.person_id'),
                           nullable=False)
    _apartment_id = db.Column('apartment_id', db.Integer, db.ForeignKey('Apartment.property_id'),
                              nullable=False)
    _inventories = db.relationship('Inventory', backref='rental', lazy=True)

    # Constructor
    def __init__(self, rental_id: int, start_date: dt, end_date: dt, tenant_id: int, apartment_id: int):
        self._rental_id = rental_id
        self._start_date = start_date
        self._end_date = end_date
        # Update with Payement relationship when Payment will be implementing
        self._rental_balance = 0.00
        self._tenant_id = tenant_id
        self._apartment_id = apartment_id

    # Define getter and setter property
    @hybrid_property
    def rental_id(self):
        return self._rental_id

    @hybrid_property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        self._start_date = start_date

    @hybrid_property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        self._end_date = end_date

    @hybrid_property
    def rental_balance(self):
        return self._rental_balance

    @hybrid_property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        self._tenant_id = tenant_id

    @hybrid_property
    def apartment_id(self):
        return self._apartment_id

    @apartment_id.setter
    def apartment_id(self, apartment_id):
        self._apartment_id = apartment_id

    # Get date in text format
    @hybrid_property
    def text_start_date(self):
        return dt.strftime(self._start_date, "%Y-%m-%d")

    @hybrid_property
    def text_end_date(self):
        return dt.strftime(self._end_date, "%Y-%m-%d")

    # Convert text in datetime format
    @classmethod
    def convert_date(cls, date):
        date = dt.strptime(date, "%Y-%m-%d")
        return date

    @classmethod
    def read(cls):
        try:
            rentals = cls.query.all()
            return rentals
        except Exception:
            return None

    @classmethod
    def create(cls, user_input):
        # Get text date in datetime
        start_date = cls.convert_date(user_input['start_date'])
        end_date = cls.convert_date(user_input['end_date'])

        rental = cls(None, start_date, end_date, user_input['tenant_id'], user_input['apartment_id'])
        try:
            db.session.add(rental)
            db.session.commit()
            return rental
        except Exception:
            db.session.rollback()
            return None

    @classmethod
    def update(cls, rental_id, user_input):
        # Get text date in datetime
        start_date = cls.convert_date(user_input['start_date'])
        end_date = cls.convert_date(user_input['end_date'])

        try:
            rental = cls.query.get(rental_id)
            rental.start_date = start_date
            rental.end_date = end_date
            rental.tenant_id = user_input['tenant_id']
            rental.apartment_id = user_input['apartment_id']
            db.session.commit()
            return rental
        except Exception:
            return None

    @classmethod
    def delete(cls, rental_id):
        try:
            rental = cls.query.get(rental_id)
            db.session.delete(rental)
            db.session.commit()
            return True
        except Exception:
            return False


