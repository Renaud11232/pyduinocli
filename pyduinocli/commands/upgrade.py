from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands


class UpgradeCommand(CommandBase):
    """
    This class wraps the call to the :code:`upgrade` command of :code:`arduino-cli`.
    """

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.UPGRADE)

    def __call__(self):
        """
        Calls the :code:`upgrade` command

        :return: Nothing (an empty string)
        :rtype: str or dict
        """
        return self._exec([])
