from . import *
import os


class TestConfigCommand(TestBase):

    def test_dump(self):
        dump = self._arduino.config.dump()["result"]
        self.assertIsInstance(dump, dict)
        self.assertIn("directories", dump)

    def test_init(self):
        self._arduino.config.init(".")
        config_path = "./arduino-cli.yaml"
        self.assertTrue(os.path.isfile(config_path))
        os.remove(config_path)


if __name__ == '__main__':
    unittest.main()
