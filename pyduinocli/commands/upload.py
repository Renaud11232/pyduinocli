from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands
from pyduinocli.constants import flags


class UploadCommand(CommandBase):
    """
    This class wraps the call to the :code:`upload` command of :code:`arduino-cli`.
    """

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.UPLOAD)

    def __call__(self, sketch=None, fqbn=None, input_dir=None, input_file=None, port=None, verify=None, programmer=None,
                 discovery_timeout=None, protocol=None):
        """
        Calls the :code:`upload` command

        :param sketch: The sketch to upload, cap be the full path or just the name
        :type sketch: str or NoneType
        :param fqbn: The fully qualified board name of the target board
        :type fqbn: str or NoneType
        :param input_dir: A path containing the binaries to upload
        :type input_dir: str or NoneType
        :param input_file: A path to the binary file to upload
        :type input_file: str or NoneType
        :param port: The upload port e.g.: COM10 or /dev/ttyACM0
        :type port: str or NoneType
        :param verify: Verify the uploaded binary after the upload
        :type verify: bool or NoneType
        :param programmer: Programmer to use for the upload process
        :type programmer: str or NoneType
        :param discovery_timeout: Max time to wait for port discovery, e.g.: 30s, 1m (default 5s)
        :type discovery_timeout: str or NoneType
        :param protocol: Upload port protocol, e.g: serial
        :type protocol: str or NoneType
        :return: The output of the related command
        :rtype: dict
        """
        args = []
        if fqbn:
            args.extend([flags.FQBN, CommandBase._strip_arg(fqbn)])
        if input_dir:
            args.extend([flags.INPUT_DIR, CommandBase._strip_arg(input_dir)])
        if input_file:
            args.extend([flags.INPUT_FILE, CommandBase._strip_arg(input_file)])
        if port:
            args.extend([flags.PORT, CommandBase._strip_arg(port)])
        if verify is True:
            args.append(flags.VERIFY)
        if sketch:
            args.append(CommandBase._strip_arg(sketch))
        if programmer:
            args.extend([flags.PROGRAMMER, CommandBase._strip_arg(programmer)])
        if discovery_timeout:
            args.extend([flags.DISCOVERY_TIMEOUT, CommandBase._strip_arg(discovery_timeout)])
        if protocol:
            args.extend([flags.PROTOCOL, CommandBase._strip_arg(protocol)])
        return self._exec(args)
