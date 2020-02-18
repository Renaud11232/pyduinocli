from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands


class CacheCommand(CommandBase):

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.CACHE)

    def clean(self):
        return self._exec([commands.CLEAN])
