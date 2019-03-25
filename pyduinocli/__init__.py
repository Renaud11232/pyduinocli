from subprocess import Popen, PIPE
import json
import regex


class ArduinoError(Exception):

    def __init__(self, message, cause=None, stderr=None):
        self.message = message
        self.cause = cause
        self.stderr = stderr


class Arduino:

    __FORMAT_JSON = 'json'

    __FLAG_FORMAT = '--format'
    __FLAG_CONFIG_FILE = '--config-file'
    __FLAG_FLAVOUR = '--flavour'
    __FLAG_TIMEOUT = '--timeout'
    __FLAG_BUILD_CACHE_PATH = '--build-cache-path'
    __FLAG_BUILD_PATH = '--build-path'
    __FLAG_BUILD_PROPERTIES = '--build-properties'
    __FLAG_FQBN = '--fqbn'
    __FLAG_OUTPUT = '--ouput'
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
    __COMMAND_LIB = 'lib'
    __COMMAND_SKETCH = 'sketch'
    __COMMAND_NEW = 'new'
    __COMMAND_UPLOAD = 'upload'
    __COMMAND_VERSION = 'version'

    __OUTPUT_ENCODING = 'utf-8'

    __REGEX_JSON = r'\{(?:[^{}]|(?R))*\}'

    __ERROR_MESSAGE = "Message"
    __ERROR_CAUSE = "Cause"
    __ERROR_OSERROR = "'%s' does not exist or is not an executable"
    __ERROR_PORT_FQBN_SET = 'port and fqbn cannot both be set'
    __ERROR_PORT_FQBN_NOT_SET = 'port or fqbn must be set'

    def __init__(self, cli_path, config_file=None):
        self.__command_base = [cli_path, Arduino.__FLAG_FORMAT, Arduino.__FORMAT_JSON]
        if config_file is not None:
            self.__command_base.extend([Arduino.__FLAG_CONFIG_FILE, config_file])

    @staticmethod
    def __parse_output(data):
        pattern = regex.compile(Arduino.__REGEX_JSON)
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
            decoded_out = self.__parse_output(stdout.decode(Arduino.__OUTPUT_ENCODING))
            decoded_err = stderr.decode(Arduino.__OUTPUT_ENCODING)
            if p.returncode != 0:
                if type(decoded_out) is dict:
                    raise ArduinoError(decoded_out[Arduino.__ERROR_MESSAGE],
                                       decoded_out[Arduino.__ERROR_CAUSE],
                                       decoded_err)
                raise ArduinoError(decoded_out,
                                   None,
                                   decoded_err)
            return decoded_out
        except OSError:
            raise ArduinoError(Arduino.__ERROR_OSERROR % self.__command_base[0])

    def board_attach(self, port=None, fqbn=None, sketch_path=None, flavour=None, timeout=None):
        args = [Arduino.__COMMAND_BOARD, Arduino.__COMMAND_ATTACH]
        if port is not None and fqbn is not None:
            raise ArduinoError(Arduino.__ERROR_PORT_FQBN_SET)
        if port is None and fqbn is None:
            raise ArduinoError(Arduino.__ERROR_PORT_FQBN_NOT_SET)
        if port is not None:
            args.append(port)
        if fqbn is not None:
            args.append(fqbn)
        if sketch_path is not None:
            args.append(sketch_path)
        if flavour is not None:
            args.extend([Arduino.__FLAG_FLAVOUR, flavour])
        if timeout is not None:
            args.extend([Arduino.__FLAG_TIMEOUT, timeout])
        return self.__exec(args)

    def board_details(self, fqbn):
        args = [Arduino.__COMMAND_BOARD, Arduino.__COMMAND_DETAILS, fqbn]
        return self.__exec(args)

    def board_list(self, timeout=None):
        args = [Arduino.__COMMAND_BOARD, Arduino.__COMMAND_LIST]
        if timeout is not None:
            args.extend([Arduino.__FLAG_TIMEOUT, timeout])
        return self.__exec(args)

    def board_listall(self, boardname=None):
        args = [Arduino.__COMMAND_BOARD, Arduino.__COMMAND_LISTALL]
        if boardname is not None:
            args.append(boardname)
        return self.__exec(args)

    def compile(self,
                sketch, build_cache_path=None, build_path=None, build_properties=None, fqbn=None, output=None,
                preprocess=None, show_properties=None, vid_pid=None, warnings=None):
        args = [Arduino.__COMMAND_COMPILE]
        if build_cache_path is not None:
            args.extend([Arduino.__FLAG_BUILD_CACHE_PATH, build_cache_path])
        if build_path is not None:
            args.extend([Arduino.__FLAG_BUILD_PATH, build_path])
        if build_properties is not None:
            args.extend([Arduino.__FLAG_BUILD_PROPERTIES, build_properties])
        if fqbn is not None:
            args.extend([Arduino.__FLAG_FQBN, fqbn])
        if output is not None:
            args.extend([Arduino.__FLAG_OUTPUT, output])
        if preprocess is not None and preprocess is True:
            args.append(Arduino.__FLAG_PREPROCESS)
        if show_properties is not None and show_properties is True:
            args.append(Arduino.__FLAG_SHOW_PROPERTIES)
        if vid_pid is not None:
            args.extend([Arduino.__FLAG_VID_PID, vid_pid])
        if warnings is not None:
            args.extend([Arduino.__FLAG_WARNINGS, warnings])
        args.append(sketch)
        return self.__exec(args)

    def config_dump(self):
        return self.__exec([Arduino.__COMMAND_CONFIG, Arduino.__COMMAND_DUMP])

    def config_init(self, save_as=None):
        args = [Arduino.__COMMAND_CONFIG, Arduino.__COMMAND_INIT, Arduino.__FLAG_DEFAULT]
        if save_as is not None:
            args.extend([Arduino.__FLAG_SAVE_AS, save_as])
        return self.__exec(args)

    def core_download(self, *downloads):
        args = [Arduino.__COMMAND_CORE, Arduino.__COMMAND_DOWNLOAD]
        args.extend(downloads)
        return self.__exec(args)

    def core_install(self, *installs):
        args = [Arduino.__COMMAND_CORE, Arduino.__COMMAND_INSTALL]
        args.extend(installs)
        return self.__exec(args)

    def core_list(self, updatable=None):
        args = [Arduino.__COMMAND_CORE, Arduino.__COMMAND_LIST]
        if updatable is not None and updatable is True:
            args.append(Arduino.__FLAG_UPDATABLE)
        return self.__exec(args)

    def core_search(self, *keywords):
        args = [Arduino.__COMMAND_CORE, Arduino.__COMMAND_SEARCH]
        args.extend(keywords)
        return self.__exec(args)

    def core_uninstall(self, *installs):
        args = [Arduino.__COMMAND_CORE, Arduino.__COMMAND_UNINSTALL]
        args.extend(installs)
        return self.__exec(args)

    def core_update_index(self):
        return self.__exec([Arduino.__COMMAND_CORE, Arduino.__COMMAND_UPDATE_INDEX])

    def core_upgrade(self, *upgrades):
        args = [Arduino.__COMMAND_CORE, Arduino.__COMMAND_UPGRADE]
        args.extend(upgrades)
        return self.__exec(args)

    def lib_download(self, *downloads):
        args = [Arduino.__COMMAND_LIB, Arduino.__COMMAND_DOWNLOAD]
        args.extend(downloads)
        return self.__exec(args)

    def lib_install(self, *installs):
        args = [Arduino.__COMMAND_LIB, Arduino.__COMMAND_INSTALL]
        args.extend(installs)
        return self.__exec(args)

    def lib_list(self, all=None, updatable=None):
        args = [Arduino.__COMMAND_LIB, Arduino.__COMMAND_LIST]
        if all is not None and all is True:
            args.append(Arduino.__FLAG_ALL)
        if updatable is not None and updatable is True:
            args.append(Arduino.__FLAG_UPDATABLE)
        return self.__exec(args)

    def lib_search(self, *name):
        args = [Arduino.__COMMAND_LIB, Arduino.__COMMAND_SEARCH]
        args.extend(name)
        return self.__exec(args)

    def lib_uninstall(self, *uninstalls):
        args = [Arduino.__COMMAND_LIB, Arduino.__COMMAND_UNINSTALL]
        args.extend(uninstalls)
        return self.__exec(args)

    def lib_update_index(self):
        return self.__exec([Arduino.__COMMAND_LIB, Arduino.__COMMAND_UPDATE_INDEX])

    def lib_upgrade(self):
        return self.__exec([Arduino.__COMMAND_LIB, Arduino.__COMMAND_UPGRADE])

    def sketch_new(self, name):
        return self.__exec([Arduino.__COMMAND_SKETCH, Arduino.__COMMAND_NEW, name])

    def upload(self, sketch, fqbn=None, input=None, port=None, verify=None):
        args = [Arduino.__COMMAND_UPLOAD]
        if fqbn is not None:
            args.extend([Arduino.__FLAG_FQBN, fqbn])
        if input is not None:
            args.extend([Arduino.__FLAG_INPUT, input])
        if port is not None:
            args.extend([Arduino.__FLAG_PORT, port])
        if verify is not None and verify is True:
            args.append(Arduino.__FLAG_VERIFY)
        args.append(sketch)
        return self.__exec(args)

    def version(self):
        return self.__exec([Arduino.__COMMAND_VERSION])
