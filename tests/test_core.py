from . import *
import warnings


class TestCoreCommand(TestBase):

    @classmethod
    def setUpClass(cls):
        cls._arduino.core.update_index()

    def test_download(self):
        self._arduino.core.download(["arduino:avr"])
        warnings.warn("There is no return value to check, just checking it doesn't crash")

    def test_install(self):
        installed = self._arduino.core.list()["result"]
        self.assertFalse(any(core["id"] == "arduino:avr" for core in installed))
        self._arduino.core.install(["arduino:avr"])
        installed = self._arduino.core.list()["result"]
        self.assertTrue(any(core["id"] == "arduino:avr" for core in installed))
        self._arduino.core.uninstall(["arduino:avr"])

    def test_list(self):
        installed = self._arduino.core.list()["result"]
        self.assertIsInstance(installed, list)
        self.assertFalse(any(core["id"] == "arduino:avr" for core in installed))
        self._arduino.core.install(["arduino:avr"])
        installed = self._arduino.core.list()["result"]
        self.assertIsInstance(installed, list)
        self.assertTrue(any(core["id"] == "arduino:avr" for core in installed))
        self._arduino.core.uninstall(["arduino:avr"])

    def test_search(self):
        results = self._arduino.core.search(["avr"])["result"]
        self.assertIsInstance(results, list)
        self.assertTrue(any(core["id"] == "arduino:avr" for core in results))

    def test_search_no_param(self):
        results = self._arduino.core.search()["result"]
        self.assertIsInstance(results, list)
        self.assertTrue(any(core["id"] == "arduino:avr" for core in results))

    def test_uninstall(self):
        self._arduino.core.install(["arduino:avr"])
        self._arduino.core.uninstall(["arduino:avr"])
        installed = self._arduino.core.list()["result"]
        self.assertFalse(any(core["id"] == "arduino:avr" for core in installed))

    def test_update_index(self):
        self._arduino.core.update_index()
        warnings.warn("There is no return value to check, just checking it doesn't crash")

    def test_upgrade(self):
        self._arduino.core.upgrade()
        warnings.warn("There is no return value to check, just checking it doesn't crash")


if __name__ == '__main__':
    unittest.main()
