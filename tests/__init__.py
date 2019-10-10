import unittest
import pyduinocli


class TestBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._arduino = pyduinocli.Arduino("./arduino-cli")
