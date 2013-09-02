"""
This script creates all the models in the defined sql database
"""


import os

from food_trucks.db import init_db, get_engine, Base


if __name__ == '__main__':
    test_sql = 'sqlite:///food_truck.sql'
    engine = get_engine(test_sql)
    init_db(engine, Base)
