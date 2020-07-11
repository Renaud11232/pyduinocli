from . import *


class TestCompletionCommand(TestBase):

    def test_completion(self):
        script = self._arduino.completion(shell="bash")
        self.assertTrue(script.startswith("# bash completion"))


if __name__ == '__main__':
    unittest.main()
