import argparse


from food_trucks import my_app
from food_trucks.app import define_urls

def run_server():
    parser = argparse.ArgumentParser(description='Create the data base for the food truck app.')
    parser.add_argument('-u','--url', help='The database url to create', required=True)
    args = vars(parser.parse_args())

    food_truck_db = args['url']
    
    from food_trucks.db import get_engine, get_db_session
    engine = get_engine(food_truck_db)
    my_app.config['DB_SESSION'] = get_db_session(engine)
    define_urls(my_app)
    my_app.debug = True
    return my_app

def dev_server():
    app = run_server()
    app.run()

if __name__ == '__main__':
    dev_server()
