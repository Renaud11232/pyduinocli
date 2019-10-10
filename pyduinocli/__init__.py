from pyduinocli.commands.arduino import ArduinoCliCommand as Arduino
from pyduinocli.errors import ArduinoError

class ArduinoOld(pyduinocli.commands.Command):



    def sketch_new(self, name):
        return self.__exec([pyduinocli.constants.commands.SKETCH, pyduinocli.constants.commands.NEW, Arduino.__strip_arg(name)])

    def upload(self, sketch=None, fqbn=None, input=None, port=None, verify=None):
        args = [pyduinocli.constants.commands.UPLOAD]
        if fqbn is not None:
            args.extend([pyduinocli.constants.flags.FQBN, Arduino.__strip_arg(fqbn)])
        if input is not None:
            args.extend([pyduinocli.constants.flags.INPUT, Arduino.__strip_arg(input)])
        if port is not None:
            args.extend([pyduinocli.constants.flags.PORT, Arduino.__strip_arg(port)])
        if verify is True:
            args.append(pyduinocli.constants.flags.VERIFY)
        if sketch is not None:
            args.append(Arduino.__strip_arg(sketch))
        return self.__exec(args)

    def version(self):
        return self.__exec([pyduinocli.constants.commands.VERSION])
