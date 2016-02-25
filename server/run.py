# -*- coding: utf-8 -*-
from gevent import monkey
monkey.patch_all()

from app import flask_app
from app import socketio

if __name__ == '__main__':
	socketio.run(flask_app,host='0.0.0.0',debug = True)