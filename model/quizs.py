from random import randrange
from datetime import date
import os, base64
import json


from __init__ import app, db
from sqlalchemy.exc import IntegrityError




class Quizs(db.Model):
   __tablename__ = 'Quizs'


   id = db.Column(db.Integer, primary_key=True)
   _car = db.Column(db.String(255), unique=False, nullable=False)
   _quiztime = db.Column(db.String(255), unique=False, nullable=False)
   def __init__(self, car, quiztime):
       self._quiztime = quiztime  
       self._car = car


   @property
   def quiztime(self):
       return self._quiztime
  
   @quiztime.setter
   def quiztime(self, quiztime):
       self._quiztime = quiztime


   @property
   def car(self):
       return self._car


   @car.setter
   def car(self, car):
       self._car = car


   def __str__(self):
       return json.dumps(self.read())


   def create(self):
       try:
           db.session.add(self) 
           db.session.commit()
           return self
       except IntegrityError:
           db.session.remove()
           return None


   def read(self):
       return {
           "id": self.id,
           "quiztime": self.quiztime,
           "car": self.car,
          
       }


   def update(self, quiztime="", car=""):
       if len(quiztime) > 0:
           self.quiztime = quiztime
       if len(car) > 0:
           self.car = car
       db.session.commit()
       return self




   def delete(self):
       db.session.delete(self)
       db.session.commit()
       return None


def initQuizs():
   with app.app_context():
       db.create_all()
       u1 = Quizs( quiztime='Around 10 Hours', car='Lucid Air' )
       u2 = Quizs( quiztime='Around 7 Hours', car='Tesla Model X' )
       u3 = Quizs( quiztime='Around 7 Hours', car='Tesla Model S' )
       u4 = Quizs( quiztime='Around 18 Hours', car='Rivian R1T' )
       u5 = Quizs( quiztime='Around 11 Hours', car='NIO ET5' )


       quizs = [u1, u2, u3, u4, u5]


       for quiz in quizs:
           try:
               quiz.create()
           except IntegrityError:
               db.session.remove()
               print(f"Records exist, duplicate email, or error:")


  

