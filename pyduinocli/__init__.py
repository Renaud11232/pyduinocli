class Arduino:

    def __init__(self, cli_path, config_file=None, additional_urls=None, log_file=None, log_format=None, log_level=None):
        if not cli_path:
            from pyduinocli.errors import ArduinoError
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
