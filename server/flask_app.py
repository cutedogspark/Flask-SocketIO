from flask import Flask , render_template
from flask_restful import Resource, Api

# setting flask config
flask_app = Flask(__name__)
# the toolbar is only enabled in debug mode:
flask_app.debug = True
# set a 'SECRET_KEY' to enable the Flask session cookies
flask_app.config['SECRET_KEY'] = 'development key'

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

api.add_resource(HelloWorld, '/')

#local test python flask_app.py
if __name__ == '__main__':
    flask_app.run(host='0.0.0.0',port=8888)
    
