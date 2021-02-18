import json
from subprocess import Popen, PIPE
from pyduinocli.errors.arduinoerror import ArduinoError
from pyduinocli.constants import messages


class CommandBase:
    __ERROR_MESSAGE = "Message"
    __ERROR_CAUSE = "Cause"

    def __init__(self, base_args):
        self._base_args = list(base_args)

    @staticmethod
    def _strip_arg(arg):
        return arg.lstrip("-")

    @staticmethod
    def _strip_args(args):
        out = list()
        for arg in args:
            out.append(CommandBase._strip_arg(arg))
        return out

    @staticmethod
    def __parse_output(data):
        try:
            return json.loads(data)
        except ValueError:
            return data

    def _exec(self, args):
        command = list(self._base_args)
        command.extend(args)
        try:
            p = Popen(command, stdout=PIPE, stderr=PIPE)
            stdout, stderr = p.communicate()
            stdout = stdout.decode("utf-8").strip()
            stderr = stderr.decode("utf-8").strip()
            decoded_out = self.__parse_output(stdout)
            if p.returncode != 0:
                if type(decoded_out) is dict:
                    raise ArduinoError(decoded_out[CommandBase.__ERROR_MESSAGE],
                                       decoded_out[CommandBase.__ERROR_CAUSE],
                                       stderr)
                raise ArduinoError(decoded_out,
                                   None,
                                   stderr)
            return decoded_out
        except OSError:
            raise ArduinoError(messages.ERROR_OSERROR % self._base_args[0])
