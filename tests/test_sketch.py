import os
import shutil
from . import *


class TestSketchCommand(TestBase):

    def test_new(self):
        sketch_path = "TestSketch"
        self._arduino.sketch.new(sketch_path)
        self.assertTrue(os.path.isdir(sketch_path))
        self.assertTrue(os.path.isfile(os.path.join(sketch_path, "TestSketch.ino")))
        shutil.rmtree(sketch_path)

    def test_archive(self):
        sketch_path = "TestSketch"
        self._arduino.sketch.new(sketch_path)
        archive_path = sketch_path + ".zip"
        self._arduino.sketch.archive(sketch_path, archive_path=archive_path)
        self.assertTrue(os.path.exists(archive_path))
        os.remove(archive_path)
        shutil.rmtree(sketch_path)


if __name__ == '__main__':
    unittest.main()
