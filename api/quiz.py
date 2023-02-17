from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from datetime import datetime


from model.quizs import Quizs


quiz_api = Blueprint('quiz_api', __name__,
                  url_prefix='/api/quizs')




api = Api(quiz_api)


class QuizsAPI:       
   class _Create(Resource):
       def post(self):
           body = request.get_json()
          
           quiztime = body.get('quiztime')
           if quiztime is None or len(quiztime) < 2:
               return {'message': f'quiztime is missing, or is less than 2 characters'}, 210
           car = body.get('car')
           if car is None or len(car) < 2:
               return {'message': f'User ID is missing, or is less than 2 characters'}, 210


           uo = Quizs(quiztime=quiztime,
                     car=car)
          
           quiz = uo.create()
 
           if quiz:
               return jsonify(quiz.read())
           return {'message': f'Processed {quiztime}, either a format error or User ID is duplicate'}, 210


   class _Read(Resource):
       def get(self):
           quizs = Quizs.query.all() 
           json_ready = [quiz.read() for quiz in quizs] 
           return jsonify(json_ready) 


   api.add_resource(_Create, '/create')
   api.add_resource(_Read, '/')

