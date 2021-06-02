from . import *


class TestOutdatedCommand(TestBase):

    def test_outdated(self):
        self._arduino.lib.install(["FastLED@3.3.2"])
        outdated = self._arduino.outdated()["result"]
        self.assertIn("FastLED", outdated)
        self.assertIn("3.3.2", outdated)
        self._arduino.lib.uninstall(["FastLED@3.3.2"])


if __name__ == '__main__':
    unittest.main()
