from pyduinocli.errors import ArduinoError
from pyduinocli.commands.base import CommandBase
from pyduinocli.commands.board import BoardCommand
from pyduinocli.commands.compile import CompileCommand
from pyduinocli.commands.config import ConfigCommand
from pyduinocli.commands.core import CoreCommand
from pyduinocli.commands.daemon import DaemonCommand
from pyduinocli.commands.lib import LibCommand
from pyduinocli.commands.sketch import SketchCommand
from pyduinocli.constants import messages
from pyduinocli.constants import flags


class ArduinoCliCommand(CommandBase):

    __FORMAT_JSON = 'json'

    def __init__(self, cli_path, config_file=None, additional_urls=None, log_file=None, log_format=None,
                 log_level=None):
        if not cli_path:
            raise ArduinoError(messages.ERROR_ARDUINO_INSTANCE, messages.ERROR_ARDUINO_PATH)
        base_args = [cli_path, flags.FORMAT, ArduinoCliCommand.__FORMAT_JSON]
        if config_file is not None:
            base_args.extend([flags.CONFIG_FILE, CommandBase._strip_arg(config_file)])
        if additional_urls is not None:
            base_args.extend([flags.ADDITIONAL_URLS, ",".join(CommandBase._strip_args(additional_urls))])
        if log_file is not None:
            base_args.extend([flags.LOG_FILE, CommandBase._strip_arg(log_file)])
        if log_format is not None:
            base_args.extend([flags.LOG_FORMAT, CommandBase._strip_arg(log_format)])
        if log_level is not None:
            base_args.extend([flags.LOG_LEVEL, CommandBase._strip_arg(log_level)])
        CommandBase.__init__(self, base_args)
        self.board = BoardCommand(self._base_args)
        self.compile = CompileCommand(self._base_args)
        self.config = ConfigCommand(self._base_args)
        self.core = CoreCommand(self._base_args)
        self.daemon = DaemonCommand(self._base_args)
        self.lib = LibCommand(self._base_args)
        self.sketch = SketchCommand(self._base_args)
