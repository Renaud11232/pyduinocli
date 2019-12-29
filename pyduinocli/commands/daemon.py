from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands
from pyduinocli.constants import flags


class DaemonCommand(CommandBase):

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.DAEMON)

    def __call__(self, daemonize=None, port=None):
        args = []
        if daemonize is True:
            args.append(flags.DAEMONIZE)
        if port:
            args.extend([flags.PORT, CommandBase._strip_arg(str(port))])
        return self._exec(args)
