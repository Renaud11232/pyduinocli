from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands
from pyduinocli.constants import flags


class ConfigCommand(CommandBase):

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.CONFIG)

    def dump(self):
        return self._exec([commands.DUMP])

    def init(self, dest_dir=None):
        args = [commands.INIT]
        if dest_dir:
            args.extend([flags.DEST_DIR, CommandBase._strip_arg(dest_dir)])
        return self._exec(args)
