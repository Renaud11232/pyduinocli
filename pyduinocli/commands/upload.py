from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands
from pyduinocli.constants import flags


class UploadCommand(CommandBase):

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.UPLOAD)

    def __call__(self, sketch=None, fqbn=None, input=None, port=None, verify=None):
        args = []
        if fqbn:
            args.extend([flags.FQBN, CommandBase._strip_arg(fqbn)])
        if input:
            args.extend([flags.INPUT, CommandBase._strip_arg(input)])
        if port:
            args.extend([flags.PORT, CommandBase._strip_arg(port)])
        if verify is True:
            args.append(flags.VERIFY)
        if sketch:
            args.append(CommandBase._strip_arg(sketch))
        return self._exec(args)
