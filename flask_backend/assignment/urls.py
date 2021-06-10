from flask import Blueprint
from .views import FlaskAssignment, GetAssignmentByID, GetAssignmentByTag
from flask_restful import Api

assignment = Blueprint('assignment', __name__)
api = Api(assignment)

api.add_resource(FlaskAssignment, '/')
api.add_resource(GetAssignmentByID, '/<int:id>')
api.add_resource(GetAssignmentByTag, '/assignmentbytag')