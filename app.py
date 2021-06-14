from flask import Flask, request, jsonify, render_template
from flask_marshmallow import Marshmallow
from flask_restful import Resource, Api
import subprocess
import datetime
import pickle
import os
from functions import apiKeyCheck, storeDataPT



app = Flask(__name__)
api = Api(app)
ma = Marshmallow(app)


class pTrack(Resource):
    # @staticmethod
    # def get():
    #      try: id = request.args['id']
    #      except Exception as _: id = None

    #      if not id:
    #          users = User.query.all()
    #          return jsonify(users_schema.dump(users))
    #      user = User.query.get(id)
    #      return jsonify(user_schema.dump(user))

    @staticmethod
    def post():
        try:
            apiKey = request.args['apiKey']
            room = request.json['room']
            pIn = request.json['pIn']
            pOut = request.json['pOut']
        except Exception as _:
            return jsonify({
            'State': False,
            'Message': 'You need to parse all items requred for the post request to work',
            'ErrorCode': 'pT002'
            })

        # return jsonify({
        #      'Message': True,
        #      'apiKey': apiKey,
        #      'room': room,
        #      'pIn' : pIn,
        #      'pOut' : pOut
        #      })

        if apiKeyCheck(apiKey):

            if isinstance(room, int) and isinstance(pIn, int) and isinstance(pOut, int):
                if storeDataPT(room, pIn, pOut):

                    return jsonify({
                    'State': True,
                    'Message': 'Data was successfully saved'
                    })
                else:
                    return jsonify({
                    'State': False,
                    'Message': 'File Failed to write to disk',
                    'ErrorCode': 'pT011'
                    })
            else:
                return jsonify({
                'State': False,
                'Message': 'Items parsed must be Int',
                'ErrorCode': 'pT012'
                })

        else:
            return jsonify({
            'State': False,
            'Message': f'{apiKey} is a invalid api key either its the wrong key or the system has not been configured yet refer to docs in this persist',
            'ErrorCode': 'pT001'
            })


    # @staticmethod
    # def put():
    #     try: id = request.args['id']
    #     except Exception as _: id = None
    #     if not id:
    #         return jsonify({ 'Message': 'Must provide the user ID' })
    #     user = User.query.get(id)

    #     username = request.json['username']
    #     password = request.json['password']
    #     first_name = request.json['first_name']
    #     last_name = request.json['last_name']
    #     age = request.json['age']

    #     user.username = username 
    #     user.password = password 
    #     user.first_name = first_name 
    #     user.last_name = last_name
    #     user.age = age 

    #     db.session.commit()
    #     return jsonify({
    #         'Message': f'User {first_name} {last_name} altered.'
    #     })

    # @staticmethod
    # def delete():
    #     try: id = request.args['id']
    #     except Exception as _: id = None
    #     if not id:
    #         return jsonify({ 'Message': 'Must provide the user ID' })
    #     user = User.query.get(id)

    #     db.session.delete(user)
    #     db.session.commit()

    #     return jsonify({
    #         'Message': f'User {str(id)} deleted.'
    #     })

class bTrack(Resource):
    @staticmethod
    def post():
        try:
            apiKey = request.args['apiKey']
            room = request.json['room']
            binN = request.json['binN']
            data = request.json['data']
        except Exception as _:
            return jsonify({
            'State': False,
            'Message': 'You need to parse all items requred for the post request to work',
            'ErrorCode': 'pT002'
            })

        if apiKeyCheck(apiKey):

            if isinstance(room, int) and isinstance(binN, int) and isinstance(data, int):
                if storeDataBT(room, pIn, pOut):

                    return jsonify({
                    'State': True,
                    'Message': 'Data was successfully saved'
                    })
                else:
                    return jsonify({
                    'State': False,
                    'Message': 'File Failed to write to disk',
                    'ErrorCode': 'pT011'
                    })
            else:
                return jsonify({
                'State': False,
                'Message': 'Items parsed must be Int',
                'ErrorCode': 'pT012'
                })

        else:
            return jsonify({
            'State': False,
            'Message': f'{apiKey} is a invalid api key either its the wrong key or the system has not been configured yet refer to docs in this persist',
            'ErrorCode': 'pT001'
            })

#establish pages
api.add_resource(pTrack, '/api/pTrack')

#deliver a homeapge
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
