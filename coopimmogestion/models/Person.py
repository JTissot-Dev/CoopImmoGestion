from ..db.db import db
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime as dt
from .Address import Address


class Person(db.Model):
    # Mapping abstract Class
    __abstract__ = True
    _person_id = db.Column('person_id', db.Integer, primary_key=True, autoincrement=True)
    _first_name = db.Column('first_name', db.String(50), nullable=False)
    _last_name = db.Column('last_name', db.String(50), nullable=False)
    _birthday = db.Column('birthday', db.DateTime, nullable=False)
    _phone_number = db.Column('phone_number', db.String(50), unique=True, nullable=False)
    _email = db.Column('email', db.String(50), unique=True, nullable=False)
    _address_id = db.Column('address_id', db.Integer, db.ForeignKey('Address.address_id'),
                            nullable=False)

    # Constructor
    def __init__(self, person_id: int, first_name: str, last_name: str, birthday: dt,
                 phone_number: str, email: str, address: Address):
        self._person_id = person_id
        self._first_name = first_name
        self._last_name = last_name
        self._birthday = birthday
        self._phone_number = phone_number
        self._email = email
        self._address_id = address.address_id

    # Define getter and setter property
    @hybrid_property
    def person_id(self):
        return self._person_id

    @hybrid_property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @hybrid_property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @hybrid_property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, birthday):
        self._birthday = birthday

    @hybrid_property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self._phone_number = phone_number

    @hybrid_property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @hybrid_property
    def address_id(self):
        return self._address_id

    @address_id.setter
    def address_id(self, address_id):
        self._address_id = address_id
