from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands
from pyduinocli.constants import flags


class ConfigCommand(CommandBase):

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.CONFIG)

    def dump(self):
        return self._exec([commands.DUMP])

    def init(self, dest_dir=None, dest_file=None, overwrite=None):
        args = [commands.INIT]
        if dest_dir:
            args.extend([flags.DEST_DIR, CommandBase._strip_arg(dest_dir)])
        if dest_file:
            args.extend([flags.DEST_FILE, CommandBase._strip_arg(dest_file)])
        if overwrite is True:
            args.append(flags.OVERWRITE)
        return self._exec(args)

    def add(self, setting_name, values):
        args = [commands.ADD, CommandBase._strip_arg(setting_name)]
        args.extend(CommandBase._strip_args(values))
        return self._exec(args)

    def delete(self, setting_name):
        return self._exec([commands.DELETE, CommandBase._strip_arg(setting_name)])

    def remove(self, setting_name, values):
        args = [commands.REMOVE, CommandBase._strip_arg(setting_name)]
        args.extend(CommandBase._strip_args(values))
        return self._exec(args)

    def set(self, setting_name, values):
        args = [commands.SET, CommandBase._strip_arg(setting_name)]
        args.extend(CommandBase._strip_args(values))
        return self._exec(args)
