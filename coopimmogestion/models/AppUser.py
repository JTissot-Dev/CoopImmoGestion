from flask import session
from ..db.db import db
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime as dt
from .Person import Person
from .Address import Address
from ..crypt.crypt import bcrypt


class AppUser(Person):
    # Mapping Class with db table
    __tablename__ = "AppUser"
    _role = db.Column('role', db.String(50), nullable=False)
    _password = db.Column('password', db.String, unique=True, nullable=False)

    # Constructor
    def __init__(self, person_id: int, first_name: str, last_name: str, birthday: dt,
                 phone_number: str, email: str, address: Address, role: str, password: str):
        super().__init__(person_id, first_name, last_name, birthday, phone_number, email,
                         address)
        self._role = role
        self._password = password

    # Define getter and setter property
    @hybrid_property
    def role(self):
        return self._role

    @role.setter
    def role(self, role):
        self._role = role

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @hybrid_property
    def full_name(self):
        return f'{self._first_name} {self._last_name}'

    # Date text format
    @hybrid_property
    def text_birthday(self):
        return dt.strftime(self._birthday, "%Y-%m-%d")

    # Define string representation for UserApp object
    def __repr__(self):
        return f'<UserApp>: {self.first_name} {self.last_name}'

    # User login validator
    @classmethod
    def login(cls, email, password):
        try:
            user = cls.query.filter_by(email=email).first()
        except Exception:
            return False
        if user and bcrypt.check_password_hash(user.password, password):
            session['userfirstname'] = user.first_name
            session['username'] = user.email
            session['role'] = user.role
            return True
        return False

    @classmethod
    def logout(cls):
        session.clear()

    @classmethod
    def read(cls):
        try:
            users = cls.query.all()
            return users
        except Exception:
            return None

    @classmethod
    def create(cls, user_input, app_user_address):
        user_birthday = cls.convert_birthday(user_input['birthday'])
        # Hashing password
        user_password = bcrypt.generate_password_hash(user_input['password'])

        user = cls(None, user_input['first_name'], user_input['last_name'], user_birthday,
                   user_input['phone_number'], user_input['email'], app_user_address, user_input['role'].lower(),
                   user_password)
        try:
            db.session.add(user)
            db.session.commit()
            return user
        except Exception:
            db.session.rollback()
            return None

    @classmethod
    def update(cls, person_id, user_input, app_user_address):
        try:
            user = cls.query.get(person_id)
            user.first_name = user_input['first_name']
            user.last_name = user_input['last_name']
            user.birthday = user_input['birthday']
            user.phone_number = user_input['phone_number']
            user.role = user_input['role'].lower()
            user.address_id = app_user_address.address_id
            db.session.commit()
            return user
        except Exception:
            return None


