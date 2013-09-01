"""Tests for the FoodTruck resource"""

import unittest
import os
import inspect
import tempfile

from food_trucks.app import app, get_engine, init_db, get_db_session
from food_trucks.models.food_truck import FoodTruck


class TestFoodTruckGET(unittest.TestCase):

    def setUp(self):
        test_sql = 'sqlite:///test_db.sql'
        self.engine = get_engine(test_sql)
        self.db = init_db(self.engine)
        self.db_session = get_db_session(self.engine)
        self.app = app.test_client()

    def tearDown(self):
        self.db_session.remove()
        os.unlink('test_db.sql')

    def test_basic(self):
        nicks_tacos = FoodTruck('Nicks Tacos', 45.78985, 34.78998)

        self.db_session.add(nicks_tacos)
        self.db_session.commit()

        res = self.app.get('/food_trucks')
        import ipdb
        ipdb.set_trace()
        print res






