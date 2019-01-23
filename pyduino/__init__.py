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

    def version(self):
        return json.loads(self.__exec("version"))
