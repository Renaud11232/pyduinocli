from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands
from pyduinocli.constants import flags


class SketchCommand(CommandBase):
    """
    This class wraps the call to the :code:`sketch` command of :code:`arduino-cli`.
    """

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.SKETCH)

    def new(self, name):
        """
        Calls the :code:`sketch new` command

        :param name: The name of the sketch to create
        :type name: str
        :return: The created path
        :rtype: str or dict
        """
        return self._exec([commands.NEW, CommandBase._strip_arg(name)])

    def archive(self, sketch_path=".", archive_path=None, include_build_dir=None):
        """
        Calls the :code:`sketch archive` command

        :param sketch_path: The path to the sketch to archive
        :type sketch_path: str
        :param archive_path: The path of the output archive
        :type archive_path: str or NoneType
        :param include_build_dir: Includes the build directory in the archive
        :type include_build_dir: bool or NoneType
        :return: Nothing (an empty string)
        :rtype: str
        """
        args = [commands.ARCHIVE, CommandBase._strip_arg(sketch_path)]
        if archive_path is not None:
            args.append(CommandBase._strip_arg(archive_path))
        if include_build_dir is True:
            args.append(flags.INCLUDE_BUILD_DIR)
        return self._exec(args)
