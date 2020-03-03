from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands
from pyduinocli.constants import flags


class DebugCommand(CommandBase):

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.DEBUG)

    def __call__(self, fqbn=None, input=None, port=None, sketch=None):
        args = []
        if fqbn:
            args.extend([flags.FQBN, CommandBase._strip_arg(fqbn)])
        if input:
            args.extend([flags.INPUT, CommandBase._strip_arg(input)])
        if port:
            args.extend([flags.PORT, CommandBase._strip_arg(port)])
        if sketch:
            args.append(CommandBase._strip_arg(sketch))
        return self._exec(args)
