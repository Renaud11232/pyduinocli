from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands
from pyduinocli.constants import flags


class CompileCommand(CommandBase):

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.COMPILE)

    def __call__(self,
                 sketch, build_cache_path=None, build_path=None, build_properties=None, fqbn=None, output_dir=None,
                 port=None, preprocess=None, show_properties=None, upload=None, verify=None, vid_pid=None,
                 warnings=None, libraries=None, optimize_for_debug=None, export_binaries=None, programmer=None,
                 clean=None, only_compilation_database=None):
        args = []
        if build_cache_path:
            args.extend([flags.BUILD_CACHE_PATH, CommandBase._strip_arg(build_cache_path)])
        if build_path:
            args.extend([flags.BUILD_PATH, CommandBase._strip_arg(build_path)])
        if build_properties:
            for build_property in build_properties:
                args.extend([flags.BUILD_PROPERTY, CommandBase._strip_arg(build_property)])
        if fqbn:
            args.extend([flags.FQBN, CommandBase._strip_arg(fqbn)])
        if output_dir:
            args.extend([flags.OUTPUT_DIR, CommandBase._strip_arg(output_dir)])
        if port:
            args.extend([flags.PORT, CommandBase._strip_arg(port)])
        if preprocess is True:
            args.append(flags.PREPROCESS)
        if show_properties is True:
            args.append(flags.SHOW_PROPERTIES)
        if upload is True:
            args.append(flags.UPLOAD)
        if verify is True:
            args.append(flags.VERIFY)
        if vid_pid:
            args.extend([flags.VID_PID, CommandBase._strip_arg(vid_pid)])
        if warnings:
            args.extend([flags.WARNINGS, CommandBase._strip_arg(warnings)])
        if libraries:
            for library in libraries:
                args.extend([flags.LIBRARIES, CommandBase._strip_arg(library)])
        if optimize_for_debug is True:
            args.append(flags.OPTIMIZE_FOR_DEBUG)
        if export_binaries is True:
            args.append(flags.EXPORT_BINARIES)
        if programmer:
            args.extend([flags.PROGRAMMER, CommandBase._strip_arg(programmer)])
        if clean is True:
            args.append(flags.CLEAN)
        if only_compilation_database is True:
            args.append(flags.ONLY_COMPILATION_DATABASE)
        args.append(CommandBase._strip_arg(sketch))
        return self._exec(args)
