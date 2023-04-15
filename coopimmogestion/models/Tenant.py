from ..db.db import db
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime as dt
from .Person import Person
from .Address import Address


class Tenant(Person):
    # Mapping Class with db table
    __tablename__ = "Tenant"
    _social_security_number = db.Column('social_security_number', db.String(50), nullable=False)
    _annual_salary = db.Column('annual_salary', db.Float(precision=15, decimal_return_scale=2), nullable=False)
    _balance = db.Column('balance', db.Float(precision=15, decimal_return_scale=2), nullable=True)

    # Constructor
    def __init__(self, person_id: int, first_name: str, last_name: str, birthday: dt,
                 phone_number: str, email: str, address: Address,
                 social_security_number: str, annual_salary: float):
        super().__init__(person_id, first_name, last_name, birthday, phone_number, email,
                         address)
        self._social_security_number = social_security_number
        self._annual_salary = annual_salary
        # Update with Rental relationship when Rental will be implementing
        self._balance = 0.00

    # Define getter and setter property
    @hybrid_property
    def social_security_number(self):
        return self._social_security_number

    @social_security_number.setter
    def role(self, social_security_number):
        self._social_security_number = social_security_number

    @hybrid_property
    def annual_salary(self):
        return self._annual_salary

    @annual_salary.setter
    def password(self, annual_salary):
        self._annual_salary = annual_salary

    @hybrid_property
    def balance(self):
        return self._balance

    # Define string representation for UserApp object
    def __repr__(self):
        return f'<Tenant>: {self.first_name} {self.last_name}'

    @classmethod
    def read(cls):
        try:
            tenants = cls.query.all()
            return tenants
        except Exception:
            return None

