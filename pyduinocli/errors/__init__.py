class ArduinoError(Exception):

    def __init__(self, message, cause=None, stderr=None):
        self.message = message
        self.cause = cause
        self.stderr = stderr
