from subprocess import Popen, PIPE
import json


class Arduino:

    KWARG_FLAVOUR = 'flavour'
    KWARG_TIMEOUT = 'timeout'

    FLAG_FORMAT = '--format'
    FLAG_FLAVOUR = '--flavour'
    FLAG_TIMEOUT = '--timeout'

    COMMAND_BOARD = 'board'
    COMMAND_ATTACH = 'attach'
    COMMAND_DETAILS = 'details'
    COMMAND_LIST = 'list'
    COMMAND_VERSION = 'version'

    def __init__(self, cli_path):
        self.cli_path = cli_path

    def __exec(self, *args):
        command = [self.cli_path, Arduino.FLAG_FORMAT, 'json']
        command.extend(args)
        p = Popen(command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate()
        if p.returncode != 0:
            raise RuntimeError(stderr)
        return json.loads(stdout)

    def board_attach(self, port_fqbn, sketch_path=None, **kwargs):
        args = [Arduino.COMMAND_BOARD, Arduino.COMMAND_ATTACH, port_fqbn]
        if sketch_path is not None:
            args.append(sketch_path)
        if Arduino.KWARG_FLAVOUR in kwargs:
            args.append(Arduino.FLAG_FLAVOUR)
            args.append(kwargs.get(Arduino.KWARG_FLAVOUR))
        if Arduino.KWARG_TIMEOUT in kwargs:
            args.append(Arduino.FLAG_TIMEOUT)
            args.append(kwargs.get(Arduino.KWARG_TIMEOUT))
        return self.__exec(args)

    def board_details(self, fqbn):
        args = [Arduino.COMMAND_BOARD, Arduino.COMMAND_DETAILS, fqbn]
        return self.__exec(args)

    def board_list(self, **kwargs):
        args = [Arduino.COMMAND_BOARD, Arduino.COMMAND_LIST]
        if Arduino.KWARG_TIMEOUT in kwargs:
            args.append(Arduino.FLAG_TIMEOUT)
            args.append(kwargs.get(Arduino.KWARG_TIMEOUT))
        return self.__exec(args)

    def board_listall(self):
        pass

    def compile(self):
        pass

    def config_dump(self):
        pass

    def config_init(self):
        pass

    def core_download(self):
        pass

    def core_install(self):
        pass

    def core_list(self):
        pass

    def core_search(self):
        pass

    def core_uninstall(self):
        pass

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
