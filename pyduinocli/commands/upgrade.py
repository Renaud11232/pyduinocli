from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands
from pyduinocli.constants import flags


class UpgradeCommand(CommandBase):
    """
    This class wraps the call to the :code:`upgrade` command of :code:`arduino-cli`.
    """

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.UPGRADE)

    def __call__(self, run_post_install=None, skip_post_install=None, run_pre_uninstall=None, skip_pre_uninstall=None):
        """
        Calls the :code:`upgrade` command

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
        args = []
        if run_post_install is True:
            args.append(flags.RUN_POST_INSTALL)
        if skip_post_install is True:
            args.append(flags.SKIP_POST_INSTALL)
        if run_pre_uninstall is True:
            args.append(flags.RUN_PRE_UNINSTALL)
        if skip_pre_uninstall is True:
            args.append(flags.SKIP_PRE_UNINSTALL)
        return self._exec(args)
