"""Tests for the FoodTruck model"""

import unittest
import os

from food_trucks.db import get_engine, init_db, get_db_session, Base
from food_trucks.models.food_truck import FoodTruck


class TestFoodTruckModel(unittest.TestCase):

    def setUp(self):
        # self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        test_sql = 'sqlite:///test_db.sql'
        self.engine = get_engine(test_sql)
        self.db = init_db(self.engine, Base)
        self.db_session = get_db_session(self.engine)

    def tearDown(self):
        self.db_session.remove()
        os.unlink('test_db.sql')

    def test_basic(self):
        nicks_tacos = FoodTruck('Nicks Tacos', 45.78985, 34.78998)
        nicks_tacos.fooditems = 'Tacos'
        self.db_session.add(nicks_tacos)
        self.db_session.commit()

        results = self.db_session.query(FoodTruck).all()

        self.assertEquals(len(results), 1)
        self.assertEquals(results[0].__repr__(), u'<Truck: Nicks Tacos, Lat: 45.789850, Lng: 34.789980>')

        self.assertEquals(results[0]._serialise(), {'latitude': '45.78985', 'longitude': '34.78998', 'name': u'Nicks Tacos', u'fooditems': 'Tacos'})






