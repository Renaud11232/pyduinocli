from pyduinocli.commands.arduino import ArduinoCliCommand as Arduino
from pyduinocli.errors import ArduinoError

class ArduinoOld(pyduinocli.commands.Command):







    def version(self):
        return self.__exec([pyduinocli.constants.commands.VERSION])
