from flask_restful import Resource
from flask import request
from shared_models import db

from .models import Assignment, Tag, Assignment_Tag_Map, User

class FlaskAssignment(Resource):
    def get(self):
        assignment_query = Assignment.query.all()
        responce_dict = {}
        data_list = []
        for assignment in assignment_query:
            data_list.append({'id': assignment.id,
                    'name' : assignment.name,
                    'title': assignment.title,
                    'description': assignment.description,
                    'type': assignment.type,
                    'duration': assignment.duration
                    })
            responce_dict['data'] = data_list 
            responce_dict['status'] = 200
            responce_dict['message'] = 'Success'
        return ({'responce': responce_dict}), 200
    
    def post(self):
        req = request.json
        
        assignment = Assignment(name=req['name'],title=req['title'],description=req['description'],type=req['type'],duration=req['duration'])
        db.session.add(assignment)
        db.session.flush()
        
        for tag in req['tags']:
            tag_result = Tag(name=tag)
            db.session.add(tag_result)
            db.session.flush()

            assignment_tag = Assignment_Tag_Map(assignment_id=assignment.id, tag_id=tag_result.id)
            db.session.add(assignment_tag)

        db.session.commit()

        responce_dict = {}
        responce_dict['status'] = 200
        responce_dict['message'] = 'Success'
        
        return ({'responce': responce_dict}), 200

class GetAssignmentByID(Resource):
    def get(self, id):
        assignment_query = Assignment.query.filter_by(id=id).all()
        responce_dict = {}
        data_list = []
        for assignment in assignment_query:
            data_list.append({'id': assignment.id,
                    'name' : assignment.name,
                    'title': assignment.title,
                    'description': assignment.description,
                    'type': assignment.type,
                    'duration': assignment.duration
                    })
            responce_dict['data'] = data_list 
            responce_dict['status'] = 200
            responce_dict['message'] = 'Success'
        return ({'responce': responce_dict}), 200

class GetAssignmentByTag(Resource):
    def get(self):
        req = request.json
        tag_query = Tag.query.filter_by(name=req['tag']).all()

        tag_list = []
        for tags in tag_query:
            tag_list.append(tags.id)
        
        for tag in tag_list:
            map_query = Assignment_Tag_Map.query.filter_by(tag_id=tag).all()
        
        for map in map_query:
            assignment_query = Assignment.query.filter_by(id=map.assignment_id).all()
        
        responce_dict = {}
        data_list = []
        for assignment in assignment_query:
            data_list.append({'id': assignment.id,
                    'name' : assignment.name,
                    'title': assignment.title,
                    'description': assignment.description,
                    'type': assignment.type,
                    'duration': assignment.duration
                    })
            responce_dict['data'] = data_list 
            responce_dict['status'] = 200
            responce_dict['message'] = 'Success'
        return ({'responce': responce_dict}), 200