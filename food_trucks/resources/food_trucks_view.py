import json
from math import radians, cos, sin, asin, sqrt

from flask import request

from food_trucks.models.food_truck import FoodTruck
from food_trucks.resources.base_resource import BaseViewAPI
from food_trucks.exceptions import InvalidUsage

class FoodTruckAPI(BaseViewAPI):

    def get(self, truck_id=None):
        current_location = request.args.get('current_location', None)
        distance = request.args.get('distance', None)
        
        if truck_id != None:
            trucks = self.db.query(FoodTruck).filter(FoodTruck.id == truck_id)
            if trucks.count() == 0:
                raise InvalidUsage('', status_code=204)
        else:
            # check if we need to filter by http params for nearest trucks
            filter_trucks = False
            if current_location != None and distance != None:
                current_lat, current_long = current_location.split(',')
                distance = int(distance)
                filter_trucks = True
            trucks = self.db.query(FoodTruck).all()

            # if we need to filter by nearest trucks then after getting the trucks
            # loop through and calculate the distance between the current_location
            # and thier location and then return just those that match.
            if filter_trucks is True:
                filtered_trucks = []
                current_location = {"lat": float(current_lat), "long": float(current_long)}
                for t in trucks:
                    truck_location = {"lat": float(t.lat), "long": float(t.lng)} 
                    if calculate_distance(current_location, truck_location) < float(distance):
                        filtered_trucks.append(t)
                trucks = filtered_trucks

            if len(trucks) == 0:
                raise InvalidUsage('', status_code=204)
            
        return self._jsonify(trucks)



def calculate_distance(point1, point2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [point1['long'], point1['lat'], point2['long'], point2['lat']])
    # haversine formula 
    degrees_longitude = lon2 - lon1 
    degress_latitude = lat2 - lat1 
    a = sin(degress_latitude/2)**2 + cos(lat1) * cos(lat2) * sin(degrees_longitude/2)**2
    c = 2 * asin(sqrt(a)) 
    miles = 3961 * c
    return miles 