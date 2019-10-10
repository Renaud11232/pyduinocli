from pyduinocli.commands.arduino import ArduinoCliCommand as Arduino
from pyduinocli.errors import ArduinoError

class ArduinoOld(pyduinocli.commands.Command):



    def compile(self,
                sketch, build_cache_path=None, build_path=None, build_properties=None, fqbn=None, output=None,
                port=None, preprocess=None, show_properties=None, upload=None, verify=None, vid_pid=None, warnings=None):
        args = [pyduinocli.constants.commands.COMPILE]
        if build_cache_path is not None:
            args.extend([pyduinocli.constants.flags.BUILD_CACHE_PATH, Arduino.__strip_arg(build_cache_path)])
        if build_path is not None:
            args.extend([pyduinocli.constants.flags.BUILD_PATH, Arduino.__strip_arg(build_path)])
        if build_properties is not None:
            args.extend([pyduinocli.constants.flags.BUILD_PROPERTIES, Arduino.__strip_arg(build_properties)])
        if fqbn is not None:
            args.extend([pyduinocli.constants.flags.FQBN, Arduino.__strip_arg(fqbn)])
        if output is not None:
            args.extend([pyduinocli.constants.flags.OUTPUT, Arduino.__strip_arg(output)])
        if port is not None:
            args.extend([pyduinocli.constants.flags.PORT, Arduino.__strip_arg(port)])
        if preprocess is True:
            args.append(pyduinocli.constants.flags.PREPROCESS)
        if show_properties is True:
            args.append(pyduinocli.constants.flags.SHOW_PROPERTIES)
        if upload is True:
            args.append(pyduinocli.constants.flags.UPLOAD)
        if verify is True:
            args.append(pyduinocli.constants.flags.VERIFY)
        if vid_pid is not None:
            args.extend([pyduinocli.constants.flags.VID_PID, Arduino.__strip_arg(vid_pid)])
        if warnings is not None:
            args.extend([pyduinocli.constants.flags.WARNINGS, Arduino.__strip_arg(warnings)])
        args.append(Arduino.__strip_arg(sketch))
        return self.__exec(args)

    def config_dump(self):
        return self.__exec([pyduinocli.constants.commands.CONFIG, pyduinocli.constants.commands.DUMP])

    def config_init(self, save_as=None):
        args = [pyduinocli.constants.commands.CONFIG, pyduinocli.constants.commands.INIT, pyduinocli.constants.flags.DEFAULT]
        if save_as is not None:
            args.extend([pyduinocli.constants.flags.SAVE_AS, Arduino.__strip_arg(save_as)])
        return self.__exec(args)

    def core_download(self, downloads):
        args = [pyduinocli.constants.commands.CORE, pyduinocli.constants.commands.DOWNLOAD]
        args.extend(Arduino.__strip_args(downloads))
        return self.__exec(args)

    def core_install(self, installs):
        args = [pyduinocli.constants.commands.CORE, pyduinocli.constants.commands.INSTALL]
        args.extend(Arduino.__strip_args(installs))
        return self.__exec(args)

    def core_list(self, updatable=None):
        args = [pyduinocli.constants.commands.CORE, pyduinocli.constants.commands.LIST]
        if updatable is True:
            args.append(pyduinocli.constants.flags.UPDATABLE)
        return self.__exec(args)

    def core_search(self, keywords):
        args = [pyduinocli.constants.commands.CORE, pyduinocli.constants.commands.SEARCH]
        args.extend(Arduino.__strip_args(keywords))
        return self.__exec(args)

    def core_uninstall(self, installs):
        args = [pyduinocli.constants.commands.CORE, pyduinocli.constants.commands.UNINSTALL]
        args.extend(Arduino.__strip_args(installs))
        return self.__exec(args)

    def core_update_index(self):
        return self.__exec([pyduinocli.constants.commands.CORE, pyduinocli.constants.commands.UPDATE_INDEX])

    def core_upgrade(self, upgrades=None):
        if upgrades is None:
            upgrades = []
        args = [pyduinocli.constants.commands.CORE, pyduinocli.constants.commands.UPGRADE]
        args.extend(Arduino.__strip_args(upgrades))
        return self.__exec(args)

    def daemon(self):
        args = [pyduinocli.constants.commands.DAEMON]
        return self.__exec(args)

    def lib_download(self, downloads):
        args = [pyduinocli.constants.commands.LIB, pyduinocli.constants.commands.DOWNLOAD]
        args.extend(Arduino.__strip_args(downloads))
        return self.__exec(args)

    def lib_install(self, installs):
        args = [pyduinocli.constants.commands.LIB, pyduinocli.constants.commands.INSTALL]
        args.extend(Arduino.__strip_args(installs))
        return self.__exec(args)

    def lib_list(self, all=None, updatable=None):
        args = [pyduinocli.constants.commands.LIB, pyduinocli.constants.commands.LIST]
        if all is True:
            args.append(pyduinocli.constants.flags.ALL)
        if updatable is True:
            args.append(pyduinocli.constants.flags.UPDATABLE)
        return self.__exec(args)

    def lib_search(self, name, names=None):
        args = [pyduinocli.constants.commands.LIB, pyduinocli.constants.commands.SEARCH]
        if names is True:
            args.append(pyduinocli.constants.flags.NAMES)
        args.extend(Arduino.__strip_args(name))
        return self.__exec(args)

    def lib_uninstall(self, uninstalls):
        args = [pyduinocli.constants.commands.LIB, pyduinocli.constants.commands.UNINSTALL]
        args.extend(Arduino.__strip_args(uninstalls))
        return self.__exec(args)

    def lib_update_index(self):
        return self.__exec([pyduinocli.constants.commands.LIB, pyduinocli.constants.commands.UPDATE_INDEX])

    def lib_upgrade(self, upgrades=None):
        if upgrades is None:
            upgrades = []
        args = [pyduinocli.constants.commands.LIB, pyduinocli.constants.commands.UPGRADE]
        args.extend(Arduino.__strip_args(upgrades))
        return self.__exec(args)

    def sketch_new(self, name):
        return self.__exec([pyduinocli.constants.commands.SKETCH, pyduinocli.constants.commands.NEW, Arduino.__strip_arg(name)])

    def upload(self, sketch=None, fqbn=None, input=None, port=None, verify=None):
        args = [pyduinocli.constants.commands.UPLOAD]
        if fqbn is not None:
            args.extend([pyduinocli.constants.flags.FQBN, Arduino.__strip_arg(fqbn)])
        if input is not None:
            args.extend([pyduinocli.constants.flags.INPUT, Arduino.__strip_arg(input)])
        if port is not None:
            args.extend([pyduinocli.constants.flags.PORT, Arduino.__strip_arg(port)])
        if verify is True:
            args.append(pyduinocli.constants.flags.VERIFY)
        if sketch is not None:
            args.append(Arduino.__strip_arg(sketch))
        return self.__exec(args)

    def version(self):
        return self.__exec([pyduinocli.constants.commands.VERSION])
