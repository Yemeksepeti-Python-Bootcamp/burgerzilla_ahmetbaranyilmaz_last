from flask_restx import Api
from flask import Blueprint

from .user.controller import api as user_ns
from .restaurant.controller import api as restaurant_ns

api_bp = Blueprint("api", __name__)
api = Api(api_bp, version="1.", title="API", description="API for Burger Restaurants")

api.add_namespace(user_ns)
api.add_namespace(restaurant_ns)
