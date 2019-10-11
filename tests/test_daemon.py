from . import *
import warnings


class TestDaemonCommand(TestBase):

    def test_daemon(self):
        warnings.warn("This is meant to be run in a daemon thread or process, this will hang and cannot be tested")


if __name__ == '__main__':
    unittest.main()
