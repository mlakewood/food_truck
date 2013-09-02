"""Tests for the FoodTruck resource"""

import unittest
import json
import os


from food_trucks.app import my_app, define_urls
from food_trucks.db import get_engine, init_db, get_db_session, Base
from food_trucks.models.food_truck import FoodTruck
from food_trucks.resources.food_trucks_view import calculate_distance


class TestFoodTruckGET(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        define_urls(my_app)

    def setUp(self):
        test_sql = 'sqlite:///test_db.sql'
        self.engine = get_engine(test_sql)
        self.db = init_db(self.engine, Base)
        self.db_session = get_db_session(self.engine)
        my_app.config['DB_SESSION'] = self.db_session

        self.app = my_app.test_client()

    def tearDown(self):
        self.db_session.remove()
        os.unlink('test_db.sql')

    def test_multiple_trucks(self):
        nicks_tacos = FoodTruck('Nicks Tacos', 45.78985, 34.78998)
        nicks_tacos.fooditems = 'Tacos'

        brians_burgers = FoodTruck('Brians Burgers', 45.78985, 34.78998)
        brians_burgers.fooditems = 'Burgers'

        self.db_session.add(nicks_tacos)
        self.db_session.add(brians_burgers)

        self.db_session.commit()
        res = self.app.get('/food_trucks')
        self.assertEquals(res.status, '200 OK')
        expected_data = {u'items': [{u'latitude': u'45.78985',
                                    u'longitude': u'34.78998',
                                    u'name': u'Nicks Tacos',
                                    u'fooditems': 'Tacos'},
                                    {u'fooditems': u'Burgers',
                                     u'latitude': u'45.78985',
                                     u'longitude': u'34.78998',
                                     u'name': u'Brians Burgers'}
                                    ]
                        }
        self.assertEquals(json.loads(res.data), expected_data)

    def test_single_truck(self):
        nicks_tacos = FoodTruck('Nicks Tacos', 45.78985, 34.78998)
        nicks_tacos.fooditems = 'Tacos'

        self.db_session.add(nicks_tacos)

        self.db_session.commit()
        res = self.app.get('/food_trucks/%d' % nicks_tacos.id)
        self.assertEquals(res.status, '200 OK')
        expected_data = {u'items': [{u'latitude': u'45.78985',
                                    u'longitude': u'34.78998',
                                    u'name': u'Nicks Tacos',
                                    u'fooditems': 'Tacos'}
                                    ]
                        }
        self.assertEquals(json.loads(res.data), expected_data)

    def test_raise_204_multiple(self):

        res = self.app.get('/food_trucks')
        self.assertEquals(res.status, '204 NO CONTENT')

        self.assertEquals(res.data, '')


    def test_raise_204_single(self):

        res = self.app.get('/food_trucks/42')
        self.assertEquals(res.status, '204 NO CONTENT')

        self.assertEquals(res.data, '')

    def test_distance(self):
        nicks_tacos = FoodTruck('Nicks Tacos', 45.78985, 34.78998)
        nicks_tacos.fooditems = 'Tacos'

        brians_burgers = FoodTruck('Brians Burgers', 45.0, 34.0)
        brians_burgers.fooditems = 'Burgers'
        
        self.db_session.add(nicks_tacos)
        self.db_session.add(brians_burgers)
        
        self.db_session.commit()
        res = self.app.get('/food_trucks?current_location=45.78%2C34.78&distance=1')
        self.assertEquals(res.status, '200 OK')
        expected_data = {u'items': [{u'latitude': u'45.78985',
                                    u'longitude': u'34.78998',
                                    u'name': u'Nicks Tacos',
                                    u'fooditems': 'Tacos'}
                                    ]
                        }
        self.assertEquals(json.loads(res.data), expected_data)


class TestHaversine(unittest.TestCase):

    def test_haversine(self):

        nashville = {"lat": 36.12, "long": -86.67}
        los_angeles = {"lat": 33.94, "long": -118.40}

        self.assertEquals(calculate_distance(nashville, los_angeles), 1794.570151951225)

        

