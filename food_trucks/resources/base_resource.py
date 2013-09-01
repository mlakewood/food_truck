from flask.views import MethodView
from flask import jsonify

from food_trucks.app import get_db()

class BaseViewAPI(MethodView):

    def __init__(self):
        super(BaseViewAPI, self).__init__()
        self.db = app.get_db()

    def _jsonify(self, rows):
        output = []
        for row in rows:
            output.append(row.serialise)
        return jsonify(items=output)
