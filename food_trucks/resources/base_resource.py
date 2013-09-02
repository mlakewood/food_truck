
from flask import jsonify

from flask.views import MethodView

from food_trucks import my_app


class BaseViewAPI(MethodView):

    def __init__(self):
        super(BaseViewAPI, self).__init__()
        self.db = my_app.config['DB_SESSION']


    def _jsonify(self, rows):
        output = []
        for row in rows:
            output.append(row._serialise())
        return jsonify(items=output)