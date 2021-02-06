from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands


class CacheCommand(CommandBase):
    """
    This class wraps the call to the :code:`cache` command of :code:`arduino-cli`.
    """

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.CACHE)

    def clean(self):
        """
        Calls the :code:`cache clean` command

        :return: The result of the command
        :rtype: str or dict
        """
        return self._exec([commands.CLEAN])
