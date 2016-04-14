from flask import Flask, render_template
from flask import json, jsonify, redirect, url_for
import flask
from flask_restful import Resource, Api
from . import flask_app
# restful API
api = Api(flask_app)
##########   Route Url  ##########


@flask_app.route('/')
def index():
    return render_template('index.html')

# method 1


@flask_app.route('/method_1', methods=['GET'])
def method_1():
	return jsonify(status='success', username='garychen')

# method 2


class method_2(Resource):

	def get(self):
		return {'status': 'success', 'username': 'garychen', 'method': 'GET'}

	def post(self):
		return {'status': 'success', 'username': 'garychen', 'method': 'POST'}

api.add_resource(method_2, '/method_2')

#######################


@flask_app.route('/test_request', methods=['GET', 'POST'])
def test_request():
	return flask.request.url


@flask_app.route('/test_redirect')
def test_redirect():
	return flask.redirect('/method_1')

#######################


@flask_app.route('/login', methods=['GET', 'POST'])
def song():
	if flask.request.method == 'POST':
		return flask.redirect('/getsession')
	flask.session['username'] = 'garychen'
	return 'success'

@flask_app.route('/getsession')
def get_song_session():
    return flask.session.get('username', '<missing>')

#######################
called = []
@flask_app.before_request
def before1():
    called.append(1)

@flask_app.before_request
def before2():
    called.append(2)

@flask_app.after_request
def after1(response):
    called.append(4)
    return response

@flask_app.after_request
def after2(response):
    called.append(3)
    return response

@flask_app.teardown_request
def finish1(exc):
    called.append(6)

@flask_app.teardown_request
def finish2(exc):
    called.append(5)

@flask_app.route('/before_after_request')
def before_after_request():
    return jsonify(results = called)
# local test python flask_app.py
if __name__ == '__main__':
    flask_app.run(host='0.0.0.0',port=8888)
    
