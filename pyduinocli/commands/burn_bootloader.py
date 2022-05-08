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

    def __call__(self,
                 discovery_timeout=None, fqbn=None, port=None, programmer=None, protocol=None, verify=None,
                 board_options=None):
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
        :param discovery_timeout: Max time to wait for port discovery, e.g.: 30s, 1m (default 5s)
        :type discovery_timeout: str or NoneType
        :param protocol: Upload port protocol, e.g: serial
        :type protocol: str or NoneType
        :param board_options: Board options
        :type board_options: dict or NoneTYpe
        :return: The output of the related command
        :rtype: dict
        """
        args = []
        if discovery_timeout:
            args.extend([flags.DISCOVERY_TIMEOUT, CommandBase._strip_arg(discovery_timeout)])
        if fqbn:
            args.extend([flags.FQBN, CommandBase._strip_arg(fqbn)])
        if port:
            args.extend([flags.PORT, CommandBase._strip_arg(port)])
        if programmer:
            args.extend([flags.PROGRAMMER, CommandBase._strip_arg(programmer)])
        if protocol:
            args.extend([flags.PROTOCOL, CommandBase._strip_arg(protocol)])
        if verify is True:
            args.append(flags.VERIFY)
        if board_options:
            for option_name, option_value in board_options.items():
                option = "%s=%s" % (CommandBase._strip_arg(option_name), CommandBase._strip_arg(option_value))
                args.extend([flags.BOARD_OPTIONS, option])
        return self._exec(args)
