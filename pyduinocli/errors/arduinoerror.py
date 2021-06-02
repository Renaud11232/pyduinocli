class ArduinoError(Exception):

    def __init__(self, result):
        self.result = result
