import unittest
import pyduinocli


class TestBase(unittest.TestCase):

    def setUp(self):
        self.arduino = pyduinocli.Arduino("./arduino-cli")
