
from io import StringIO
import json
from flask.ext.sqlalchemy.sqlalchemy import exc

from food_trucks.db import get_engine, get_db_session
from food_trucks.models.food_truck import FoodTruck

if __name__ == '__main__':
    fp = open('trucks.json', 'r')
    trucks = StringIO()

    truck_list = json.loads(fp.read())
    import ipdb
    ipdb.set_trace()
    engine = get_engine('sqlite:///food_truck.sql')
    session = get_db_session(engine)

    for t in truck_list:
        print t['applicant']
        new_truck = FoodTruck(t['applicant'], t['location']['latitude'], t['location']['longitude'])
        new_truck.fooditems = t['fooditems']
        session.add(new_truck)
        try:
            session.commit()
        except exc.IntegrityError:
            pass


