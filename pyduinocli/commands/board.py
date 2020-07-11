from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands
from pyduinocli.constants import messages
from pyduinocli.constants import flags
from pyduinocli.errors.arduinoerror import ArduinoError


class BoardCommand(CommandBase):
    """
    This class wraps the call to the :code:`board` command of :code:`arduino-cli`
    """

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.BOARD)

    def attach(self, port=None, fqbn=None, sketch_path=None, timeout=None):
        """
        Calls the :code:`board attach` command.

        :param port:
        :param fqbn:
        :param sketch_path:
        :param timeout:
        :return:
        """
        args = [commands.ATTACH]
        if port and fqbn:
            raise ArduinoError(messages.ERROR_PORT_FQBN_SET)
        if not port and not fqbn:
            raise ArduinoError(messages.ERROR_PORT_FQBN_NOT_SET)
        if port:
            args.append(CommandBase._strip_arg(port))
        if fqbn:
            args.append(CommandBase._strip_arg(fqbn))
        if sketch_path:
            args.append(CommandBase._strip_arg(sketch_path))
        if timeout:
            args.extend([flags.TIMEOUT, CommandBase._strip_arg(timeout)])
        return self._exec(args)

    def details(self, fqbn, full=None):
        args = [commands.DETAILS, CommandBase._strip_arg(fqbn)]
        if full is True:
            args.append(flags.FULL)
        return self._exec(args)

    def list(self, timeout=None):
        args = [commands.LIST]
        if timeout:
            args.extend([flags.TIMEOUT, CommandBase._strip_arg(timeout)])
        return self._exec(args)

    def listall(self, boardname=None):
        args = [commands.LISTALL]
        if boardname:
            args.append(CommandBase._strip_arg(boardname))
        return self._exec(args)
