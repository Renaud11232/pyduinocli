from pyduinocli.commands.arduino import ArduinoCliCommand as Arduino
from pyduinocli.errors import ArduinoError

class ArduinoOld(pyduinocli.commands.Command):




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
