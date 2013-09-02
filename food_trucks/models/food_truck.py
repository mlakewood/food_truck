
from sqlalchemy import Column, Integer, String, Float

from food_trucks.db import Base

class FoodTruck(Base):

    __tablename__ = 'food_truck'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True)
    lat = Column(Float())
    lng = Column(Float())
    fooditems = Column(String(200))

    def __init__(self, name, lat, lng):
        self.name = name
        self.lat = lat
        self.lng = lng

    def __repr__(self):
        return '<Truck: %s, Lat: %f, Lng: %f>' % (self.name, self.lat, self.lng)

    def _serialise(self):
        return {
                'name': self.name,
                'latitude': format(self.lat, '.5f'),
                'longitude': format(self.lng, '.5f'),
                'fooditems': self.fooditems
                }