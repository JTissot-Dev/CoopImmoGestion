from ..db.db import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm.exc import NoResultFound
from datetime import datetime as dt


class Inventory(db.Model):
    # Mapping Class with db table
    __tablename__ = "Inventory"
    _inventory_id = db.Column('inventory_id', db.Integer, primary_key=True, autoincrement=True)
    _type_inv = db.Column('type_inv', db.String(50), nullable=False)
    _inventory_date = db.Column('inventory_date', db.DateTime, nullable=False)
    _observation = db.Column('observation', db.String(250), nullable=True)
    _rental_id = db.Column('rental_id', db.Integer, db.ForeignKey('Rental.rental_id'),
                           nullable=False)

    # Constructor
    def __init__(self, inventory_id: int, type_inv: str, inventory_date: dt,
                 observation: str, rental_id: int):
        self._inventory_id = inventory_id
        self._type_inv = type_inv
        self._inventory_date = inventory_date
        self._observation = observation
        self._rental_id = rental_id

    # Define getter and setter property
    @hybrid_property
    def inventory_id(self):
        return self._inventory_id

    @hybrid_property
    def type_inv(self):
        return self._type_inv

    @type_inv.setter
    def type_inv(self, type_inv):
        self._type_inv = type_inv

    @hybrid_property
    def inventory_date(self):
        return self._inventory_date

    @inventory_date.setter
    def inventory_date(self, inventory_date):
        self._inventory_date = inventory_date

    @hybrid_property
    def observation(self):
        return self._observation

    @observation.setter
    def observation(self, observation):
        self._observation = observation

    @hybrid_property
    def rental_id(self):
        return self._rental_id

    @rental_id.setter
    def rental_id(self, rental_id):
        self._rental_id = rental_id

    # Get date in text format
    @hybrid_property
    def text_inventory_date(self):
        return dt.strftime(self._inventory_date, "%Y-%m-%d")

    # Convert text in datetime format
    @classmethod
    def convert_date(cls, date):
        date = dt.strptime(date, "%Y-%m-%d")
        return date

    @classmethod
    def read(cls):
        try:
            inventories = cls.query.all()
            return inventories
        except NoResultFound:
            return []
        except Exception:
            return None

    @classmethod
    def create(cls, user_input, rental_id):
        # Get text date in datetime
        inventory_date = cls.convert_date(user_input['inventory_date'])

        if rental_id:
            inventory = cls(None, user_input['type_inv'], inventory_date, user_input['observation'],
                            rental_id)
        else:
            inventory = cls(None, user_input['type_inv'], inventory_date, user_input['observation'],
                            user_input['rental_id'])
        try:
            db.session.add(inventory)
            db.session.commit()
            return inventory
        except Exception:
            db.session.rollback()
            return None