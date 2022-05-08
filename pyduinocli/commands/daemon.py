from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands
from pyduinocli.constants import flags


class DaemonCommand(CommandBase):
    """
    This class wraps the call to the :code:`daemon` command of :code:`arduino-cli`.
    """

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.DAEMON)

    def __call__(self, daemonize=None, port=None, debug=None, debug_filter=None, ip=None, debug_file=None):
        """
        Calls the :code:`daemon` command

        :param daemonize: Do not terminate daemon process if the parent process dies
        :type daemonize: bool or NoneType
        :param port: The TCP port the daemon will listen to
        :type port: str, integer or NoneType
        :param debug: Enable debug logging of gRPC calls
        :type debug: bool or NoneType
        :param debug_filter: Display only the provided gRPC calls
        :type debug_filter: str or NoneType
        :param ip: The IP address the daemon will listen to (default "127.0.0.1")
        :type ip: str or NoneType
        :param debug_file: Append debug logging to the specified file
        :type debug_file: str or NoneType
        :return: The output of the related command
        :rtype: dict
        """
        args = []
        if daemonize is True:
            args.append(flags.DAEMONIZE)
        if port:
            args.extend([flags.PORT, CommandBase._strip_arg(str(port))])
        if debug is True:
            args.append(flags.DEBUG)
        if debug_filter:
            args.extend([flags.DEBUG_FILTER, CommandBase._strip_arg(debug_filter)])
        if debug_file:
            args.extend([flags.DEBUG_FILE, CommandBase._strip_arg(debug_file)])
        return self._exec(args)
