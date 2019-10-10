import unittest
from . import TestBase


class TestVersionCommand(TestBase):

    def test_version(self):
        version = self._arduino.version()
        self.assertIsInstance(version, dict)
        self.assertIn("VersionString", version)


if __name__ == '__main__':
    unittest.main()
