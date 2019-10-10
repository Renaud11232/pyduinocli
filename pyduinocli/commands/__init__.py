import pyduinocli


class CommandBase:
    __ERROR_MESSAGE = "Message"
    __ERROR_CAUSE = "Cause"

    __FORMAT_JSON = 'json'

    __REGEX_JSON = r'(\{|\[)'

    def __init__(self, global_args, command_name):
        self.__command_base = list(global_args)
        self.__command_base.append(command_name)

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
        import re
        pattern = re.compile(CommandBase.__REGEX_JSON)
        for match in pattern.finditer(data):
            candidate = data[match.start():]
            try:
                import json
                return json.loads(candidate)
            except ValueError:
                continue
        return data

    def _exec(self, args):
        command = list(self.__command_base)
        command.extend(args)
        try:
            from subprocess import Popen, PIPE
            p = Popen(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
            stdout, stderr = p.communicate()
            decoded_out = self.__parse_output(stdout)
            if p.returncode != 0:
                if type(decoded_out) is dict:
                    raise pyduinocli.errors.ArduinoError(decoded_out[CommandBase.__ERROR_MESSAGE],
                                                         decoded_out[CommandBase.__ERROR_CAUSE],
                                                         stderr)
                raise pyduinocli.errors.ArduinoError(decoded_out,
                                                     None,
                                                     stderr)
            return decoded_out
        except OSError:
            raise pyduinocli.errors.ArduinoError(pyduinocli.constants.messages.ERROR_OSERROR % self.__command_base[0])
