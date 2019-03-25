from subprocess import Popen, PIPE
import json
import regex


class ArduinoError(Exception):

    def __init__(self, message, cause=None, stderr=None):
        self.message = message
        self.cause = cause
        self.stderr = stderr


class Arduino:

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
    FLAG_ALL = '--all'

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
    def __parse_output(data):
        pattern = regex.compile(r"\{(?:[^{}]|(?R))*\}")
        match = pattern.search(data)
        if match is None:
            return data
        else:
            return json.loads(match.group())

    def __exec(self, args):
        command = list(self.__command_base)
        command.extend(args)
        try:
            p = Popen(command, stdout=PIPE, stderr=PIPE)
            stdout, stderr = p.communicate()
            decoded_out = self.__parse_output(stdout.decode("utf-8"))
            decoded_err = stderr.decode("utf-8")
            if p.returncode != 0:
                if type(decoded_out) is dict:
                    raise ArduinoError(decoded_out[Arduino.ERROR_MESSAGE],
                                       decoded_out[Arduino.ERROR_CAUSE],
                                       decoded_err)
                raise ArduinoError(decoded_out,
                                   None,
                                   decoded_err)
            return decoded_out
        except OSError:
            raise ArduinoError(Arduino.ERROR_OSERROR % self.__command_base[0])

    def board_attach(self, port=None, fqbn=None, sketch_path=None, flavour=None, timeout=None):
        args = [Arduino.COMMAND_BOARD, Arduino.COMMAND_ATTACH]
        if port is not None and fqbn is not None:
            raise ArduinoError("port and fqbn cannot both be set")
        if port is None and fqbn is None:
            raise ArduinoError("port or fqbn must be set")
        if port is not None:
            args.append(port)
        if fqbn is not None:
            args.append(fqbn)
        if sketch_path is not None:
            args.append(sketch_path)
        if flavour is not None:
            args.extend([Arduino.FLAG_FLAVOUR, flavour])
        if timeout is not None:
            args.extend([Arduino.FLAG_TIMEOUT, timeout])
        return self.__exec(args)

    def board_details(self, fqbn):
        args = [Arduino.COMMAND_BOARD, Arduino.COMMAND_DETAILS, fqbn]
        return self.__exec(args)

    def board_list(self, timeout=None):
        args = [Arduino.COMMAND_BOARD, Arduino.COMMAND_LIST]
        if timeout is not None:
            args.extend([Arduino.FLAG_TIMEOUT, timeout])
        return self.__exec(args)

    def board_listall(self, boardname=None):
        args = [Arduino.COMMAND_BOARD, Arduino.COMMAND_LISTALL]
        if boardname is not None:
            args.append(boardname)
        return self.__exec(args)

    def compile(self,
                sketch, build_cache_path=None, build_path=None, build_properties=None, fqbn=None, output=None,
                preprocess=None, show_properties=None, vid_pid=None, warnings=None):
        args = [Arduino.COMMAND_COMPILE]
        if build_cache_path is not None:
            args.extend([Arduino.FLAG_BUILD_CACHE_PATH, build_cache_path])
        if build_path is not None:
            args.extend([Arduino.FLAG_BUILD_PATH, build_path])
        if build_properties is not None:
            args.extend([Arduino.FLAG_BUILD_PROPERTIES, build_properties])
        if fqbn is not None:
            args.extend([Arduino.FLAG_FQBN, fqbn])
        if output is not None:
            args.extend([Arduino.FLAG_OUTPUT, output])
        if preprocess is not None and preprocess is True:
            args.append(Arduino.FLAG_PREPROCESS)
        if show_properties is not None and show_properties is True:
            args.append(Arduino.FLAG_SHOW_PROPERTIES)
        if vid_pid is not None:
            args.extend([Arduino.FLAG_VID_PID, vid_pid])
        if warnings is not None:
            args.extend([Arduino.FLAG_WARNINGS, warnings])
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

    def core_list(self, updatable=None):
        args = [Arduino.COMMAND_CORE, Arduino.COMMAND_LIST]
        if updatable is not None and updatable is True:
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

    def lib_list(self, all=None, updatable=None):
        args = [Arduino.COMMAND_LIB, Arduino.COMMAND_LIST]
        if all is not None and all is True:
            args.append(Arduino.FLAG_ALL)
        if updatable is not None and updatable is True:
            args.append(Arduino.FLAG_UPDATABLE)
        return self.__exec(args)

    def lib_search(self, *name):
        args = [Arduino.COMMAND_LIB, Arduino.COMMAND_SEARCH]
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

    def upload(self, sketch, fqbn=None, input=None, port=None, verify=None):
        args = [Arduino.COMMAND_UPLOAD]
        if fqbn is not None:
            args.extend([Arduino.FLAG_FQBN, fqbn])
        if input is not None:
            args.extend([Arduino.FLAG_INPUT, input])
        if port is not None:
            args.extend([Arduino.FLAG_PORT, port])
        if verify is not None and verify is True:
            args.append(Arduino.FLAG_VERIFY)
        args.append(sketch)
        return self.__exec(args)

    def version(self):
        return self.__exec([Arduino.COMMAND_VERSION])
