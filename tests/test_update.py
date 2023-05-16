from . import *


class TestUpdateCommand(TestBase):

    def test_update(self):
        self._arduino.lib.install(["FastLED@3.3.2"])
        outdated = self._arduino.update(show_outdated=True)["result"]
        self.assertTrue(any(lib["library"]["name"] == "FastLED" and lib["library"]["version"] == "3.3.2" for lib in outdated["libraries"]))
        self._arduino.lib.uninstall(["FastLED@3.3.2"])


if __name__ == '__main__':
    unittest.main()
