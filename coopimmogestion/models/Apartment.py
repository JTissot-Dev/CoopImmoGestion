from flask import Markup
from ..db.db import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm.exc import NoResultFound
from .Property import Property
from .Address import Address
from .Price import Price


class Apartment(Property):
    # Mapping Class with db table
    __tablename__ = "Apartment"
    _stage = db.Column('stage', db.Integer, nullable=False)
    _outdoor = db.Column('outdoor', db.Boolean, default=False, nullable=False)
    _price = db.relationship('Price', uselist=False, backref='apartment', lazy=True, cascade='all, delete-orphan')
    _rental = db.relationship('Rental', uselist=False, backref='apartment', lazy=True)

    # Constructor
    def __init__(self, property_id: int, reference: str, living_area: float, rooms: int,
                 address: Address, stage: int, outdoor: bool, rent: float, charge: float,
                 security_deposit: float):
        super().__init__(property_id, reference, living_area, rooms, address)
        self._stage = stage
        self._outdoor = outdoor
        self._price = Price(None, rent, charge, security_deposit, property_id)

    # Define getter and setter property
    @hybrid_property
    def stage(self):
        return self._stage

    @stage.setter
    def stage(self, stage):
        self._stage = stage

    @hybrid_property
    def outdoor(self):
        return self._outdoor

    @outdoor.setter
    def outdoor(self, outdoor):
        self._outdoor = outdoor

    @hybrid_property
    def price(self):
        return self._price

    # Define string representation for Apartment object
    def __repr__(self):
        return f'<Apartment>: {self.reference}'

    @classmethod
    def read(cls):
        try:
            apartments = cls.query.all()
            return apartments
        except NoResultFound:
            return []
        except Exception:
            return None

    @classmethod
    def create(cls, user_input, apartment_address):
        # get outdoor value in boolean type
        if user_input.get('outdoor'):
            outdoor = bool(Markup(user_input['outdoor']))
        else:
            outdoor = False

        apartment = cls(None, user_input['reference'], user_input['living_area'], user_input['rooms'],
                        apartment_address, user_input['stage'], outdoor, user_input['rent'],
                        user_input['charge'], user_input['security_deposit'])
        try:
            db.session.add(apartment)
            db.session.commit()
            return apartment
        except Exception:
            db.session.rollback()
            return None

    @classmethod
    def update(cls, property_id, user_input, apartment_address):
        # get outdoor value in boolean type
        if user_input.get('outdoor'):
            outdoor = bool(Markup(user_input['outdoor']))
        else:
            outdoor = False

        try:
            apartment = cls.query.get(property_id)
            apartment.reference = user_input['reference']
            apartment.living_area = user_input['living_area']
            apartment.rooms = user_input['rooms']
            apartment.stage = user_input['stage']
            apartment.outdoor = outdoor
            apartment.price.rent = user_input['rent']
            apartment.price.charge = user_input['charge']
            apartment.price.security_deposit = user_input['security_deposit']
            apartment.address_id = apartment_address.address_id
            db.session.commit()
            return apartment
        except Exception:
            return None

    @classmethod
    def delete(cls, property_id):
        try:
            apartment = cls.query.get(property_id)
            db.session.delete(apartment)
            db.session.commit()
            return True
        except Exception:
            return False

