
from food_trucks import my_app
from food_trucks.app import define_urls

def run_server():
    from food_trucks.db import get_engine, get_db_session
    engine = get_engine('sqlite:///food_truck.sql')
    my_app.config['DB_SESSION'] = get_db_session(engine)
    define_urls(my_app)
    my_app.debug = True
    return my_app

if __name__ == '__main__':
    app = run_server()
    app.run()