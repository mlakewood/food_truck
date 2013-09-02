"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This flask app exposes some restful api endpoints for food truck discovery. 

"""

import os
from flask import Flask, render_template, request, redirect, url_for

from food_trucks import my_app

from food_trucks.models.food_truck import FoodTruck
from food_trucks.resources.food_trucks import FoodTruckAPI

def define_urls(app):
    app.add_url_rule('/food_trucks', view_func=FoodTruckAPI.as_view('food_trucks'))

@my_app.teardown_appcontext
def shutdown_session(exception=None):
    if 'DB_SESSION' in my_app.config:
        my_app.config['DB_SESSION'].remove()


@my_app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


