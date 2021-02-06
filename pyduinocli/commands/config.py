from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands
from pyduinocli.constants import flags


class ConfigCommand(CommandBase):
    """
    This class wraps the call to the :code:`config` command of :code:`arduino-cli`.
    """

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.CONFIG)

    def dump(self):
        """
        Calls the :code:`config dump` command

        :return: The dumped config
        :rtype: str
        """
        return self._exec([commands.DUMP])

    def init(self, dest_dir=None, dest_file=None, overwrite=None):
        """
        Calls the :code:`config init` command

        :param dest_dir: The directory where to save the file
        :type dest_dir: str or NoneType
        :param dest_file: A path where the file will be saved
        :type dest_file: str or NoneType
        :param overwrite: Overwrites an existing file
        :type overwrite: bool or NoneType
        :return: The created file
        :rtype: str or dict
        """
        args = [commands.INIT]
        if dest_dir:
            args.extend([flags.DEST_DIR, CommandBase._strip_arg(dest_dir)])
        if dest_file:
            args.extend([flags.DEST_FILE, CommandBase._strip_arg(dest_file)])
        if overwrite is True:
            args.append(flags.OVERWRITE)
        return self._exec(args)

    def add(self, setting_name, values):
        """
        Calls the :code:`config add` command

        :param setting_name: The name of the setting to add
        :type setting_name: str
        :param values: The values to add to the setting
        :type values: list
        """
        args = [commands.ADD, CommandBase._strip_arg(setting_name)]
        args.extend(CommandBase._strip_args(values))
        return self._exec(args)

    def delete(self, setting_name):
        """
        Calls the :code:`config delete` command

        :param setting_name: The name of the setting to delete
        :type setting_name: str
        """
        return self._exec([commands.DELETE, CommandBase._strip_arg(setting_name)])

    def remove(self, setting_name, values):
        """
        Calls the :code:`config remove` command

        :param setting_name: The name of the setting from which values will be removed
        :type setting_name: str
        :param values: The list of values to remove
        :type values: list
        """
        args = [commands.REMOVE, CommandBase._strip_arg(setting_name)]
        args.extend(CommandBase._strip_args(values))
        return self._exec(args)

    def set(self, setting_name, values):
        """
        Calls the :code:`config set` command

        :param setting_name: The name of the setting to set
        :type setting_name: str
        :param values: The list of values to set
        :type values: list
        """
        args = [commands.SET, CommandBase._strip_arg(setting_name)]
        args.extend(CommandBase._strip_args(values))
        return self._exec(args)
