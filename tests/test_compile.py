from . import *
import shutil


class TestCompileCommand(CoreNeedingTest):

    def test_compile(self):
        sketch_path = self._arduino.sketch.new("TestSketch")["result"].split(": ")[1]
        self._arduino.compile(sketch_path, fqbn="arduino:avr:mega:cpu=atmega2560")
        shutil.rmtree(sketch_path)


if __name__ == '__main__':
    unittest.main()
