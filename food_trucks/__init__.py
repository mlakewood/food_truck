from flask import Flask

my_app = Flask(__name__, static_folder='../static', static_url_path='', template_folder='templates')