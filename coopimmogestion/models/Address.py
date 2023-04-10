from ..db.db import db
from sqlalchemy.ext.hybrid import hybrid_property


class Address(db.Model):
    # Mapping Class with db table
    __tablename__ = "Address"
    _address_id = db.Column('address_id', db.Integer, primary_key=True, autoincrement=True)
    _street_name = db.Column('street_name', db.String(100), nullable=False)
    _street_number = db.Column('street_number', db.Integer, nullable=False)
    _additional_address = db.Column('additional_address', db.String(50), nullable=True)
    _zip_code = db.Column('zip_code', db.String(50), nullable=False)
    _city = db.Column('city', db.String(50), nullable=False)
    _app_users = db.relationship('AppUser')

    # Constructor
    def __init__(self, address_id: int, street_name: str, street_number: int,
                 additional_address: str, zip_code: str, city: str):
        self._address_id = address_id
        self._street_name = street_name
        self._street_number = street_number
        self._additional_address = additional_address
        self._zip_code = zip_code
        self._city = city

    # Define getter and setter property
    @hybrid_property
    def address_id(self):
        return self._address_id

    @hybrid_property
    def street_name(self):
        return self._street_name

    @street_name.setter
    def street_name(self, street_name):
        self._street_name = street_name

    @hybrid_property
    def street_number(self):
        return self._street_number

    @street_number.setter
    def street_number(self, street_number):
        self._street_number = street_number

    @hybrid_property
    def additional_address(self):
        return self._additional_address

    @additional_address.setter
    def additional_address(self, additional_address):
        self._additional_address = additional_address

    @hybrid_property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        self._zip_code = zip_code

    @hybrid_property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

    @hybrid_property
    def app_users(self):
        return self._app_users

    @app_users.setter
    def persons(self, app_users):
        self._app_users = app_users

    # Define string representation for Address object
    def __repr__(self):
        return f'''<Address>: {self.street_name} {self.street_number} {self.additional_address}
                {self.zip_code} {self.city}'''

    @classmethod
    def create(cls, user_input):
        address = cls(None, user_input['street_name'], user_input['street_number'],
                      user_input['additional_address'], user_input['zip_code'], user_input['city'])

        # Add address in db if not exist
        try:
            exist_address = Address.query.filter_by(street_name=address.street_name,
                                                    street_number=address.street_number,
                                                    additional_address=address.additional_address,
                                                    zip_code=address.zip_code, city=address.city).first()
            if not exist_address:
                db.session.add(address)
                db.session.commit()
            else:
                address = exist_address
            return address
        except Exception:
            db.session.rollback()
            return None
