from . import *


class TestCompletionCommand(TestBase):

    def test_completion(self):
        self.assertRaises(pyduinocli.ArduinoError, self._arduino.completion, shell="bash")


if __name__ == '__main__':
    unittest.main()
