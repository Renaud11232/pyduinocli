from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands
from pyduinocli.constants import flags


class CompletionCommand(CommandBase):

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.COMPLETION)

    def __call__(self, shell, no_description=None):
        args = []
        if no_description is True:
            args.append(flags.NO_DESCRIPTION)
        args.append(CommandBase._strip_arg(shell))
        return self._exec(args)
