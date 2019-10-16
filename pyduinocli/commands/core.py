from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands
from pyduinocli.constants import flags


class CoreCommand(CommandBase):

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.CORE)
        
    def download(self, downloads):
        args = [commands.DOWNLOAD]
        args.extend(CommandBase._strip_args(downloads))
        return self._exec(args)

    def install(self, installs):
        args = [commands.INSTALL]
        args.extend(CommandBase._strip_args(installs))
        return self._exec(args)

    def list(self, updatable=None):
        args = [commands.LIST]
        if updatable is True:
            args.append(flags.UPDATABLE)
        return self._exec(args)

    def search(self, keywords):
        args = [commands.SEARCH]
        args.extend(CommandBase._strip_args(keywords))
        return self._exec(args)

    def uninstall(self, installs):
        args = [commands.UNINSTALL]
        args.extend(CommandBase._strip_args(installs))
        return self._exec(args)

    def update_index(self):
        return self._exec([commands.UPDATE_INDEX])

    def upgrade(self, upgrades=None):
        if not upgrades:
            upgrades = []
        args = [commands.UPGRADE]
        args.extend(CommandBase._strip_args(upgrades))
        return self._exec(args)