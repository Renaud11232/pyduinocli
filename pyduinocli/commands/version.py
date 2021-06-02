from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands


class VersionCommand(CommandBase):
    """
    This class wraps the call to the :code:`version` command of :code:`arduino-cli`.
    """

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.VERSION)

    def __call__(self):
        """
        Calls the :code:`version` command

        :return: The output of the related command
        :rtype: dict
        """
        return self._exec([])
