from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands


class SketchCommand(CommandBase):

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.SKETCH)

    def new(self, name):
        return self._exec([commands.NEW, CommandBase._strip_arg(name)])
