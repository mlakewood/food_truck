import json


from food_trucks.models.food_truck import FoodTruck
from food_trucks.resources.base_resource import BaseViewAPI
from food_trucks.exceptions import InvalidUsage

class FoodTruckAPI(BaseViewAPI):

    def get(self, truck_id=None):
        if truck_id != None:
            trucks = self.db.query(FoodTruck).filter(FoodTruck.id == truck_id)
            if trucks.count() == 0:
                raise InvalidUsage('', status_code=204)
        else:
            trucks = self.db.query(FoodTruck).all()

            if len(trucks) == 0:
                raise InvalidUsage('', status_code=204)
            
        return self._jsonify(trucks)
