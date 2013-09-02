"""Tests for the FoodTruck resource"""

import unittest
import os
import inspect
import tempfile

from food_trucks.app import my_app, define_urls
from food_trucks.db import get_engine, init_db, get_db_session, Base
from food_trucks.models.food_truck import FoodTruck


class TestFoodTruckGET(unittest.TestCase):

    def setUp(self):
        test_sql = 'sqlite:///test_db.sql'
        self.engine = get_engine(test_sql)
        self.db = init_db(self.engine, Base)
        self.db_session = get_db_session(self.engine)
        define_urls(my_app)
        self.app = my_app.test_client()



    def tearDown(self):
        self.db_session.remove()
        os.unlink('test_db.sql')

    def test_basic(self):
        nicks_tacos = FoodTruck('Nicks Tacos', 45.78985, 34.78998)

        self.db_session.add(nicks_tacos)
        self.db_session.commit()
        res = self.app.get('/food_trucks')
        self.assertEquals(res.status, '200 OK')

