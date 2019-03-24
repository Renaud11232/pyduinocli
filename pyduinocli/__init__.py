from subprocess import Popen, PIPE
import json


class ArduinoError(Exception):

    def __init__(self, message, cause=None, stderr=None):
        self.message = message
        self.cause = cause
        self.stderr = stderr


class Arduino:

    KWARG_FLAVOUR = 'flavour'
    KWARG_TIMEOUT = 'timeout'
    KWARG_BUILD_CACHE_PATH = 'build_cache_path'
    KWARG_BUILD_PATH = 'build_path'
    KWARG_BUILD_PROPERTIES = 'build_properties'
    KWARG_FQBN = 'fqbn'
    KWARG_OUTPUT = 'output'
    KWARG_PREPROCESS = 'preprocess'
    KWARG_SHOW_PROPERTIES = 'show_properties'
    KWARG_VID_PID = 'vid_pid'
    KWARG_WARNINGS = 'warnings'
    KWARG_VERIFY = 'verify'
    KWARG_INPUT = 'input'
    KWARG_PORT = 'port'
    KWARG_UPDATABLE = 'updatable'
    KWARG_NAMES = 'names'

    FORMAT_JSON = 'json'

    FLAG_FORMAT = '--format'
    FLAG_CONFIG_FILE = '--config-file'
    FLAG_FLAVOUR = '--flavour'
    FLAG_TIMEOUT = '--timeout'
    FLAG_BUILD_CACHE_PATH = '--build-cache-path'
    FLAG_BUILD_PATH = '--build-path'
    FLAG_BUILD_PROPERTIES = '--build-properties'
    FLAG_FQBN = '--fqbn'
    FLAG_OUTPUT = '--ouput'
    FLAG_PREPROCESS = '--preprocess'
    FLAG_SHOW_PROPERTIES = '--show-properties'
    FLAG_VID_PID = '--vid-pid'
    FLAG_WARNINGS = '--warnings'
    FLAG_DEFAULT = '--default'
    FLAG_SAVE_AS = '--save-as'
    FLAG_VERIFY = '--verify'
    FLAG_INPUT = '--input'
    FLAG_PORT = '--port'
    FLAG_UPDATABLE = '--updatable'
    FLAG_NAMES = '--names'

    COMMAND_BOARD = 'board'
    COMMAND_ATTACH = 'attach'
    COMMAND_DETAILS = 'details'
    COMMAND_LIST = 'list'
    COMMAND_LISTALL = 'listall'
    COMMAND_COMPILE = 'compile'
    COMMAND_CONFIG = 'config'
    COMMAND_DUMP = 'dump'
    COMMAND_INIT = 'init'
    COMMAND_CORE = 'core'
    COMMAND_DOWNLOAD = 'download'
    COMMAND_INSTALL = 'install'
    COMMAND_SEARCH = 'search'
    COMMAND_UNINSTALL = 'uninstall'
    COMMAND_UPDATE_INDEX = 'update-index'
    COMMAND_UPGRADE = 'upgrade'
    COMMAND_LIB = 'lib'
    COMMAND_SKETCH = 'sketch'
    COMMAND_NEW = 'new'
    COMMAND_UPLOAD = 'upload'
    COMMAND_VERSION = 'version'

    ERROR_MESSAGE = "Message"
    ERROR_CAUSE = "Cause"
    ERROR_OSERROR = "'%s' does not exist or is not an executable"

    def __init__(self, cli_path, config_file=None):
        self.__command_base = [cli_path, Arduino.FLAG_FORMAT, Arduino.FORMAT_JSON]
        if config_file is not None:
            self.__command_base.extend([Arduino.FLAG_CONFIG_FILE, config_file])

    @staticmethod
    def __decode_output(data):
        try:
            return json.loads(data)
        except ValueError:
            return data.decode("utf-8")

    def __exec(self, args):
        command = list(self.__command_base)
        command.extend(args)
        try:
            p = Popen(command, stdout=PIPE, stderr=PIPE)
            stdout, stderr = p.communicate()
            decoded_out = self.__decode_output(stdout)
            if p.returncode != 0:
                if type(decoded_out) is dict:
                    raise ArduinoError(decoded_out[Arduino.ERROR_MESSAGE], decoded_out[Arduino.ERROR_CAUSE], stderr)
                raise ArduinoError(decoded_out)
            return decoded_out
        except OSError:
            raise ArduinoError(Arduino.ERROR_OSERROR % self.__command_base[0])

    def board_attach(self, port_fqbn, sketch_path=None, **kwargs):
        args = [Arduino.COMMAND_BOARD, Arduino.COMMAND_ATTACH, port_fqbn]
        if sketch_path is not None:
            args.append(sketch_path)
        if Arduino.KWARG_FLAVOUR in kwargs:
            args.extend([Arduino.FLAG_FLAVOUR, kwargs.get(Arduino.KWARG_FLAVOUR)])
        if Arduino.KWARG_TIMEOUT in kwargs:
            args.extend([Arduino.FLAG_TIMEOUT, Arduino.KWARG_TIMEOUT])
        return self.__exec(args)

    def board_details(self, fqbn):
        args = [Arduino.COMMAND_BOARD, Arduino.COMMAND_DETAILS, fqbn]
        return self.__exec(args)

    def board_list(self, **kwargs):
        args = [Arduino.COMMAND_BOARD, Arduino.COMMAND_LIST]
        if Arduino.KWARG_TIMEOUT in kwargs:
            args.extend([Arduino.FLAG_TIMEOUT, Arduino.KWARG_TIMEOUT])
        return self.__exec(args)

    def board_listall(self, boardname=None):
        args = [Arduino.COMMAND_BOARD, Arduino.COMMAND_LISTALL]
        if boardname is not None:
            args.append(boardname)
        return self.__exec(args)

    def compile(self, sketch, **kwargs):
        args = [Arduino.COMMAND_COMPILE]
        if Arduino.KWARG_BUILD_CACHE_PATH in kwargs:
            args.extend([Arduino.FLAG_BUILD_CACHE_PATH, kwargs.get(Arduino.KWARG_BUILD_CACHE_PATH)])
        if Arduino.KWARG_BUILD_PATH in kwargs:
            args.extend([Arduino.FLAG_BUILD_PATH, kwargs.get(Arduino.KWARG_BUILD_PATH)])
        if Arduino.KWARG_BUILD_PROPERTIES in kwargs:
            args.extend([Arduino.FLAG_BUILD_PROPERTIES, kwargs.get(Arduino.KWARG_BUILD_PROPERTIES)])
        if Arduino.KWARG_FQBN in kwargs:
            args.extend([Arduino.FLAG_FQBN, kwargs.get(Arduino.KWARG_FQBN)])
        if Arduino.KWARG_OUTPUT in kwargs:
            args.extend([Arduino.FLAG_OUTPUT, kwargs.get(Arduino.KWARG_OUTPUT)])
        if Arduino.KWARG_PREPROCESS in kwargs and kwargs.get(Arduino.KWARG_PREPROCESS) is True:
            args.append(Arduino.FLAG_PREPROCESS)
        if Arduino.KWARG_SHOW_PROPERTIES in kwargs and kwargs.get(Arduino.KWARG_SHOW_PROPERTIES) is True:
            args.append(Arduino.FLAG_SHOW_PROPERTIES)
        if Arduino.KWARG_VID_PID in kwargs:
            args.extend([Arduino.FLAG_VID_PID, kwargs.get(Arduino.KWARG_VID_PID)])
        if Arduino.KWARG_WARNINGS in kwargs:
            args.extend([Arduino.FLAG_WARNINGS, kwargs.get(Arduino.KWARG_WARNINGS)])
        args.append(sketch)
        return self.__exec(args)

    def config_dump(self):
        return self.__exec([Arduino.COMMAND_CONFIG, Arduino.COMMAND_DUMP])

    def config_init(self, save_as=None):
        args = [Arduino.COMMAND_CONFIG, Arduino.COMMAND_INIT, Arduino.FLAG_DEFAULT]
        if save_as is not None:
            args.extend([Arduino.FLAG_SAVE_AS, save_as])
        return self.__exec(args)

    def core_download(self, *downloads):
        args = [Arduino.COMMAND_CORE, Arduino.COMMAND_DOWNLOAD]
        args.extend(downloads)
        return self.__exec(args)

    def core_install(self, *installs):
        args = [Arduino.COMMAND_CORE, Arduino.COMMAND_INSTALL]
        args.extend(installs)
        return self.__exec(args)

    def core_list(self, **kwargs):
        args = [Arduino.COMMAND_CORE, Arduino.COMMAND_LIST]
        if Arduino.KWARG_UPDATABLE in kwargs and kwargs.get(Arduino.KWARG_UPDATABLE) is True:
            args.append(Arduino.FLAG_UPDATABLE)
        return self.__exec(args)

    def core_search(self, *keywords):
        args = [Arduino.COMMAND_CORE, Arduino.COMMAND_SEARCH]
        args.extend(keywords)
        return self.__exec(args)

    def core_uninstall(self, *installs):
        args = [Arduino.COMMAND_CORE, Arduino.COMMAND_UNINSTALL]
        args.extend(installs)
        return self.__exec(args)

    def core_update_index(self):
        return self.__exec([Arduino.COMMAND_CORE, Arduino.COMMAND_UPDATE_INDEX])

    def core_upgrade(self, *upgrades):
        args = [Arduino.COMMAND_CORE, Arduino.COMMAND_UPGRADE]
        args.extend(upgrades)
        return self.__exec(args)

    def lib_download(self, *downloads):
        args = [Arduino.COMMAND_LIB, Arduino.COMMAND_DOWNLOAD]
        args.extend(downloads)
        return self.__exec(args)

    def lib_install(self, *installs):
        args = [Arduino.COMMAND_LIB, Arduino.COMMAND_INSTALL]
        args.extend(installs)
        return self.__exec(args)

    def lib_list(self, **kwargs):
        args = [Arduino.COMMAND_LIB, Arduino.COMMAND_LIST]
        if Arduino.KWARG_UPDATABLE in kwargs and kwargs.get(Arduino.KWARG_UPDATABLE) is True:
            args.append(Arduino.FLAG_UPDATABLE)
        return self.__exec(args)

    def lib_search(self, *name, **kwargs):
        args = [Arduino.COMMAND_LIB, Arduino.COMMAND_SEARCH]
        if Arduino.KWARG_NAMES in kwargs and kwargs.get(Arduino.KWARG_NAMES) is True:
            args.append(Arduino.FLAG_NAMES)
        args.extend(name)
        return self.__exec(args)

    def lib_uninstall(self, *uninstalls):
        args = [Arduino.COMMAND_LIB, Arduino.COMMAND_UNINSTALL]
        args.extend(uninstalls)
        return self.__exec(args)

    def lib_update_index(self):
        return self.__exec([Arduino.COMMAND_LIB, Arduino.COMMAND_UPDATE_INDEX])

    def lib_upgrade(self):
        return self.__exec([Arduino.COMMAND_LIB, Arduino.COMMAND_UPGRADE])

    def sketch_new(self, name):
        return self.__exec([Arduino.COMMAND_SKETCH, Arduino.COMMAND_NEW, name])

    def upload(self, sketch, **kwargs):
        args = [Arduino.COMMAND_UPLOAD]
        if Arduino.KWARG_FQBN in kwargs:
            args.extend([Arduino.FLAG_FQBN, kwargs.get(Arduino.KWARG_FQBN)])
        if Arduino.KWARG_INPUT in kwargs:
            args.extend([Arduino.FLAG_INPUT, kwargs.get(Arduino.KWARG_INPUT)])
        if Arduino.KWARG_PORT in kwargs:
            args.extend([Arduino.FLAG_PORT, kwargs.get(Arduino.KWARG_PORT)])
        if Arduino.KWARG_VERIFY in kwargs and kwargs.get(Arduino.KWARG_VERIFY) is True:
            args.append(Arduino.FLAG_VERIFY)
        args.append(sketch)
        return self.__exec(args)

    def version(self):
        return self.__exec([Arduino.COMMAND_VERSION])
