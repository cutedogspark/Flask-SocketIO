# -*- coding: utf-8 -*-
from gevent import monkey
monkey.patch_all()

from app import flask_app
from app import socketio

if __name__ == '__main__':
	flask_app.run(host='0.0.0.0',port=8888)
	# socketio.run(flask_app, host='0.0.0.0', port=5603, debug=True)
