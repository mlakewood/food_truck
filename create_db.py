"""
This script creates all the models in the defined sql database
"""


import os

from food_trucks.app import init_db


if __name__ == '__main__':
    init_db()