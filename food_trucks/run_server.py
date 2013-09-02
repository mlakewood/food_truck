
from food_trucks import my_app
from food_trucks.app import define_urls


if __name__ == '__main__':
    from food_trucks.db import get_engine, get_db_session
    engine = get_engine('sqlite:///food_trucks.sql')
    my_app.config['DB_SESSION'] = get_db_session(engine)
    define_urls(my_app)
    my_app.run(debug=True)