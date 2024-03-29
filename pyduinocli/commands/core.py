from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands
from pyduinocli.constants import flags


class CoreCommand(CommandBase):
    """
    This class wraps the call to the :code:`core` command of :code:`arduino-cli`.
    """

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.CORE)
        
    def download(self, downloads):
        """
        Calls the :code:`core download` command

        :param downloads: A list of cores to download
        :type downloads: list
        :return: The output of the related command
        :rtype: dict
        """
        args = [commands.DOWNLOAD]
        args.extend(CommandBase._strip_args(downloads))
        return self._exec(args)

    def install(self, installs, run_post_install=None, skip_post_install=None, no_overwrite=None,
                run_pre_uninstall=None, skip_pre_uninstall=None):
        """
        Calls the :code:`core download` command

        :param installs: A list of cores to install
        :type installs: list
        :param run_post_install: Force run of post-install scripts
        :type run_post_install: bool or NoneType
        :param skip_post_install: Force skip of post-install scripts
        :type skip_post_install: bool or NoneType
        :param no_overwrite: Do not overwrite already installed platforms
        :type no_overwrite: bool or NoneType
        :param run_pre_uninstall: Force run of pre-uninstall scripts (if the CLI is not running interactively)
        :type run_pre_uninstall: bool or NoneType
        :param skip_pre_uninstall: Force skip of pre-uninstall scripts (if the CLI is running interactively).
        :type skip_pre_uninstall: bool or NoneType
        :return: The output of the related command
        :rtype: dict
        """
        args = [commands.INSTALL]
        args.extend(CommandBase._strip_args(installs))
        if run_post_install is True:
            args.append(flags.RUN_POST_INSTALL)
        if skip_post_install is True:
            args.append(flags.SKIP_POST_INSTALL)
        if no_overwrite is True:
            args.append(flags.NO_OVERWRITE)
        if run_pre_uninstall is True:
            args.append(flags.RUN_PRE_UNINSTALL)
        if skip_pre_uninstall is True:
            args.append(flags.SKIP_PRE_UNINSTALL)
        return self._exec(args)

    def list(self, updatable=None, all=None):
        """
        Calls the :code:`core list` command

        :param updatable: Only shows cores that are not up to date
        :type updatable: bool or NoneType
        :param all: Shows all installed and non installed cores (also shows manually installed cores)
        :type all: bool or NoneType
        :return: The output of the related command
        :rtype: dict
        """
        args = [commands.LIST]
        if updatable is True:
            args.append(flags.UPDATABLE)
        if all is True:
            args.append(flags.ALL)
        return self._exec(args)

    def search(self, keywords=None, all=None):
        """
        Calls the :code:`core search` command

        :param keywords: A list of keywords to use to search, if None, all cores will show up
        :type keywords: list or NoneType
        :param all: Shows all available core versions
        :type all: bool or NoneType
        :return: The output of the related command
        :rtype: dict
        """
        args = [commands.SEARCH]
        if keywords is None:
            keywords = []
        if keywords:
            args.extend(CommandBase._strip_args(keywords))
        if all is True:
            args.append(flags.ALL)
        return self._exec(args)

    def uninstall(self, uninstalls, run_post_install=None, run_pre_uninstall=None, skip_post_install=None,
                  skip_pre_uninstall=None):
        """
        Calls the :code:`core uninstall` command

        :param uninstalls: A list of cores to uninstall
        :type uninstalls: list
        :param run_post_install: Force run of post-install scripts (if the CLI is not running interactively).
        :type run_post_install: bool or NoneType
        :param run_pre_uninstall: Force run of pre-uninstall scripts (if the CLI is not running interactively).
        :type run_pre_uninstall: bool or NoneType
        :param skip_post_install: Force skip of post-install scripts (if the CLI is running interactively).
        :type skip_post_install: bool or NoneType
        :param skip_pre_uninstall: Force skip of pre-uninstall scripts (if the CLI is running interactively).
        :type skip_pre_uninstall: bool or NoneType
        :return: The output of the related command
        :rtype: dict
        """
        args = [commands.UNINSTALL]
        if run_post_install is True:
            args.append(flags.RUN_POST_INSTALL)
        if run_pre_uninstall is True:
            args.append(flags.RUN_PRE_UNINSTALL)
        if skip_post_install is True:
            args.append(flags.SKIP_POST_INSTALL)
        if skip_pre_uninstall is True:
            args.append(flags.SKIP_PRE_UNINSTALL)
        args.extend(CommandBase._strip_args(uninstalls))
        return self._exec(args)

    def update_index(self):
        """
        Calls the :code:`core update-index` command

        :return: The output of the related command
        :rtype: dict
        """
        return self._exec([commands.UPDATE_INDEX])

    def upgrade(self, upgrades=None, run_post_install=None, skip_post_install=None, run_pre_uninstall=None,
                skip_pre_uninstall=None):
        """
        Calls the :code:`core upgrade` command

        :param upgrades: A list of cores to upgrade, if None, all cores will be upgraded
        :type upgrades: list or NoneType
        :param run_post_install: Force run of post-install scripts
        :type run_post_install: bool or NoneType
        :param skip_post_install: Force skip of post-install scripts
        :type skip_post_install: bool or NoneType
        :param run_pre_uninstall: Force run of pre-uninstall scripts (if the CLI is not running interactively).
        :type run_pre_uninstall: bool or NoneType
        :param skip_pre_uninstall: Force skip of pre-uninstall scripts (if the CLI is running interactively).
        :type skip_pre_uninstall: bool or NoneType
        :return: The output of the related command
        :rtype: dict
        """
        if not upgrades:
            upgrades = []
        args = [commands.UPGRADE]
        args.extend(CommandBase._strip_args(upgrades))
        if run_post_install is True:
            args.append(flags.RUN_POST_INSTALL)
        if skip_post_install is True:
            args.append(flags.SKIP_POST_INSTALL)
        if run_pre_uninstall is True:
            args.append(flags.RUN_PRE_UNINSTALL)
        if skip_pre_uninstall is True:
            args.append(flags.SKIP_PRE_UNINSTALL)
        return self._exec(args)
