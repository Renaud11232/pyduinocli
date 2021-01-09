from . import *
import warnings
import os


class TestLibCommand(TestBase):

    @classmethod
    def setUpClass(cls):
        cls._arduino.lib.update_index()

    def test_deps(self):
        dependecies = self._arduino.lib.deps("FastLED")
        self.assertTrue(any(dep["name"] == "FastLED" for dep in dependecies["dependencies"]))

    def test_download(self):
        self._arduino.lib.download(["FastLED"])
        warnings.warn("There is no return value to check, just checking it doesn't crash")

    def test_install(self):
        installed = self._arduino.lib.list()
        self.assertTrue(not any(lib["library"]["name"] == "FastLED" for lib in installed))
        self._arduino.lib.install(["FastLED"])
        installed = self._arduino.lib.list()
        self.assertTrue(any(lib["library"]["name"] == "FastLED" for lib in installed))
        self._arduino.lib.uninstall(["FastLED"])

    def test_list(self):
        installed = self._arduino.lib.list()
        self.assertTrue(not any(lib["library"]["name"] == "FastLED" for lib in installed))
        self._arduino.lib.install(["FastLED"])
        installed = self._arduino.lib.list()
        self.assertTrue(any(lib["library"]["name"] == "FastLED" for lib in installed))
        self._arduino.lib.uninstall(["FastLED"])

    def test_search(self):
        results = self._arduino.lib.search(["FastLED"])
        self.assertIsInstance(results, dict)
        libraries = results["libraries"]
        self.assertIsInstance(libraries, list)
        self.assertTrue(any(lib["name"] == "FastLED" for lib in libraries))

    def test_search_no_param(self):
        results = self._arduino.lib.search()
        self.assertIsInstance(results, dict)
        libraries = results["libraries"]
        self.assertIsInstance(libraries, list)
        self.assertTrue(any(lib["name"] == "FastLED" for lib in libraries))

    def test_uninstall(self):
        self._arduino.lib.install(["FastLED"])
        self._arduino.lib.uninstall(["FastLED"])
        installed = self._arduino.lib.list()
        self.assertTrue(installed == "null" or not any(lib["library"]["name"] == "FastLED" for lib in installed))

    def test_update_index(self):
        self._arduino.lib.update_index()
        warnings.warn("There is no return value to check, just checking it doesn't crash")

    def test_upgrade(self):
        self._arduino.lib.upgrade()
        warnings.warn("There is no return value to check, just checking it doesn't crash")

    def test_examples(self):
        self._arduino.lib.install(["FastLED"])
        examples = self._arduino.lib.examples("FastLED")
        print(examples)
        self.assertIsInstance(examples, list)
        for lib in examples:
            example_list = lib["examples"]
            for example in example_list:
                self.assertTrue(os.path.join("FastLED", "examples") in example)
        self._arduino.lib.uninstall(["FastLED"])


if __name__ == '__main__':
    unittest.main()
