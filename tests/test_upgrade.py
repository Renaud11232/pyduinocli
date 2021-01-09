from . import *


class TestUpgradeCommand(TestBase):

    def test_upgrade(self):
        self._arduino.lib.install(["FastLED@3.3.2"])
        self._arduino.upgrade()
        outdated = self._arduino.outdated()
        self.assertNotIn("FastLED", outdated)
        self.assertNotIn("3.3.2", outdated)
        self._arduino.lib.uninstall(["FastLED"])


if __name__ == '__main__':
    unittest.main()
