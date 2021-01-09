from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands
from pyduinocli.constants import flags


class UpdateCommand(CommandBase):
    """
    This class wraps the call to the :code:`update` command of :code:`arduino-cli`.
    """

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.UPDATE)

    def __call__(self, show_outdated=None):
        """
        Calls the :code:`update` command

        :return: The list of outdated cores and libraries that can be upgraded if show_updated flag is True
        :rtype: str or dict
        """
        args = []
        if show_outdated is True:
            args.append(flags.SHOW_OUTDATED)
        return self._exec(args)
