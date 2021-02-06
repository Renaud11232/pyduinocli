from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands
from pyduinocli.constants import flags


class LibCommand(CommandBase):

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.LIB)

    def deps(self, library):
        return self._exec([commands.DEPS, CommandBase._strip_arg(library)])

    def download(self, downloads):
        args = [commands.DOWNLOAD]
        args.extend(CommandBase._strip_args(downloads))
        return self._exec(args)

    def install(self, libraries=None, git_urls=None, zip_paths=None):
        args = [commands.INSTALL]
        if libraries:
            args.extend(CommandBase._strip_args(libraries))
        if git_urls:
            args.append(flags.GIT_URL)
            args.extend(CommandBase._strip_args(git_urls))
        if zip_paths:
            args.append(flags.ZIP_PATH)
            args.extend(CommandBase._strip_args(zip_paths))
        return self._exec(args)

    def list(self, all=None, updatable=None, fqbn=None):
        args = [commands.LIST]
        if all is True:
            args.append(flags.ALL)
        if updatable is True:
            args.append(flags.UPDATABLE)
        if fqbn is not None:
            args.extend([flags.FQBN, CommandBase._strip_arg(fqbn)])
        return self._exec(args)

    def search(self, keywords=None, names=None):
        args = [commands.SEARCH]
        if names is True:
            args.append(flags.NAMES)
        if keywords is None:
            keywords = []
        if keywords:
            args.extend(CommandBase._strip_args(keywords))
        return self._exec(args)

    def uninstall(self, uninstalls):
        args = [commands.UNINSTALL]
        args.extend(CommandBase._strip_args(uninstalls))
        return self._exec(args)

    def update_index(self):
        return self._exec([commands.UPDATE_INDEX])

    def upgrade(self, upgrades=None):
        if not upgrades:
            upgrades = []
        args = [commands.UPGRADE]
        args.extend(CommandBase._strip_args(upgrades))
        return self._exec(args)

    def examples(self, library, fqbn=None):
        args = [commands.EXAMPLES, CommandBase._strip_arg(library)]
        if fqbn is not None:
            args.extend([flags.FQBN, CommandBase._strip_arg(fqbn)])
        return self._exec(args)

