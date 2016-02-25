from flask import Flask , render_template
from flask_restful import Resource, Api
from . import flask_app
# restful API
api = Api(flask_app)

#Route Url
@flask_app.route('/')
def index():
    return render_template('index.html')

@flask_app.route('/hello')
def hello():
    return 'Hello World'

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/api')

#local test python flask_app.py
if __name__ == '__main__':
    flask_app.run(host='0.0.0.0',port=8888)
    
