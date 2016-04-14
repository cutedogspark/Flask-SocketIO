from gevent import monkey
monkey.patch_all()

import unittest
from app import socketio
from app import flask_app as app
import json
#
#
# from app import flask_app
# from app import socketio


class TestSocketIO(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # print 'setUpClass'
        pass

    @classmethod
    def tearDownClass(cls):
        # print 'tearDownClass'
        # cov.stop()
        # cov.report(include='flask_socketio/__init__.py')
        pass

    def setUp(self):
        # print 'setUp'
        self.Namespace = '/test'
        print '\r'
        pass

    def tearDown(self):
        # print 'tearDown'
        pass

    def test_connect(self):
        client = socketio.test_client(app)
        received = client.get_received()
        # print received
        self.assertEqual(len(received), 1)
        self.assertEqual(received[0]['args'][0]['data'], 'Connected')
        self.assertEqual(received[0]['name'], 'my response')
        client.disconnect()

    def test_connect_namespace(self):
        client = socketio.test_client(app, namespace=self.Namespace)
        received = client.get_received(self.Namespace)
        # print received
        self.assertEqual(len(received), 1)
        self.assertEqual(received[0]['name'], 'my response')
        self.assertEqual(received[0]['args'][0]['data'], 'Connected oceanktv')
        client.disconnect(namespace=self.Namespace)

    def test_emit(self):
        client = socketio.test_client(app)
        client.get_received()
        client.emit('test get emit', {'data': 'garychen'})
        received = client.get_received()
        # print received
        client.disconnect()

    def test_emit_namespace(self):
        client = socketio.test_client(app, namespace=self.Namespace)
        client.get_received(namespace=self.Namespace)
        client.emit('test get emit', {'data': 'garychen'}, namespace=self.Namespace)
        received = client.get_received(namespace=self.Namespace)
        # print received
        client.disconnect(namespace=self.Namespace)

    def test_broadcast(self):
        client1 = socketio.test_client(app)
        client2 = socketio.test_client(app)
        client3 = socketio.test_client(app, namespace=self.Namespace)
        # connect message
        client2.get_received()
        client3.get_received(self.Namespace)

        client1.emit('my custom broadcast event', {'name': 'Andy'}, broadcast=True)

        # broadcast message
        received = client2.get_received()
        # print received
        self.assertEqual(len(received), 1)
        self.assertEqual(len(received[0]['args']), 1)
        self.assertEqual(received[0]['name'], 'my custom response')
        self.assertEqual(received[0]['args'][0]['name'], 'Andy')

        self.assertEqual(len(client3.get_received(self.Namespace)), 0)

    def test_broadcast_Namespace(self):
        client1 = socketio.test_client(app, namespace=self.Namespace)
        client2 = socketio.test_client(app, namespace=self.Namespace)
        client3 = socketio.test_client(app)

        client2.get_received(self.Namespace)
        client3.get_received()

        client1.emit('my custom broadcast namespace event', {'name': 'Randy'},
                     namespace=self.Namespace)

        # broadcast message by Namespace
        received = client2.get_received(self.Namespace)
        # print received
        self.assertEqual(len(received), 1)
        self.assertEqual(len(received[0]['args']), 1)
        self.assertEqual(received[0]['name'], 'my custom namespace response')
        self.assertEqual(received[0]['args'][0]['name'], 'Randy')

        self.assertEqual(len(client3.get_received()), 0)

if __name__ == '__main__':
    unittest.main()
