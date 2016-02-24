from socketIO_client import SocketIO, LoggingNamespace
import sys
import logging
logging.getLogger('requests').setLevel(logging.WARNING)
logging.basicConfig(level=logging.DEBUG)

def on_connect():
    print "on_connect()"

if len(sys.argv) < 2:
	host = 'localhost'
else:
	host = sys.argv[1]

socketIO = SocketIO(host, 5000, LoggingNamespace)
print 'socketIO init done'
socketIO.on('connect', on_connect)

socketIO.wait(seconds=3)
print 'exit'
