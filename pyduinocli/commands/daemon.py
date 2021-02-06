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

    def __call__(self, daemonize=None, port=None):
        """
        Calls the :code:`daemon` command

        :param daemonize: Do not terminate daemon process if the parent process dies
        :type daemonize: bool or NoneType
        :param port: The TCP port the daemon will listen to
        :type port: str or NoneType
        :return: Nothing since this will not return and should be run in a separate thread or process
        """
        args = []
        if daemonize is True:
            args.append(flags.DAEMONIZE)
        if port:
            args.extend([flags.PORT, CommandBase._strip_arg(str(port))])
        return self._exec(args)
