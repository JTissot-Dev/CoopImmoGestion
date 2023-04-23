from ..db.db import db
from sqlalchemy.ext.hybrid import hybrid_property


class AgencyFee(db.Model):
    __tablename__ = "AgencyFee"
    _agency_fee_id = db.Column('agency_fee_id', db.Integer, primary_key=True, autoincrement=False, unique=True)
    _rate = db.Column('rate', db.Float(precision=15, decimal_return_scale=2), nullable=False)
    _rents = db.relationship('Rent', backref='agency_fee', lazy=True)

    # Constructor
    def __init__(self, agency_fee_id: int, rate: float):
        self._agency_fee_id = agency_fee_id
        self._rate = rate

    # Define setter and getter property
    @hybrid_property
    def agency_fee_id(self):
        return self._agency_fee_id

    @hybrid_property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, rate):
        self._rate = rate
