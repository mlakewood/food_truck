import json

from flask.views import MethodView

from food_trucks.models.food_truck import FoodTruck

class FoodTruckAPI(MethodView):

    def get(self):

        trucks = FoodTruck.query.all()
        # return self._jsonify(food_trucks)
        return 'foo!', 200

    def _jsonify(self, rows):
        output = []
        for row in rows:
            output.append(row.serialise)
        return jsonify(items=output)