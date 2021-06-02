from . import *
import os


class TestConfigCommand(TestBase):

    def test_dump(self):
        dump = self._arduino.config.dump()
        self.assertIsInstance(dump, dict)
        self.assertIn("directories", dump)

    def test_init(self):
        config_path = self._arduino.config.init(".")["result"].split(": ")[1]
        self.assertTrue(os.path.isfile(config_path))
        os.remove(config_path)


if __name__ == '__main__':
    unittest.main()
