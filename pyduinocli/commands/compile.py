from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands
from pyduinocli.constants import flags


class CompileCommand(CommandBase):

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.COMPILE)

    def __call__(self,
                 sketch, build_cache_path=None, build_path=None, build_properties=None, fqbn=None, output=None,
                 port=None, preprocess=None, show_properties=None, upload=None, verify=None, vid_pid=None,
                 warnings=None):
        args = [commands.COMPILE]
        if build_cache_path is not None:
            args.extend([flags.BUILD_CACHE_PATH, CommandBase._strip_arg(build_cache_path)])
        if build_path is not None:
            args.extend([flags.BUILD_PATH, CommandBase._strip_arg(build_path)])
        if build_properties is not None:
            args.extend([flags.BUILD_PROPERTIES, CommandBase._strip_arg(build_properties)])
        if fqbn is not None:
            args.extend([flags.FQBN, CommandBase._strip_arg(fqbn)])
        if output is not None:
            args.extend([flags.OUTPUT, CommandBase._strip_arg(output)])
        if port is not None:
            args.extend([flags.PORT, CommandBase._strip_arg(port)])
        if preprocess is True:
            args.append(flags.PREPROCESS)
        if show_properties is True:
            args.append(flags.SHOW_PROPERTIES)
        if upload is True:
            args.append(flags.UPLOAD)
        if verify is True:
            args.append(flags.VERIFY)
        if vid_pid is not None:
            args.extend([flags.VID_PID, CommandBase._strip_arg(vid_pid)])
        if warnings is not None:
            args.extend([flags.WARNINGS, CommandBase._strip_arg(warnings)])
        args.append(CommandBase._strip_arg(sketch))
        return self._exec(args)
