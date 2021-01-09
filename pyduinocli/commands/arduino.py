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
from pyduinocli.commands.burn_bootloader import BurnBootloaderCommand
from pyduinocli.commands.completion import CompletionCommand
from pyduinocli.commands.outdated import OutdatedCommand
from pyduinocli.commands.update import UpdateCommand
from pyduinocli.commands.upgrade import UpgradeCommand
from pyduinocli.constants import flags


class ArduinoCliCommand(CommandBase):
    """
    This is the main class of pyduinocli. This class wraps all calls to :code:`arduino-cli`.

    This is the only class that a user should create instances of.
    """

    __FORMAT_JSON = 'json'

    def __init__(self, cli_path="arduino-cli", config_file=None, additional_urls=None, log_file=None, log_format=None,
                 log_level=None):
        """
        :param cli_path: The :code:`arduino-cli` command name if available in :code:`$PATH`. Can also be a direct path the the executable
        :type cli_path: str
        :param config_file: The path to the :code:`arduino-cli` configuration file to be used
        :type config_file: str or NoneType
        :param additional_urls: A list of URLs to custom board definitions files
        :type additional_urls: list or NoneType
        :param log_file: A path to a file where logs will be stored
        :type log_file: str or NoneType
        :param log_format: The format the logs will use
        :type log_format: str or NoneType
        :param log_level: The log level for the log file
        :type log_level: str or NoneType
        """
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
        self.__board = BoardCommand(self._base_args)
        self.__cache = CacheCommand(self._base_args)
        self.__compile = CompileCommand(self._base_args)
        self.__config = ConfigCommand(self._base_args)
        self.__core = CoreCommand(self._base_args)
        self.__daemon = DaemonCommand(self._base_args)
        self.__debug = DebugCommand(self._base_args)
        self.__lib = LibCommand(self._base_args)
        self.__sketch = SketchCommand(self._base_args)
        self.__upload = UploadCommand(self._base_args)
        self.__version = VersionCommand(self._base_args)
        self.__burn_bootloader = BurnBootloaderCommand(self._base_args)
        self.__completion = CompletionCommand(self._base_args)
        self.__outdated = OutdatedCommand(self._base_args)
        self.__update = UpdateCommand(self._base_args)
        self.__upgrade = UpgradeCommand(self._base_args)

    @property
    def board(self):
        """
        The board command wrapper for this :code:`arduino-cli` wrapper

        :type: :class:`pyduinocli.commands.board.BoardCommand`
        """
        return self.__board

    @property
    def cache(self):
        """
        The cache command wrapper for this :code:`arduino-cli` wrapper

        :type: :class:`pyduinocli.commands.cache.CacheCommand`
        """
        return self.__cache

    @property
    def compile(self):
        """
        The compile command wrapper for this :code:`arduino-cli` wrapper

        :type: :class:`pyduinocli.commands.compile.CompileCommand`
        """
        return self.__compile

    @property
    def config(self):
        """
        The config command wrapper for this :code:`arduino-cli` wrapper

        :type: :class:`pyduinocli.commands.config.ConfigCommand`
        """
        return self.__config

    @property
    def core(self):
        """
        The core command wrapper for this :code:`arduino-cli` wrapper

        :type: :class:`pyduinocli.commands.core.CoreCommand`
        """
        return self.__core

    @property
    def daemon(self):
        """
        The daemon command wrapper for this :code:`arduino-cli` wrapper

        :type: :class:`pyduinocli.commands.daemon.DaemonCommand`
        """
        return self.__daemon

    @property
    def debug(self):
        """
        The debug command wrapper for this :code:`arduino-cli` wrapper

        :type: :class:`pyduinocli.commands.debug.DebugCommand`
        """
        return self.__debug

    @property
    def lib(self):
        """
        The lib command wrapper for this :code:`arduino-cli` wrapper

        :type: :class:`pyduinocli.commands.lib.LibCommand`
        """
        return self.__lib

    @property
    def sketch(self):
        """
        The sketch command wrapper for this :code:`arduino-cli` wrapper

        :type: :class:`pyduinocli.commands.sketch.SketchCommand`
        """
        return self.__sketch

    @property
    def upload(self):
        """
        The upload command wrapper for this :code:`arduino-cli` wrapper

        :type: :class:`pyduinocli.commands.upload.UploadCommand`
        """
        return self.__upload

    @property
    def version(self):
        """
        The version command wrapper for this :code:`arduino-cli` wrapper

        :type: :class:`pyduinocli.commands.version.VersionCommand`
        """
        return self.__version

    @property
    def burn_bootloader(self):
        """
        The burn-bootloader command wrapper for this :code:`arduino-cli` wrapper

        :type: :class:`pyduinocli.commands.burn_bootloader.BurnBootloaderCommand`
        """
        return self.__burn_bootloader

    @property
    def completion(self):
        """
        The completion command wrapper for this :code:`arduino-cli` wrapper

        :type: :class:`pyduinocli.commands.completion.CompletionCommand`
        """
        return self.__completion

    @property
    def outdated(self):
        """
        The outdated command wrapper for this :code:`arduino-cli` wrapper

        :type: :class:`pyduinocli.commands.outdated.OutdatedCommand`
        """
        return self.__outdated

    @property
    def update(self):
        """
        The update command wrapper for this :code:`arduino-cli` wrapper

        :type: :class:`pyduinocli.commands.update.UpdateCommand`
        """
        return self.__update

    @property
    def upgrade(self):
        """
        The upgrade command wrapper for this :code:`arduino-cli` wrapper

        :type: :class:`pyduinocli.commands.upgrade.UpgradeCommand`
        """
        return self.__upgrade
