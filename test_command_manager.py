import unittest
from unittest import TestCase
import fakeredis


from command_management import CommandManager


def make_no_commands():
    r = fakeredis.FakeRedis()
    r.flushall()
    return CommandManager(r)

def make_commands():
    r = fakeredis.FakeRedis()
    r.flushall()
    r.set('Hello', 'Jeff')
    r.set('My dudes', 'Waluigi')
    return CommandManager(r)


class TestCommandManager(TestCase):

    def test_new_empty_command_list(self):
        wii=make_no_commands()
        wii.delete_all()
        self.assertEqual(0, len(wii.get_command_list()))

    def test_new_nonempty_inventory(self):
        wii = make_commands()
        wii.delete_all()
        wii.new_message('a', 'left')
        wii.new_message('b', 'right')
        self.assertEqual(len({'a':'left', 'b':'right'}), len(wii.get_command_list()))







#Fake Flask send
#make sure object gets message (mock)