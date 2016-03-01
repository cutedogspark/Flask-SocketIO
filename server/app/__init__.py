from flask import Flask 
from flask_socketio import SocketIO

# setting flask config
flask_app = Flask(__name__)
# the toolbar is only enabled in debug mode:
flask_app.debug = True
# set a 'SECRET_KEY' to enable the Flask session cookies
flask_app.config['SECRET_KEY'] = 'oceanktv'

socketio = SocketIO(flask_app, async_mode='gevent')


# from utils.logger import KTVLogger
# logger = KTVLogger('ktv_app_server').init_logger('flask_app')


import app.flask_api
import app.socket_even
# import app.socketio_event