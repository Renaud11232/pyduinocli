from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands
from pyduinocli.constants import flags


class MonitorCommand(CommandBase):
    """
    This class wraps the call to the :code:`monitor` command of :code:`arduino-cli`.
    """

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.MONITOR)

    def __call__(self, config=None, describe=None, discovery_timeout=None, fqbn=None, port=None, protocol=None,
                 quiet=None, board_options=None):
        """
        Calls the :code:`monitor` command

        :param config: Configuration of the port.
        :type config: str or NoneType
        :param describe: Show all the settings of the communication port.
        :type describe: bool or NoneType
        :param discovery_timeout: Max time to wait for port discovery, e.g.: 30s, 1m (default 5s)
        :type discovery_timeout: str or NoneType
        :param fqbn: Fully Qualified Board Name, e.g.: arduino:avr:uno
        :type fqbn: str or NoneType
        :param port: Upload port address, e.g.: COM3 or /dev/ttyACM2
        :type port: str or NoneType
        :param protocol: Upload port protocol, e.g: serial
        :type protocol: str or NoneType
        :param quiet: Run in silent mode, show only monitor input and output.
        :type quiet: bool or NoneType
        :param board_options: Board options
        :type board_options: dict or NoneTYpe
        :return: The output of the related command
        :rtype: dict
        """
        args = []
        if config:
            args.extend([flags.CONFIG, CommandBase._strip_arg(config)])
        if describe is True:
            args.append(flags.DESCRIBE)
        if discovery_timeout:
            args.extend([flags.DISCOVERY_TIMEOUT, CommandBase._strip_args(discovery_timeout)])
        if fqbn:
            args.extend([flags.FQBN, CommandBase._strip_arg(fqbn)])
        if port:
            args.extend([flags.PORT, CommandBase._strip_arg(port)])
        if protocol:
            args.extend([flags.PROTOCOL, CommandBase._strip_arg(protocol)])
        if quiet is True:
            args.append(flags.QUIET)
        if board_options:
            for option_name, option_value in board_options.items():
                option = "%s=%s" % (CommandBase._strip_arg(option_name), CommandBase._strip_arg(option_value))
                args.extend([flags.BOARD_OPTIONS, option])
        return self._exec(args)
