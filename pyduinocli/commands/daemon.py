from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands


class DaemonCommand(CommandBase):

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.DAEMON)

    def __call__(self):
        return self._exec([])
