from pyduinocli.commands.base import CommandBase
from pyduinocli.commands.board import BoardCommand
from pyduinocli.commands.cache import CacheCommand
from pyduinocli.commands.compile import CompileCommand
from pyduinocli.commands.config import ConfigCommand
from pyduinocli.commands.core import CoreCommand
from pyduinocli.commands.daemon import DaemonCommand
from pyduinocli.commands.debug import DebugCommand
from pyduinocli.commands.lib import LibCommand
from pyduinocli.commands.sketch import SketchCommand
from pyduinocli.commands.upload import UploadCommand
from pyduinocli.commands.version import VersionCommand
from pyduinocli.constants import flags


class ArduinoCliCommand(CommandBase):

    __FORMAT_JSON = 'json'

    def __init__(self, cli_path="arduino-cli", config_file=None, additional_urls=None, log_file=None, log_format=None,
                 log_level=None):
        base_args = [cli_path, flags.FORMAT, ArduinoCliCommand.__FORMAT_JSON]
        if config_file:
            base_args.extend([flags.CONFIG_FILE, CommandBase._strip_arg(config_file)])
        if additional_urls:
            base_args.extend([flags.ADDITIONAL_URLS, ",".join(CommandBase._strip_args(additional_urls))])
        if log_file:
            base_args.extend([flags.LOG_FILE, CommandBase._strip_arg(log_file)])
        if log_format:
            base_args.extend([flags.LOG_FORMAT, CommandBase._strip_arg(log_format)])
        if log_level:
            base_args.extend([flags.LOG_LEVEL, CommandBase._strip_arg(log_level)])
        CommandBase.__init__(self, base_args)
        self.board = BoardCommand(self._base_args)
        self.cache = CacheCommand(self._base_args)
        self.compile = CompileCommand(self._base_args)
        self.config = ConfigCommand(self._base_args)
        self.core = CoreCommand(self._base_args)
        self.daemon = DaemonCommand(self._base_args)
        self.debug = DebugCommand(self._base_args)
        self.lib = LibCommand(self._base_args)
        self.sketch = SketchCommand(self._base_args)
        self.upload = UploadCommand(self._base_args)
        self.version = VersionCommand(self._base_args)
