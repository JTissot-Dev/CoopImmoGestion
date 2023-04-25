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
    def read(cls, payment_id):
        if payment_id:
            try:
                rent = cls.query.get(payment_id)
                return rent
            except Exception:
                return None
        else:
            try:
                rents = cls.query.all()
                return rents
            except NoResultFound:
                return []
            except Exception:
                return None

    @classmethod
    def create(cls, user_input, rental_id):
        # Get text date in datetime
        payment_date = cls.convert_payment_date(user_input['payment_date'])

        if rental_id:
            rent = cls(None, user_input['amount'], payment_date, user_input['origin'],
                       rental_id, 1)
        else:
            rent = cls(None, user_input['amount'], payment_date, user_input['origin'],
                       user_input['rental_id'], 1)
        try:
            db.session.add(rent)
            db.session.commit()
            return rent
        except Exception as e:
            print(e)
            db.session.rollback()
            return None

    @classmethod
    def update(cls, payment_id, user_input):
        # Get text date in datetime
        payment_date = cls.convert_payment_date(user_input['payment_date'])

        try:
            rent = cls.query.get(payment_id)
            rent.amount = user_input['amount']
            rent.payment_date = payment_date
            rent.origin = user_input['origin']
            rent.rental_id = user_input['rental_id']
            db.session.commit()
            return rent
        except Exception as e:
            print(e)
            return None

    @classmethod
    def delete(cls, payment_id):
        try:
            rent = cls.query.get(payment_id)
            db.session.delete(rent)
            db.session.commit()
            return rent
        except Exception:
            return None
