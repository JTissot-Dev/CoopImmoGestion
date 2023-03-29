from ..db.db import db
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime as dt
from .Person import Person


class AppUser(Person):
    # Mapping Class with db table
    __tablename__ = "AppUser"
    _role = db.Column('role', db.String(50), nullable=False)
    _password = db.Column('password', db.String(50), unique=True, nullable=False)

    # Constructor
    def __init__(self, person_id: int, first_name: str, last_name: str, birthday: dt,
                 phone_number: str, email: str, address_id: int, role: str, password: str):
        super().__init__(person_id, first_name, last_name, birthday, phone_number, email,
                         address_id)
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

    # Define string representation for UserApp object
    def __repr__(self):
        return f'<UserApp>: {self.first_name} {self.last_name}'
