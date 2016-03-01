# -*- coding: utf-8 -*-
from socketIO_client import SocketIO, LoggingNamespace, BaseNamespace
import sys

import logging
# logging.getLogger('requests').setLevel(logging.WARNING)
logging.basicConfig(level=logging.DEBUG)

# select host or remote server
if len(sys.argv) < 3:
	host = 'localhost'
	#8001(node),5000(flask-socketio),5603(ktv)
	port = 5603
else:
	host = sys.argv[1]
	port = sys.argv[2]
# set sub namespace
Namespace = '/oceanktv'

class Main(LoggingNamespace):
	_connected = True
	def initialize(self):
		print '(GY) Main initialize'

	def on_connect(self):
		print '(GY) Main On connect'

	def on_disconnect(self):
		print('(GY) Main on_disconnect')

class Oceanktv(LoggingNamespace):
    def initialize(self):
    	print('(GY) Oceanktv initialize')
        self.called_on_disconnect = False
        self.args_by_event = {}
        self.response = None

    def on_disconnect(self):
    	print('(GY) Oceanktv on_disconnect')
        self.called_on_disconnect = True

    def on_wait_with_disconnect_response(self):
    	print('(GY) Oceanktv on_wait_with_disconnect_response')
        self.disconnect()

    def on_event(self, event, *args):
    	print('(GY) Oceanktv on_event')
        callback, args = find_callback(args)
        if callback:
            callback(*args)
        self.args_by_event[event] = args

    def on_message(self, data):
    	print('(GY) Oceanktv on_message')
        self.response = data

	def on_change(self, change):
		print('(GY) on change')

    def on_connect(self):
        self.emit('my broadcast event', {'data': 'Hi, I am python client emit(on_connect even), Can you here me ?'} )

    def on_my_response(self, *args):
        print('(GY) on_my_response', args)

if __name__ == '__main__':
	print '(GY) connect ....%s %s' % (host, port)
	socketIO = SocketIO(host, int(port), Main)
	print '(GY) socketIO define Namespace in Oceanktv'
	oceanktv_namespace = socketIO.define(Oceanktv,Namespace)
	while (1):
		oceanktv_namespace.emit('my broadcast event', {'data': 'I am python client...broadcast emit '} )
		socketIO.wait(seconds=1)
		pass
	print 'exit'
