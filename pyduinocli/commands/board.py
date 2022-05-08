from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands
from pyduinocli.constants import flags


class BoardCommand(CommandBase):
    """
    This class wraps the call to the :code:`board` command of :code:`arduino-cli`
    """

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.BOARD)

    def attach(self, port=None, fqbn=None, sketch_path=None, discovery_timeout=None, protocol=None, board_options=None):
        """
        Calls the :code:`board attach` command.

        :param port: Upload port address, e.g.: COM3 or /dev/ttyACM2
        :type port: str or NoneTYpe
        :param fqbn: Fully Qualified Board Name, e.g.: arduino:avr:uno
        :type fqbn: str or NoneTYpe
        :param sketch_path: The path of the sketch to attach to the board
        :type sketch_path: str or NoneTYpe
        :param discovery_timeout: Max time to wait for port discovery, e.g.: 30s, 1m (default 5s)
        :type discovery_timeout: str or NoneTYpe
        :param protocol: Upload port protocol, e.g: serial
        :type protocol: str or NoneTYpe
        :param board_options: Board options
        :type board_options: dict or NoneTYpe
        :return: The output of the related command
        :rtype: dict
        """
        args = [commands.ATTACH]
        if port:
            args.extend([flags.PORT, CommandBase._strip_arg(port)])
        if protocol:
            args.extend([flags.PROTOCOL, CommandBase._strip_arg(protocol)])
        if fqbn:
            args.extend([flags.FQBN, CommandBase._strip_arg(fqbn)])
        if sketch_path:
            args.append(CommandBase._strip_arg(sketch_path))
        if discovery_timeout:
            args.extend([flags.DISCOVERY_TIMEOUT, CommandBase._strip_arg(discovery_timeout)])
        if board_options:
            for option_name, option_value in board_options.items():
                option = "%s=%s" % (CommandBase._strip_arg(option_name), CommandBase._strip_arg(option_value))
                args.extend([flags.BOARD_OPTIONS, option])
        return self._exec(args)

    def details(self, fqbn, full=None, list_programmers=None, board_options=None):
        """
        Calls the :code:`board details` command.

        :param fqbn: The fqbn of the board
        :type fqbn: str
        :param full: Show full board details
        :type full: bool or NoneTYpe
        :param list_programmers: Show list of available programmers
        :type list_programmers: bool or NoneTYpe
        :param board_options: Board options
        :type board_options: dict or NoneTYpe
        :return: The output of the related command
        :rtype: dict
        """
        args = [commands.DETAILS, flags.FQBN, CommandBase._strip_arg(fqbn)]
        if full is True:
            args.append(flags.FULL)
        if list_programmers is True:
            args.append(flags.LIST_PROGRAMMERS)
        if board_options:
            for option_name, option_value in board_options.items():
                option = "%s=%s" % (CommandBase._strip_arg(option_name), CommandBase._strip_arg(option_value))
                args.extend([flags.BOARD_OPTIONS, option])
        return self._exec(args)

    def list(self, discovery_timeout=None, watch=None):
        """
        Calls the :code:`board list` command.

        :param discovery_timeout: Max time to wait for port discovery, e.g.: 30s, 1m (default 1s)
        :type discovery_timeout: str or NoneType
        :param watch: Command keeps running and prints list of connected boards whenever there is a change. Added to pyduinocli for completion but won't actually return, use a loop instead
        :type watch: bool or NoneTYpe
        :return: The output of the related command
        :rtype: dict
        """
        args = [commands.LIST]
        if discovery_timeout:
            args.extend([flags.DISCOVERY_TIMEOUT, CommandBase._strip_arg(discovery_timeout)])
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
        :return: The output of the related command
        :rtype: dict
        """
        args = [commands.LISTALL]
        if boardname:
            args.append(CommandBase._strip_arg(boardname))
        if show_hidden is True:
            args.append(flags.SHOW_HIDDEN)
        return self._exec(args)

    def search(self, boardname=None, show_hidden=None):
        """
        Calls the :code:`board search` command.

        :param boardname: The name of the board
        :type boardname: str or NoneType
        :param show_hidden: Show also boards marked as 'hidden' in the platform
        :type show_hidden: bool or NoneTYpe
        :return: The output of the related command
        :rtype: dict
        """
        args = [commands.SEARCH]
        if boardname:
            args.append(CommandBase._strip_arg(boardname))
        if show_hidden is True:
            args.append(flags.SHOW_HIDDEN)
        return self._exec(args)
