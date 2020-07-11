from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands
from pyduinocli.constants import flags


class BurnBootloaderCommand(CommandBase):
    """
    This class wraps the call to the :code:`board` command of :code:`arduino-cli`
    """

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.BURN_BOOTLOADER)

    def __call__(self, fqbn=None, port=None, programmer=None, verify=None):
        args = []
        if fqbn:
            args.extend([flags.FQBN, CommandBase._strip_arg(fqbn)])
        if port:
            args.extend([flags.PORT, CommandBase._strip_arg(port)])
        if programmer:
            args.extend([flags.PROGRAMMER, CommandBase._strip_arg(programmer)])
        if verify is True:
            args.append(flags.VERIFY)
        return self._exec(args)
