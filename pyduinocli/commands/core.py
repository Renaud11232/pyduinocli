from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands
from pyduinocli.constants import flags


class CoreCommand(CommandBase):

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.CORE)
        
    def core_download(self, downloads):
        args = [commands.CORE, commands.DOWNLOAD]
        args.extend(CommandBase._strip_args(downloads))
        return self._exec(args)

    def core_install(self, installs):
        args = [commands.CORE, commands.INSTALL]
        args.extend(CommandBase._strip_args(installs))
        return self._exec(args)

    def core_list(self, updatable=None):
        args = [commands.CORE, commands.LIST]
        if updatable is True:
            args.append(flags.UPDATABLE)
        return self._exec(args)

    def core_search(self, keywords):
        args = [commands.CORE, commands.SEARCH]
        args.extend(CommandBase._strip_args(keywords))
        return self._exec(args)

    def core_uninstall(self, installs):
        args = [commands.CORE, commands.UNINSTALL]
        args.extend(CommandBase._strip_args(installs))
        return self._exec(args)

    def core_update_index(self):
        return self._exec([commands.CORE, commands.UPDATE_INDEX])

    def core_upgrade(self, upgrades=None):
        if upgrades is None:
            upgrades = []
        args = [commands.CORE, commands.UPGRADE]
        args.extend(CommandBase._strip_args(upgrades))
        return self._exec(args)
