from . import *
import warnings


class TestDebugCommand(TestBase):

    def test_debug(self):
        warnings.warn("This cannot be automagically tested as it needs specific hardware to be connected")


if __name__ == '__main__':
    unittest.main()
