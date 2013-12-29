#!/usr/bin/env python

"""
This script creates all the models in the defined sql database
"""


import os
import argparse

from food_trucks.db import init_db, get_engine, Base

def main():
    parser = argparse.ArgumentParser(description='Create the data base for the food truck app.')
    parser.add_argument('-u','--url', help='The database url to create', required=True)
    args = vars(parser.parse_args())

    food_truck_db = args['url']
    engine = get_engine(food_truck_db)
    init_db(engine, Base)


if __name__ == '__main__':
    main()
