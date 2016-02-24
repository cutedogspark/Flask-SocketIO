from flask import Flask , render_template

#setting flask config
flask_app = Flask(__name__)
# the toolbar is only enabled in debug mode:
flask_app.debug = True
# set a 'SECRET_KEY' to enable the Flask session cookies
flask_app.config['SECRET_KEY'] = 'development key'


#Route Url
@flask_app.route('/')
def index():
    return render_template('index.html')

@flask_app.route('/hello')
def hello():
    return 'Hello World'

#local test python flask_app.py
if __name__ == '__main__':
    flask_app.run(host='0.0.0.0',port=8888)
    
