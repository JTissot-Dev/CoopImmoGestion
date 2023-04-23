from ..db.db import db
from .Payment import Payment
from datetime import datetime as dt
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm.exc import NoResultFound


class SecurityDeposit(Payment):
    __tablename__ = "SecurityDeposit"
    _rental_id = db.Column('rental_id', db.Integer, db.ForeignKey('Rental.rental_id'),
                           nullable=False)

    # Constructor
    def __init__(self, payment_id: int, amount: float, payment_date: dt, rental_id: int):
        super().__init__(payment_id, amount, payment_date)
        self._rental_id = rental_id

    # Define getter and setter property
    @hybrid_property
    def rental_id(self):
        return self._rental_id

    @rental_id.setter
    def rental_id(self, rental_id):
        self._rental_id = rental_id

    @classmethod
    def read(cls):
        try:
            security_deposits = cls.query.all()
            return security_deposits
        except NoResultFound:
            return []
        except Exception:
            return None
