import unittest
import flask
import json
import code
from unittest import TestCase


class TestWiiApi(TestCase):
    def setUp(self):
        code.app.testing = True
        self.app = code.app.test_client()


    def test_root(self):
        result = self.app.get('/')
        inventory = json.loads(result.data)
        self.assertEqual({}, inventory)

    def test_post_message_recieved(self):
        result = self.app.post('/post', data=dict(msg='Hello',name='Jeff'), follow_redirects=True)
        message = json.loads(result.data)
        self.assertEqual('Hello', message)

    def test_post_message_recieved_with_spaces(self):
        result = self.app.post('/post', data=dict(msg='Hello my dudes',name='Jeff'), follow_redirects=True)
        message = json.loads(result.data)
        self.assertEqual('Hello my dudes', message)

