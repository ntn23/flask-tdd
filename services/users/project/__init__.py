# services/users/project/__init__.py

import os
from flask import Flask, jsonify
from flask_restful import Resource, Api
import sys

# instantiate the app
app = Flask(__name__)

api = Api(app)

# set config
app_settings = os.getenv('APP_SETTINGS')  # new
app.config.from_object(app_settings)      # new


class UsersPing(Resource):
    def get(self):
        return {
        'status': 'success',
        'message': 'pong!'
    }

# print(app.config, file=sys.stderr)
api.add_resource(UsersPing, '/users/ping')