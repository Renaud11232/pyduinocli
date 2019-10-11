from . import *
import warnings


class TestBoardCommand(CoreNeedingTest):

    def test_attach(self):
        warnings.warn("Cannot test attach, it needs special hardware to be connected.")

    def test_details(self):
        details = self._arduino.board.details("arduino:avr:mega")
        self.assertIsInstance(details, dict)
        self.assertIn("config_options", details)

    def test_list(self):
        warnings.warn("Cannot test list, it needs special hardware to be connected.")

    def test_listall(self):
        list = self._arduino.board.listall()
        self.assertIsInstance(list, dict)
        self.assertIn("boards", list)


if __name__ == '__main__':
    unittest.main()
