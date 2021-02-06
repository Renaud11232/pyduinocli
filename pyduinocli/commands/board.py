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

        :param port: The port of the board to attach
        :type port: str or NoneTYpe
        :param fqbn: The fqbn of the board to attach
        :type fqbn: str or NoneTYpe
        :param sketch_path: The path of the sketch to attach to the board
        :type sketch_path: str or NoneTYpe
        :param timeout: The connected devices search timeout, raise it if your board doesn't show up (e.g. to 10s). (default "5s")
        :type timeout: str or NoneTYpe
        :return: The output of the command
        :rtype: str or dict
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

    def details(self, fqbn, full=None, list_programmers=None):
        """
        Calls the :code:`board details` command.

        :param fqbn: The fqbn of the board
        :type fqbn: str
        :param full: Show full board details
        :type full: bool or NoneTYpe
        :param list_programmers: Show list of available programmers
        :type list_programmers: bool or NoneTYpe
        :return: The details for the given board
        :rtype: dict
        """
        args = [commands.DETAILS, flags.FQBN, CommandBase._strip_arg(fqbn)]
        if full is True:
            args.append(flags.FULL)
        if list_programmers is True:
            args.append(flags.LIST_PROGRAMMERS)
        return self._exec(args)

    def list(self, timeout=None, watch=None):
        """
        Calls the :code:`board list` command.

        :param timeout: The connected devices search timeout, raise it if your board doesn't show up (e.g. to 10s). (default "0s")
        :type timeout: str or NoneType
        :param watch: Command keeps running and prints list of connected boards whenever there is a change. Added to pyduinocli for completion but won't actually return, use a loop instead
        :type watch: bool or NoneTYpe
        :return: The list of found boards
        :rtype: dict
        """
        args = [commands.LIST]
        if timeout:
            args.extend([flags.TIMEOUT, CommandBase._strip_arg(timeout)])
        if watch is True:
            args.append(flags.WATCH)
        return self._exec(args)

    def listall(self, boardname=None, show_hidden=None):
        """
        Calls the :code:`board listall` command.

        :param boardname: The name of the board, all board will be returned if left unset (or None)
        :type boardname: str or NoneType
        :param show_hidden: Show also boards marked as 'hidden' in the platform
        :type show_hidden: bool or NoneTYpe
        :return: The list of all boards
        :rtype: dict
        """
        args = [commands.LISTALL]
        if boardname:
            args.append(CommandBase._strip_arg(boardname))
        if show_hidden is True:
            args.append(flags.SHOW_HIDDEN)
        return self._exec(args)
