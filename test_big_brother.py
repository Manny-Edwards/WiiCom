import unittest
import flask
import json
import code
import command_management
from unittest import TestCase


class TestBigBrotherApi(TestCase):
    def setUp(self):
        code.app.testing = True
        self.app = code.app.test_client()

    def initialize_db(self, command):
        code.wii = command_management.CommandManager(command)

    def test_root(self):
        result = self.app.get('/')
        test = json.loads(result.data)
        self.assertEqual({}, test)

    def test_no_commands(self):
        self.initialize_db({})
        result = self.app.get('/msg_history')
        command = json.loads(result.data)
        self.assertEqual([], command)

    def test_one_commands(self):
        self.initialize_db({'Hello':'My Dude'})
        result = self.app.get('/msg_history')
        command = json.loads(result.data)
        self.assertEqual([], command)

