from subprocess import Popen, PIPE
import json


class Arduino:

    def __init__(self, cli_path):
        self.cli_path = cli_path

    def __exec(self, *args):
        command = [self.cli_path, '--format', 'json']
        command.extend(args)
        p = Popen(command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate()
        if p.returncode != 0:
            raise RuntimeError(stderr)
        return stdout

    def board_attach(self):
        pass

    def board_details(self):
        pass

    def board_list(self):
        pass

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
        return json.loads(self.__exec("version"))
