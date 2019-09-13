import unittest
import pyduinocli


class TestVersion(unittest.TestCase):

    def setUp(self):
        self.arduino = pyduinocli.Arduino("./arduino-cli")

    def test_version(self):
        self.assertEqual(self.arduino.version()["VersionString"], "0.5.0")

