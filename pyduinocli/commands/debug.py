from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands
from pyduinocli.constants import flags


class DebugCommand(CommandBase):
    """
    This class wraps the call to the :code:`debug` command of :code:`arduino-cli`.
    Warning, While this has been added in pyduinocli, it has not been tested, and won't probably work since it will start an interactive gdb session and won't return
    """

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.DEBUG)

    def __call__(self, fqbn=None, input_dir=None, port=None, interpreter=None, info=None, programmer=None, sketch=None,
                 discovery_timeout=None, protocol=None, board_options=None):
        """
        Calls the :code:`debug` command

        :param fqbn: Fully Qualified Board Name, e.g.: arduino:avr:uno
        :type fqbn: str or NoneType
        :param input_dir: Directory containing binaries for debug.
        :type input_dir: str or NoneType
        :param port: Debug port, e.g.: COM10 or /dev/ttyACM0
        :type port: str or NoneType
        :param interpreter: Debug interpreter e.g.: console, mi, mi1, mi2, mi3 (default "console")
        :type interpreter: str or NoneType
        :param info: Show metadata about the debug session instead of starting the debugger.
        :type info: str or NoneType
        :param programmer: Programmer to use for debugging
        :type programmer: str or NoneType
        :param sketch: The sketch to debug
        :type sketch: str or NoneType
        :param discovery_timeout: Max time to wait for port discovery, e.g.: 30s, 1m (default 5s)
        :type discovery_timeout: str or NoneType
        :param protocol: Upload port protocol, e.g: serial
        :type protocol: str or NoneType
        :param board_options: Board options
        :type board_options: dict or NoneTYpe
        :return: The output of the related command
        :rtype: dict
        """
        args = []
        if fqbn:
            args.extend([flags.FQBN, CommandBase._strip_arg(fqbn)])
        if input_dir:
            args.extend([flags.INPUT_DIR, CommandBase._strip_arg(input_dir)])
        if port:
            args.extend([flags.PORT, CommandBase._strip_arg(port)])
        if interpreter:
            args.extend([flags.INTERPRETER, CommandBase._strip_arg(interpreter)])
        if info is True:
            args.append(flags.INFO)
        if programmer:
            args.extend([flags.PROGRAMMER, CommandBase._strip_arg(programmer)])
        if sketch:
            args.append(CommandBase._strip_arg(sketch))
        if discovery_timeout:
            args.extend([flags.DISCOVERY_TIMEOUT, CommandBase._strip_arg(discovery_timeout)])
        if protocol:
            args.extend([flags.PROTOCOL, CommandBase._strip_arg(protocol)])
        if board_options:
            for option_name, option_value in board_options.items():
                option = "%s=%s" % (CommandBase._strip_arg(option_name), CommandBase._strip_arg(option_value))
                args.extend([flags.BOARD_OPTIONS, option])
        return self._exec(args)
