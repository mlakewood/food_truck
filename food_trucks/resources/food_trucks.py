from flask.views import MethodView
import json

from food_trucks.app import app, db
from food_trucks.resources.base_resource import BaseResource
from food_trucks.models.food_truck import FoodTruck

class FoodTruckAPI(BaseResource):

    def get(self):
=       food_trucks = FoodTruck.query.all()
        return self._jsonify(food_trucks)


app.add_url_rule('/food_trucks/', view_func=FoodTruckAPI.as_view('food_trucks'))