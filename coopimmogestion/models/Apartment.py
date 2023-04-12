from ..db.db import db
from sqlalchemy.ext.hybrid import hybrid_property
from .Property import Property
from .Address import Address


class Apartment(Property):
    # Mapping Class with db table
    __tablename__ = "Apartment"
    _stage = db.Column('stage', db.Integer, nullable=False)
    _outdoor = db.Column('outdoor', db.Boolean, default=False, nullable=False)

    # Constructor
    def __init__(self, property_id: int, reference: str, living_area: float, rooms: int,
                 address: Address, stage: int, outdoor: bool):
        super().__init__(property_id, reference, living_area, rooms, address)
        self._stage = stage
        self._outdoor = outdoor

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

