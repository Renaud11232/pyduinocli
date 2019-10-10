from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands
from pyduinocli.constants import messages
from pyduinocli.constants import flags
from pyduinocli.errors import ArduinoError


class BoardCommand(CommandBase):

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.BOARD)

    def attach(self, port=None, fqbn=None, sketch_path=None, timeout=None):
        args = [commands.ATTACH]
        if port is not None and fqbn is not None:
            raise ArduinoError(messages.ERROR_PORT_FQBN_SET)
        if port is None and fqbn is None:
            raise ArduinoError(messages.ERROR_PORT_FQBN_NOT_SET)
        if port is not None:
            args.append(CommandBase._strip_arg(port))
        if fqbn is not None:
            args.append(CommandBase._strip_arg(fqbn))
        if sketch_path is not None:
            args.append(CommandBase._strip_arg(sketch_path))
        if timeout is not None:
            args.extend([flags.TIMEOUT, CommandBase._strip_arg(timeout)])
        return self._exec(args)

    def details(self, fqbn):
        args = [commands.DETAILS, CommandBase._strip_arg(fqbn)]
        return self._exec(args)

    def list(self, timeout=None):
        args = [commands.LIST]
        if timeout is not None:
            args.extend([flags.TIMEOUT, CommandBase._strip_arg(timeout)])
        return self._exec(args)

    def listall(self, boardname=None):
        args = [commands.LISTALL]
        if boardname is not None:
            args.append(CommandBase._strip_arg(boardname))
        return self._exec(args)
