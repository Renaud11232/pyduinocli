import unittest
from . import TestBase


class TestVersionCommand(TestBase):

    def test_version(self):
        version = self._arduino.version()
        self.assertIsInstance(version, dict)
        self.assertIn("VersionString", version)
        self.assertEqual(version["VersionString"], "0.5.0")


if __name__ == '__main__':
    unittest.main()
