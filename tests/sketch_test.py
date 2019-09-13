from . import TestBase
import os.path


class TestSketch(TestBase):

    def test_new(self):
        sketch = self.arduino.sketch_new("TestSketch").split("Sketch created in: ")[1].strip()
        self.assertTrue(os.path.exists(sketch))
        self.assertTrue(os.path.exists(os.path.join(sketch, "TestSketch.ino")))
