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

    def new(self, name, overwrite=None):
        """
        Calls the :code:`sketch new` command

        :param name: The name of the sketch to create
        :type name: str
        :param overwrite: Overwrites an existing .ino sketch.
        :type overwrite: bool or NoneType
        :return: The output of the related command
        :rtype: dict
        """
        args = [commands.NEW, CommandBase._strip_arg(name)]
        if overwrite is True:
            args.append(flags.OVERWRITE)
        return self._exec(args)

    def archive(self, sketch_path=".", archive_path=None, include_build_dir=None, overwrite=None):
        """
        Calls the :code:`sketch archive` command

        :param sketch_path: The path to the sketch to archive
        :type sketch_path: str
        :param archive_path: The path of the output archive
        :type archive_path: str or NoneType
        :param include_build_dir: Includes the build directory in the archive
        :type include_build_dir: bool or NoneType
        :param overwrite: Overwrites an already existing archive
        :type overwrite: bool or NoneType
        :return: The output of the related command
        :rtype: dict
        """
        args = [commands.ARCHIVE, CommandBase._strip_arg(sketch_path)]
        if archive_path is not None:
            args.append(CommandBase._strip_arg(archive_path))
        if include_build_dir is True:
            args.append(flags.INCLUDE_BUILD_DIR)
        if overwrite is True:
            args.append(flags.OVERWRITE)
        return self._exec(args)
