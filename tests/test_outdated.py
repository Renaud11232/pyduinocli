from . import *


class TestOutdatedCommand(TestBase):

    def test_outdated(self):
        self._arduino.lib.install(["FastLED@3.3.2"])
        outdated = self._arduino.outdated()["result"]
        self.assertTrue(any([l["library"]["name"] == "FastLED" and l["library"]["version"] == "3.3.2" for l in outdated["libraries"]]))
        self._arduino.lib.uninstall(["FastLED@3.3.2"])


if __name__ == '__main__':
    unittest.main()
