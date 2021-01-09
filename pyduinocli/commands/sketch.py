from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands
from pyduinocli.constants import flags


class SketchCommand(CommandBase):

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.SKETCH)

    def new(self, name):
        return self._exec([commands.NEW, CommandBase._strip_arg(name)])

    def archive(self, sketch_path=".", archive_path=None, include_build_dir=None):
        args = [commands.ARCHIVE, CommandBase._strip_arg(sketch_path)]
        if archive_path is not None:
            args.append(CommandBase._strip_arg(archive_path))
        if include_build_dir is True:
            args.append(flags.INCLUDE_BUILD_DIR)
        return self._exec(args)
