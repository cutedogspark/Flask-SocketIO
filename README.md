# Flask-SocketIO

##create virtual env  
```python 
	virtualenv --no-site-packages  env   
	cd env   
	source env/bin/activate   
``` 
##exit env  
```python 
	deactivate   
``` 

##install  
```python
	pip install --upgrade pip   
	pip install flask-socketio   
	pip install gevent-websocket   
	pip install flask   
	pip install socketIO-client   
	pip install flask-debugtoolbar
``` 

##test 

###Server
```python
	cd server
	python app.py  
``` 
###client
```python                                                                                                    
	python client.py   
	DEBUG:root:localhost:5000/socket.io [transport selected] websocket   
	DEBUG:root:localhost:5000/socket.io [heartbeat reset]   
	socketIO init done   
	DEBUG:root:localhost:5000/socket.io [engine.io noop]   
	DEBUG:root:localhost:5000/socket.io [engine.io pong]   
	DEBUG:root:localhost:5000/socket.io [engine.io pong]   
``` 
