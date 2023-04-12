from ..db.db import db
from sqlalchemy.ext.hybrid import hybrid_property
from .Address import Address


class Property(db.Model):
    # Mapping Class with db table
    __abstract__ = True
    _property_id = db.Column('property_id', db.Integer, primary_key=True, autoincrement=True)
    _reference = db.Column('reference', db.String(50), nullable=False)
    _living_area = db.Column('living_area', db.Float(precision=15, scale=4), nullable=False)
    _rooms = db.Column('rooms', db.Integer(50), nullable=False)
    _address_id = db.Column('address_id', db.Integer, db.ForeignKey('Address.address_id'),
                            nullable=False)

    # Constructor
    def __init__(self, property_id: int, reference: str, living_area: float, rooms: int,
                 address: Address):
        self._property_id = property_id
        self._reference = reference
        self._living_area = living_area
        self._rooms = rooms
        self._address_id = address.address_id

    # Define getter and setter property
    @hybrid_property
    def property_id(self):
        return self._property_id

    @hybrid_property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, reference):
        self._reference = reference

    @hybrid_property
    def living_area(self):
        return self._living_area

    @living_area.setter
    def living_area(self, living_area):
        self._living_area = living_area

    @hybrid_property
    def rooms(self):
        return self._rooms

    @rooms.setter
    def rooms(self, rooms):
        self._rooms = rooms
