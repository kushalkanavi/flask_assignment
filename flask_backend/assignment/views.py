from flask_restful import Resource

class Assignment(Resource):
    def get(self):
        return ({'About': 'You are in assignment get page'})
    
    def post(self):
        return ({'responce': 'All Okay'})