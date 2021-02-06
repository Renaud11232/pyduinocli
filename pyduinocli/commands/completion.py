from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands
from pyduinocli.constants import flags


class CompletionCommand(CommandBase):
    """
    This class wraps the call to the :code:`completion` command of :code:`arduino-cli`.
    """

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.COMPLETION)

    def __call__(self, shell, no_description=None):
        """
        Calls the :code:`completion` command

        :param shell: The shell name that will use completition
        :type shell: str
        :param no_description: Disable completion description for shells that support it
        :type no_description: bool or NoneTYpe
        :return: The script that will initialize completion
        :rtype: str
        """
        args = []
        if no_description is True:
            args.append(flags.NO_DESCRIPTION)
        args.append(CommandBase._strip_arg(shell))
        return self._exec(args)
