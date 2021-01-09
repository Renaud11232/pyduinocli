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

    def __call__(self, run_post_install=None, skip_post_install=None):
        """
        Calls the :code:`upgrade` command

        :return: Nothing (an empty string)
        :rtype: str or dict
        """
        args = []
        if run_post_install is True:
            args.append(flags.RUN_POST_INSTALL)
        if skip_post_install is True:
            args.append(flags.SKIP_POST_INSTALL)
        return self._exec(args)
