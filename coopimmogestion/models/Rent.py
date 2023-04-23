from ..db.db import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm.exc import NoResultFound
from .Payment import Payment
from datetime import datetime as dt


class Rent(Payment):
    __tablename__ = "Rent"
    _origin = db.Column('origin', db.String(50), nullable=False)
    _rental_id = db.Column('rental_id', db.Integer, db.ForeignKey('Rental.rental_id'),
                           nullable=False)
    _agency_fee_id = db.Column('agency_fee_id', db.Integer, db.ForeignKey('AgencyFee.agency_fee_id'),
                               nullable=False)

    # Constructor
    def __init__(self, payment_id: int, amount: float, payment_date: dt,
                 origin: str, rental_id: int, agency_fee_id: int):
        super().__init__(payment_id, amount, payment_date)
        self._origin = origin
        self._rental_id = rental_id
        self._agency_fee_id = agency_fee_id

    # Define getter and setter property
    @hybrid_property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, origin):
        self._origin = origin

    @hybrid_property
    def rental_id(self):
        return self._rental_id

    @rental_id.setter
    def rental_id(self, rental_id):
        self._rental_id = rental_id

    @classmethod
    def read(cls):
        try:
            rents = cls.query.all()
            return rents
        except NoResultFound:
            return []
        except Exception:
            return None
