from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands
from pyduinocli.constants import flags


class BurnBootloaderCommand(CommandBase):
    """
    This class wraps the call to the :code:`burn-bootloader` command of :code:`arduino-cli`
    """

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.BURN_BOOTLOADER)

    def __call__(self, fqbn=None, port=None, programmer=None, verify=None):
        """
        Calls the :code:`burn-bootloader` command

        :param fqbn: The fqbn of the board to burn
        :type fqbn: str or NoneType
        :param port: The port to use to burl the bootloader
        :type port: str or NoneTYpe
        :param programmer: The programmer to use for the burning process
        :type programmer: str or NoneTYpe
        :param verify: Verifies that the bootloader was successfully burnt
        :type verify: bool or NoneTYpe
        :return: The output of the command
        :rtype: str or dict
        """
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
