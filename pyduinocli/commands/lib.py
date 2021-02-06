from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands
from pyduinocli.constants import flags


class LibCommand(CommandBase):
    """
    This class wraps the call to the :code:`lib` command of :code:`arduino-cli`.
    """

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.LIB)

    def deps(self, library):
        """
        Calls the :code:`lib deps` command

        :param library: The name of the library for dependency checking
        :type library: str
        :return: The dependencies
        :rtype: dict
        """
        return self._exec([commands.DEPS, CommandBase._strip_arg(library)])

    def download(self, downloads):
        """
        Calls the :code:`lib download` command

        :param downloads: A list of libraries to download
        :type downloads: list
        :return: Nothing (an empty string)
        :rtype: str
        """
        args = [commands.DOWNLOAD]
        args.extend(CommandBase._strip_args(downloads))
        return self._exec(args)

    def install(self, libraries=None, git_urls=None, zip_paths=None):
        """
        Calls the :code:`lib install` command

        :param libraries: A list of libraries to install
        :type libraries: list or NoneType
        :param git_urls: A list of git repositories containing libraries to install
        :type git_urls: list or NoneType
        :param zip_paths: A list of paths to zip files to install
        :type zip_paths: list or NoneType
        :return: The libraries that were installed
        :rtype: str or dict
        """
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
        """
        Calls the :code:`lib list` command

        :param all: Includes built-in libraries
        :type all: bool or NoneType
        :param updatable: Only shows libraries that are not up to date
        :type updatable: bool or NoneType
        :param fqbn: Shows libraries for the specified board
        :type fqbn: str or NoneType
        :return: The installed libraries
        :rtype: dict
        """
        args = [commands.LIST]
        if all is True:
            args.append(flags.ALL)
        if updatable is True:
            args.append(flags.UPDATABLE)
        if fqbn is not None:
            args.extend([flags.FQBN, CommandBase._strip_arg(fqbn)])
        return self._exec(args)

    def search(self, keywords=None, names=None):
        """
        Calls the :code:`lib search` command

        :param keywords: A list of keywords to use to search, if None, all libraries will show up
        :type keywords: list or NoneType
        :param names: Only shows libraries names
        :type names: bool or NoneType
        :return: The found libraries matching keywords
        :rtype: dict
        """
        args = [commands.SEARCH]
        if names is True:
            args.append(flags.NAMES)
        if keywords is None:
            keywords = []
        if keywords:
            args.extend(CommandBase._strip_args(keywords))
        return self._exec(args)

    def uninstall(self, uninstalls):
        """
        Calls the :code:`lib uninstall` command

        :param uninstalls: A list of libraries to uninstall
        :type uninstalls: list
        :return: Nothing (an empty string)
        :rtype: str
        """
        args = [commands.UNINSTALL]
        args.extend(CommandBase._strip_args(uninstalls))
        return self._exec(args)

    def update_index(self):
        """
        Calls the :code:`lib update-index` command

        :return: Nothing (an empty string)
        :rtype: str
        """
        return self._exec([commands.UPDATE_INDEX])

    def upgrade(self, upgrades=None):
        """
        Calls the :code:`lib upgrade` command

        :param upgrades: A list of libraries to upgrade, if None, all libraries will be upgraded
        :type upgrades: list or NoneType
        :return: Nothing (an empty string)
        :rtype: str
        """
        if not upgrades:
            upgrades = []
        args = [commands.UPGRADE]
        args.extend(CommandBase._strip_args(upgrades))
        return self._exec(args)

    def examples(self, library, fqbn=None):
        """
        Calls the :code:`lib examples` command

        :param library: The name of the library
        :type library: str
        :param fqbn: The board FQBN
        :type fqbn: str or NoneType
        :return: The available examples
        :rtype: dict
        """
        args = [commands.EXAMPLES, CommandBase._strip_arg(library)]
        if fqbn is not None:
            args.extend([flags.FQBN, CommandBase._strip_arg(fqbn)])
        return self._exec(args)

