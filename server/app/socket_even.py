# -*- coding: utf-8 -*-
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect

from . import socketio

Namespace = '/test'
#====================================================================

@socketio.on('connect', Namespace)
def test_connect():
    emit('my response', {'data': 'Connected oceanktv', 'count': 0})

@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Connected', 'count': 0})

@socketio.on('disconnect')
def test_disconnect():
    # print('Client disconnected', request.sid)
    pass

@socketio.on('disconnect', Namespace)
def test_disconnect():
    # print('Client disconnected', request.sid)
    pass

@socketio.on('test get emit')
def on_custom_event(message):
    emit('emit echo response',{'data': message['data'], 'namespace': None})

@socketio.on('test get emit', Namespace)
def test_get_emit_message(message):
    # print 'message = %s' % message
    emit('emit echo response',{'data': message['data'], 'namespace': Namespace})


@socketio.on('my custom broadcast event')
def on_custom_event_broadcast(message):
    emit('my custom response', message, broadcast=True)


@socketio.on('my custom broadcast namespace event', namespace='/test')
def on_custom_event_broadcast_test(data):
    emit('my custom namespace response', data, namespace='/test',
         broadcast=True)


#====================================================================
@socketio.on('my event', Namespace)
def test_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': message['data'], 'count': session['receive_count']})
    emit('my response2',
         {'data': message['data'], 'count': session['receive_count']}, broadcast=True)

@socketio.on('my broadcast event', namespace=Namespace)
def test_broadcast_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': message['data'], 'count': session['receive_count']},
         broadcast=True)


@socketio.on('join', Namespace)
def join(message):
    join_room(message['room'])
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': 'In rooms: ' + ', '.join(rooms()),
          'count': session['receive_count']})


@socketio.on('leave', Namespace)
def leave(message):
    leave_room(message['room'])
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': 'In rooms: ' + ', '.join(rooms()),
          'count': session['receive_count']})


@socketio.on('close room', Namespace)
def close(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response', {'data': 'Room ' + message['room'] + ' is closing.',
                         'count': session['receive_count']},
         room=message['room'])
    close_room(message['room'])


@socketio.on('my room event', Namespace)
def send_room_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': message['data'], 'count': session['receive_count']},
         room=message['room'])


@socketio.on('disconnect request', Namespace)
def disconnect_request():
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': 'Disconnected!', 'count': session['receive_count']})
    disconnect()


if __name__ == '__main__':
    socketio.run(flask_app,host='0.0.0.0',debug = True)
