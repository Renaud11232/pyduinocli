from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands
from pyduinocli.constants import flags


class ConfigCommand(CommandBase):

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.CONFIG)

    def dump(self):
        return self._exec([commands.DUMP])

    def init(self, save_as=None):
        args = [commands.INIT]
        if save_as:
            args.extend([flags.SAVE_AS, CommandBase._strip_arg(save_as)])
        return self._exec(args)
