"""
This package contains a flask app RESTFul api for listing
food_trucks in the SF area

"""
# pylint: disable=C
from flask import Flask

my_app = Flask(__name__, static_folder='static', static_url_path='', 
               template_folder='templates')
