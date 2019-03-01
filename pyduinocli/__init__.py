from subprocess import Popen, PIPE
import json


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
    COMMAND_VERSION = 'version'

    def __init__(self, cli_path, config_file=None):
        self.__command_base = [cli_path, Arduino.FLAG_FORMAT, 'json']
        if config_file is not None:
            self.__command_base.extend([Arduino.FLAG_CONFIG_FILE, config_file])

    # TODO better error handling
    def __exec(self, *args):
        command = self.__command_base
        command.extend(args)
        p = Popen(command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate()
        if p.returncode != 0:
            raise RuntimeError('stderr : %s, stdout: %s' % (stderr, stdout))
        return json.loads(stdout)

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
        args = [Arduino.COMMAND_CONFIG, Arduino.COMMAND_DUMP]
        return self.__exec(args)

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

    def core_list(self):
        return self.__exec(Arduino.COMMAND_CORE, Arduino.COMMAND_LIST)

    def core_search(self, *keywords):
        args = [Arduino.COMMAND_CORE, Arduino.COMMAND_SEARCH]
        args.extend(keywords)
        return self.__exec(args)

    def core_uninstall(self, *installs):
        args = [Arduino.COMMAND_CORE, Arduino.COMMAND_UNINSTALL]
        args.extend(installs)
        return self.__exec(args)

    def core_update_index(self):
        pass

    def core_upgrade(self):
        pass

    def lib_download(self):
        pass

    def lib_install(self):
        pass

    def lib_list(self):
        pass

    def lib_search(self):
        pass

    def lib_uninstall(self):
        pass

    def lib_update_index(self):
        pass

    def lib_upgrade(self):
        pass

    def sketch_new(self):
        pass

    def upload(self):
        pass

    def version(self):
        return self.__exec(Arduino.COMMAND_VERSION)
