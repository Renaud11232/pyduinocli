import unittest
import pyduinocli


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.arduino = pyduinocli.Arduino("./arduino-cli")
