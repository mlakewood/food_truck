
from io import StringIO
import json
import flask_sqlalchemy
import requests

from food_trucks.db import get_engine, get_db_session
from food_trucks.models.food_truck import FoodTruck

if __name__ == '__main__':
    truck_request = requests.get('http://data.sfgov.org/resource/rqzj-sfat.json')

    if truck_request.status_code != 200:
        raise Exception("Error getting data. Status code: %s, Message: %s" % truck_request.status, truck_request.data)

    truck_list = json.loads(truck_request.content)
    engine = get_engine('sqlite:///food_truck.sql')
    session = get_db_session(engine)

    session.query(FoodTruck).delete()

    for t in truck_list:
        print t['applicant']
        try:
            new_truck = FoodTruck(t['applicant'], t['location']['latitude'], t['location']['longitude'])
            new_truck.fooditems = t['fooditems']
            session.add(new_truck)

            session.commit()
        except flask_sqlalchemy.sqlalchemy.exc.IntegrityError:
            session.rollback()
            continue
        except KeyError:
            continue


