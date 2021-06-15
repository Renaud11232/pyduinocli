from . import *


class TestVersionCommand(TestBase):

    def test_version(self):
        version = self._arduino.version()["result"]
        self.assertIsInstance(version, dict)
        self.assertIn("VersionString", version)


if __name__ == '__main__':
    unittest.main()
