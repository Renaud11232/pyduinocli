from subprocess import Popen, PIPE
import json
import re


class ArduinoError(Exception):

    def __init__(self, message, cause=None, stderr=None):
        self.message = message
        self.cause = cause
        self.stderr = stderr


class Arduino:

    __FORMAT_JSON = 'json'

    __FLAG_ADDITIONAL_URLS = '--additional-urls'
    __FLAG_CONFIG_FILE = '--config-file'
    __FLAG_FORMAT = '--format'
    __FLAG_LOG_FILE = '--log-file'
    __FLAG_LOG_FORMAT = '--log-format'
    __FLAG_LOG_LEVEL = '--log-level'
    __FLAG_TIMEOUT = '--timeout'
    __FLAG_BUILD_CACHE_PATH = '--build-cache-path'
    __FLAG_BUILD_PATH = '--build-path'
    __FLAG_BUILD_PROPERTIES = '--build-properties'
    __FLAG_FQBN = '--fqbn'
    __FLAG_OUTPUT = '--ouput'
    __FLAG_UPLOAD = '--upload'
    __FLAG_PREPROCESS = '--preprocess'
    __FLAG_SHOW_PROPERTIES = '--show-properties'
    __FLAG_VID_PID = '--vid-pid'
    __FLAG_WARNINGS = '--warnings'
    __FLAG_DEFAULT = '--default'
    __FLAG_SAVE_AS = '--save-as'
    __FLAG_VERIFY = '--verify'
    __FLAG_INPUT = '--input'
    __FLAG_PORT = '--port'
    __FLAG_UPDATABLE = '--updatable'
    __FLAG_NAMES = '--names'
    __FLAG_ALL = '--all'

    __COMMAND_BOARD = 'board'
    __COMMAND_ATTACH = 'attach'
    __COMMAND_DETAILS = 'details'
    __COMMAND_LIST = 'list'
    __COMMAND_LISTALL = 'listall'
    __COMMAND_COMPILE = 'compile'
    __COMMAND_CONFIG = 'config'
    __COMMAND_DUMP = 'dump'
    __COMMAND_INIT = 'init'
    __COMMAND_CORE = 'core'
    __COMMAND_DOWNLOAD = 'download'
    __COMMAND_INSTALL = 'install'
    __COMMAND_SEARCH = 'search'
    __COMMAND_UNINSTALL = 'uninstall'
    __COMMAND_UPDATE_INDEX = 'update-index'
    __COMMAND_UPGRADE = 'upgrade'
    __COMMAND_DAEMON = 'daemon'
    __COMMAND_LIB = 'lib'
    __COMMAND_SKETCH = 'sketch'
    __COMMAND_NEW = 'new'
    __COMMAND_UPLOAD = 'upload'
    __COMMAND_VERSION = 'version'

    __REGEX_JSON = r'(\{|\[)'

    __ERROR_MESSAGE = "Message"
    __ERROR_CAUSE = "Cause"
    __ERROR_OSERROR = "'%s' does not exist or is not an executable"
    __ERROR_ARDUINO_INSTANCE = "Could not create an Arduino instance"
    __ERROR_ARDUINO_PATH = "Arduino path is missing"
    __ERROR_PORT_FQBN_SET = 'port and fqbn cannot both be set'
    __ERROR_PORT_FQBN_NOT_SET = 'port or fqbn must be set'

    def __init__(self, cli_path, config_file=None, additional_urls=None, log_file=None, log_format=None, log_level=None):
        if not cli_path:
            raise ArduinoError(Arduino.__ERROR_ARDUINO_INSTANCE, Arduino.__ERROR_ARDUINO_PATH)
        self.__command_base = [cli_path, Arduino.__FLAG_FORMAT, Arduino.__FORMAT_JSON]
        if config_file is not None:
            self.__command_base.extend([Arduino.__FLAG_CONFIG_FILE, Arduino.__strip_arg(config_file)])
        if additional_urls is not None:
            self.__command_base.extend([Arduino.__FLAG_ADDITIONAL_URLS, ",".join(Arduino.__strip_args(additional_urls))])
        if log_file is not None:
            self.__command_base.extend([Arduino.__FLAG_LOG_FILE, Arduino.__strip_arg(log_file)])
        if log_format is not None:
            self.__command_base.extend([Arduino.__FLAG_LOG_FORMAT, Arduino.__strip_arg(log_format)])
        if log_level is not None:
            self.__command_base.extend([Arduino.__FLAG_LOG_LEVEL, Arduino.__strip_arg(log_level)])

    @staticmethod
    def __strip_arg(arg):
        return arg.lstrip("-")

    @staticmethod
    def __strip_args(args):
        out = list()
        for arg in args:
            out.append(Arduino.__strip_arg(arg))
        return out

    @staticmethod
    def __parse_output(data):
        pattern = re.compile(Arduino.__REGEX_JSON)
        for match in pattern.finditer(data):
            candidate = data[match.start():]
            try:
                return json.loads(candidate)
            except ValueError:
                continue
        return data

    def __exec(self, args):
        command = list(self.__command_base)
        command.extend(args)
        try:
            p = Popen(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
            stdout, stderr = p.communicate()
            decoded_out = self.__parse_output(stdout)
            if p.returncode != 0:
                if type(decoded_out) is dict:
                    raise ArduinoError(decoded_out[Arduino.__ERROR_MESSAGE],
                                       decoded_out[Arduino.__ERROR_CAUSE],
                                       stderr)
                raise ArduinoError(decoded_out,
                                   None,
                                   stderr)
            return decoded_out
        except OSError:
            raise ArduinoError(Arduino.__ERROR_OSERROR % self.__command_base[0])

    def board_attach(self, port=None, fqbn=None, sketch_path=None, timeout=None):
        args = [Arduino.__COMMAND_BOARD, Arduino.__COMMAND_ATTACH]
        if port is not None and fqbn is not None:
            raise ArduinoError(Arduino.__ERROR_PORT_FQBN_SET)
        if port is None and fqbn is None:
            raise ArduinoError(Arduino.__ERROR_PORT_FQBN_NOT_SET)
        if port is not None:
            args.append(Arduino.__strip_arg(port))
        if fqbn is not None:
            args.append(Arduino.__strip_arg(fqbn))
        if sketch_path is not None:
            args.append(Arduino.__strip_arg(sketch_path))
        if timeout is not None:
            args.extend([Arduino.__FLAG_TIMEOUT, Arduino.__strip_arg(timeout)])
        return self.__exec(args)

    def board_details(self, fqbn):
        args = [Arduino.__COMMAND_BOARD, Arduino.__COMMAND_DETAILS, Arduino.__strip_arg(fqbn)]
        return self.__exec(args)

    def board_list(self, timeout=None):
        args = [Arduino.__COMMAND_BOARD, Arduino.__COMMAND_LIST]
        if timeout is not None:
            args.extend([Arduino.__FLAG_TIMEOUT, Arduino.__strip_arg(timeout)])
        return self.__exec(args)

    def board_listall(self, boardname=None):
        args = [Arduino.__COMMAND_BOARD, Arduino.__COMMAND_LISTALL]
        if boardname is not None:
            args.append(Arduino.__strip_arg(boardname))
        return self.__exec(args)

    def compile(self,
                sketch, build_cache_path=None, build_path=None, build_properties=None, fqbn=None, output=None,
                port=None, preprocess=None, show_properties=None, upload=None, verify=None, vid_pid=None, warnings=None):
        args = [Arduino.__COMMAND_COMPILE]
        if build_cache_path is not None:
            args.extend([Arduino.__FLAG_BUILD_CACHE_PATH, Arduino.__strip_arg(build_cache_path)])
        if build_path is not None:
            args.extend([Arduino.__FLAG_BUILD_PATH, Arduino.__strip_arg(build_path)])
        if build_properties is not None:
            args.extend([Arduino.__FLAG_BUILD_PROPERTIES, Arduino.__strip_arg(build_properties)])
        if fqbn is not None:
            args.extend([Arduino.__FLAG_FQBN, Arduino.__strip_arg(fqbn)])
        if output is not None:
            args.extend([Arduino.__FLAG_OUTPUT, Arduino.__strip_arg(output)])
        if port is not None:
            args.extend([Arduino.__FLAG_PORT, Arduino.__strip_arg(port)])
        if preprocess is True:
            args.append(Arduino.__FLAG_PREPROCESS)
        if show_properties is True:
            args.append(Arduino.__FLAG_SHOW_PROPERTIES)
        if upload is True:
            args.append(Arduino.__FLAG_UPLOAD)
        if verify is True:
            args.append(Arduino.__FLAG_VERIFY)
        if vid_pid is not None:
            args.extend([Arduino.__FLAG_VID_PID, Arduino.__strip_arg(vid_pid)])
        if warnings is not None:
            args.extend([Arduino.__FLAG_WARNINGS, Arduino.__strip_arg(warnings)])
        args.append(Arduino.__strip_arg(sketch))
        return self.__exec(args)

    def config_dump(self):
        return self.__exec([Arduino.__COMMAND_CONFIG, Arduino.__COMMAND_DUMP])

    def config_init(self, save_as=None):
        args = [Arduino.__COMMAND_CONFIG, Arduino.__COMMAND_INIT, Arduino.__FLAG_DEFAULT]
        if save_as is not None:
            args.extend([Arduino.__FLAG_SAVE_AS, Arduino.__strip_arg(save_as)])
        return self.__exec(args)

    def core_download(self, downloads):
        args = [Arduino.__COMMAND_CORE, Arduino.__COMMAND_DOWNLOAD]
        args.extend(Arduino.__strip_args(downloads))
        return self.__exec(args)

    def core_install(self, installs):
        args = [Arduino.__COMMAND_CORE, Arduino.__COMMAND_INSTALL]
        args.extend(Arduino.__strip_args(installs))
        return self.__exec(args)

    def core_list(self, updatable=None):
        args = [Arduino.__COMMAND_CORE, Arduino.__COMMAND_LIST]
        if updatable is True:
            args.append(Arduino.__FLAG_UPDATABLE)
        return self.__exec(args)

    def core_search(self, keywords):
        args = [Arduino.__COMMAND_CORE, Arduino.__COMMAND_SEARCH]
        args.extend(Arduino.__strip_args(keywords))
        return self.__exec(args)

    def core_uninstall(self, installs):
        args = [Arduino.__COMMAND_CORE, Arduino.__COMMAND_UNINSTALL]
        args.extend(Arduino.__strip_args(installs))
        return self.__exec(args)

    def core_update_index(self):
        return self.__exec([Arduino.__COMMAND_CORE, Arduino.__COMMAND_UPDATE_INDEX])

    def core_upgrade(self, upgrades=None):
        if upgrades is None:
            upgrades = []
        args = [Arduino.__COMMAND_CORE, Arduino.__COMMAND_UPGRADE]
        args.extend(Arduino.__strip_args(upgrades))
        return self.__exec(args)

    def daemon(self):
        args = [Arduino.__COMMAND_DAEMON]
        return self.__exec(args)

    def lib_download(self, downloads):
        args = [Arduino.__COMMAND_LIB, Arduino.__COMMAND_DOWNLOAD]
        args.extend(Arduino.__strip_args(downloads))
        return self.__exec(args)

    def lib_install(self, installs):
        args = [Arduino.__COMMAND_LIB, Arduino.__COMMAND_INSTALL]
        args.extend(Arduino.__strip_args(installs))
        return self.__exec(args)

    def lib_list(self, all=None, updatable=None):
        args = [Arduino.__COMMAND_LIB, Arduino.__COMMAND_LIST]
        if all is True:
            args.append(Arduino.__FLAG_ALL)
        if updatable is True:
            args.append(Arduino.__FLAG_UPDATABLE)
        return self.__exec(args)

    def lib_search(self, name, names=None):
        args = [Arduino.__COMMAND_LIB, Arduino.__COMMAND_SEARCH]
        if names is True:
            args.append(Arduino.__FLAG_NAMES)
        args.extend(Arduino.__strip_args(name))
        return self.__exec(args)

    def lib_uninstall(self, uninstalls):
        args = [Arduino.__COMMAND_LIB, Arduino.__COMMAND_UNINSTALL]
        args.extend(Arduino.__strip_args(uninstalls))
        return self.__exec(args)

    def lib_update_index(self):
        return self.__exec([Arduino.__COMMAND_LIB, Arduino.__COMMAND_UPDATE_INDEX])

    def lib_upgrade(self, upgrades=None):
        if upgrades is None:
            upgrades = []
        args = [Arduino.__COMMAND_LIB, Arduino.__COMMAND_UPGRADE]
        args.extend(Arduino.__strip_args(upgrades))
        return self.__exec(args)

    def sketch_new(self, name):
        return self.__exec([Arduino.__COMMAND_SKETCH, Arduino.__COMMAND_NEW, Arduino.__strip_arg(name)])

    def upload(self, sketch=None, fqbn=None, input=None, port=None, verify=None):
        args = [Arduino.__COMMAND_UPLOAD]
        if fqbn is not None:
            args.extend([Arduino.__FLAG_FQBN, Arduino.__strip_arg(fqbn)])
        if input is not None:
            args.extend([Arduino.__FLAG_INPUT, Arduino.__strip_arg(input)])
        if port is not None:
            args.extend([Arduino.__FLAG_PORT, Arduino.__strip_arg(port)])
        if verify is True:
            args.append(Arduino.__FLAG_VERIFY)
        if sketch is not None:
            args.append(Arduino.__strip_arg(sketch))
        return self.__exec(args)

    def version(self):
        return self.__exec([Arduino.__COMMAND_VERSION])
