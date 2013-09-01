"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This flask app exposes some restful api endpoints for food truck discovery. 

"""

import os
from flask import Flask, render_template, request, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base



app = Flask(__name__, static_folder='../static', static_url_path='')

# app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')


def get_engine(url):
    return create_engine(url, convert_unicode=True)


engine = get_engine('sqlite:///food_trucks.sql')

def get_db_session(engine=engine):
    return scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

db_session = get_db_session(engine)

Base = declarative_base()
Base.query = db_session.query_property()

def init_db(engine=engine):
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from food_trucks.models.food_truck import FoodTruck
    Base.metadata.create_all(bind=engine)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
