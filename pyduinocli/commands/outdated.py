from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands


class OutdatedCommand(CommandBase):
    """
    This class wraps the call to the :code:`outdated` command of :code:`arduino-cli`.
    """

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.OUTDATED)

    def __call__(self):
        """
        Calls the :code:`outdated` command

        :return: The list of outdated cores and libraries that can be upgraded
        :rtype: str or dict
        """
        return self._exec([])
