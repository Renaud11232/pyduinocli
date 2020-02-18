from . import *
import warnings


class TestConfigCommand(TestBase):

    def test_clean(self):
        self._arduino.cache.clean()
        warnings.warn("There is no return value to check, just checking it doesn't crash")


if __name__ == '__main__':
    unittest.main()
