from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands
from pyduinocli.constants import flags


class LibCommand(CommandBase):

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.LIB)

    def download(self, downloads):
        args = [commands.LIB, commands.DOWNLOAD]
        args.extend(CommandBase._strip_args(downloads))
        return self._exec(args)

    def install(self, installs):
        args = [commands.LIB, commands.INSTALL]
        args.extend(CommandBase._strip_args(installs))
        return self._exec(args)

    def list(self, all=None, updatable=None):
        args = [commands.LIB, commands.LIST]
        if all is True:
            args.append(flags.ALL)
        if updatable is True:
            args.append(flags.UPDATABLE)
        return self._exec(args)

    def search(self, name, names=None):
        args = [commands.LIB, commands.SEARCH]
        if names is True:
            args.append(flags.NAMES)
        args.extend(CommandBase._strip_args(name))
        return self._exec(args)

    def uninstall(self, uninstalls):
        args = [commands.LIB, commands.UNINSTALL]
        args.extend(CommandBase._strip_args(uninstalls))
        return self._exec(args)

    def update_index(self):
        return self._exec([commands.LIB, commands.UPDATE_INDEX])

    def upgrade(self, upgrades=None):
        if upgrades is None:
            upgrades = []
        args = [commands.LIB, commands.UPGRADE]
        args.extend(CommandBase._strip_args(upgrades))
        return self._exec(args)
