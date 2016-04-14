from gevent import monkey
monkey.patch_all()
import pytest
import unittest
from mock import patch
from app import socketio
from app import flask_app as app
import json
import flask
from mock import Mock
from flask_restful.utils import http_status_message, unpack

class Target:
  def something(self):
    raise TypeError


class TestFlaskAPI(unittest.TestCase):
    @classmethod

    def setUp(self):
        # print 'setUp'
        self.app = app
        self.app_client = app.test_client()
        self.app.testing = True
        print '\r'
        pass
        
    def tearDown(self):
        # print 'tearDown'
        pass

    def test_http_code(self):
        self.assertEquals(http_status_message(200), 'OK')
        self.assertEquals(http_status_message(404), 'Not Found')

    def test_method_1_get(self):
        rv = self.app_client.get('/method_1')
        # print " data => %s" % rv.data
        assert 'success' in rv.data
        pass

    def test_method_2_get(self):
        rv = self.app_client.get('/method_2')
        # print " data => %s" % rv.data
        assert 'success' in rv.data
        assert 'GET' in rv.data
        pass

    def test_method_2_post(self):
        rv = self.app_client.post('/method_2')
        # print " data => %s" % rv.data
        assert 'success' in rv.data
        assert 'POST' in rv.data
        pass

    def test_check_request_url(self):
        ctx = self.app.test_request_context()
        # print " data => %s" % ctx.request.url
        assert ctx.request.url == 'http://localhost/'
        with self.app_client as client:
          rv = client.get('/test_request')
          # print " data => %s" % rv.data
          assert rv.data == b'http://localhost/test_request'

    def test_http_status_code_200(self):
        with self.app_client as client:
            assert client.get('/method_2').status_code == 200

    def test_http_status_code_404(self):
        with self.app_client as client:
            assert client.get('/method_2x').status_code == 404

    def test_check_redirect_url(self):
        with self.app_client as client:
            rv = client.get('/test_redirect')
            # print " data %s" % rv.data
            assert 'method_1' in rv.data

    def test_check_session(self):
        with self.app_client as client:
            rv = client.get('/getsession')
            # print " data [%s]" % rv.data
            assert rv.data == b'<missing>'

            # attrs = vars(rv)
            # print "\r===========================================================\r\n"
            # print '\r\n, \r\n'.join("%s: %s" % item for item in attrs.items())

            rv = client.get('/login')
            assert rv.data == b'success'
            assert flask.session.get('username') == 'garychen'

            # attrs = vars(rv)
            # print "\r===========================================================\r\n"
            # print '\r\n, \r\n'.join("%s: %s" % item for item in attrs.items())

            rv = client.post('/login', data={}, follow_redirects=True)
            assert rv.data == b'garychen'

            # attrs = vars(rv)
            # print "===========================================================\r\n"
            # print '\r\n, \r\n'.join("%s: %s" % item for item in attrs.items())

            rv = client.get('/getsession')
            assert rv.data == b'garychen'

    def test_error_handlers(self):
        with self.app_client as client:
            self.target = Target()
            self.assertRaises(TypeError, lambda: self.target.something())
            pass

    def test_before_after_request(self):
        first_dict = {'results': [1, 2]}
        first_dict_json = json.dumps(first_dict)
        second_dict = {'results': [1, 2, 3, 4, 5, 6, 1, 2]}
        second_dict_json = json.dumps(second_dict)
        with self.app_client as client:
            rv = client.get('/before_after_request')
            # print " data => [%s]" % rv.data
            self.assertEqual(json.loads(rv.data), first_dict)
            rv = client.get('/before_after_request')
            # print " data => [%s]" % rv.data
            self.assertEqual(json.loads(rv.data), second_dict)

if __name__ == '__main__':
    unittest.main()