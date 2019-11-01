import os
import shutil
from . import *


class TestSketchCommand(TestBase):

    def test_new(self):
        sketch_path = eval(self._arduino.sketch.new("TestSketch")).split(": ")[1]
        self.assertTrue(os.path.isdir(sketch_path))
        self.assertTrue(os.path.isfile(os.path.join(sketch_path, "TestSketch.ino")))
        shutil.rmtree(sketch_path)


if __name__ == '__main__':
    unittest.main()
