from . import TestBase


class TestVersion(TestBase):

    def test_version(self):
        self.assertEqual(self.arduino.version()["VersionString"], "0.5.0")
