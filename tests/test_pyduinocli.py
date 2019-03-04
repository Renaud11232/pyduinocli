import unittest
import pyduinocli


class TestPyduinocli(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.__arduino = pyduinocli.Arduino("./arduino-cli")

    def test_version(self):
        print(self.__arduino.version())


if __name__ == '__main__':
    unittest.main()
