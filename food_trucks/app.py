"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This flask app exposes some restful api endpoints for food truck discovery. 

"""

from flask import render_template, send_from_directory

from food_trucks import my_app

from food_trucks.resources.food_trucks_view import FoodTruckAPI

def define_urls(app):
    food_truck = FoodTruckAPI.as_view('food_trucks')
    app.add_url_rule('/food_trucks', view_func=food_truck, methods=['GET',])
    app.add_url_rule('/food_trucks/<int:truck_id>', view_func=food_truck, methods=['GET',])
    app.add_url_rule('/', view_func=food_truck, methods=['GET',])


@my_app.teardown_appcontext
def shutdown_session(exception=None):
    if 'DB_SESSION' in my_app.config:
        my_app.config['DB_SESSION'].remove()


@my_app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

@my_app.route('/')
def static_from_root():
    return send_from_directory(my_app.static_folder, 'index.html')

