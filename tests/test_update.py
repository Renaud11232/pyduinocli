from . import *


class TestUpdateCommand(TestBase):

    def test_update(self):
        self._arduino.lib.install(["FastLED@3.3.2"])
        outdated = self._arduino.update(show_outdated=True)["result"]
        self.assertIn("FastLED", outdated)
        self.assertIn("3.3.2", outdated)
        self._arduino.lib.uninstall(["FastLED@3.3.2"])


if __name__ == '__main__':
    unittest.main()
