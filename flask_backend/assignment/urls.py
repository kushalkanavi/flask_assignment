from flask import Blueprint
from .views import Assignment
from flask_restful import Api

assignment = Blueprint('assignment', __name__)
api = Api(assignment)

api.add_resource(Assignment, '/')