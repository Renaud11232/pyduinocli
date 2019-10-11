import unittest
import pyduinocli


class TestBase(unittest.TestCase):

    _arduino = pyduinocli.Arduino("./arduino-cli")


class CoreNeedingTest(TestBase):

    @classmethod
    def setUpClass(cls):
        cls._arduino.core.update_index()
        cls._arduino.core.install(["arduino:avr"])

    @classmethod
    def tearDownClass(cls):
        cls._arduino.core.uninstall(["arduino:avr"])
