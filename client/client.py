from socketIO_client import SocketIO, LoggingNamespace

import logging
logging.getLogger('requests').setLevel(logging.WARNING)
logging.basicConfig(level=logging.DEBUG)

def on_connect():
    print "on_connect()"
# socketIO = SocketIO('172.17.34.14', 5603, LoggingNamespace)
# socketIO = SocketIO('172.17.34.14', 5000, LoggingNamespace)

socketIO = SocketIO('localhost', 5000, LoggingNamespace)
print 'socketIO init done'
socketIO.on('connect', on_connect)

socketIO.wait(seconds=3)
print 'exit'
a