from pyduinocli.commands.base import CommandBase
from pyduinocli.constants import commands
from pyduinocli.constants import flags


class CompileCommand(CommandBase):
    """
    This class wraps the call to the :code:`compile` command of :code:`arduino-cli`.
    """

    def __init__(self, base_args):
        CommandBase.__init__(self, base_args)
        self._base_args.append(commands.COMPILE)

    def __call__(self,
                 sketch, build_cache_path=None, build_path=None, build_properties=None, fqbn=None, output_dir=None,
                 port=None, preprocess=None, show_properties=None, upload=None, verify=None, vid_pid=None,
                 warnings=None, libraries=None, optimize_for_debug=None, export_binaries=None, programmer=None,
                 clean=None, only_compilation_database=None):
        """
        Calls the :code:`compile` command

        :param sketch: The sketch to compile, can also be a path to a sketch
        :type sketch: str
        :param build_cache_path: Builds of 'core.a' are saved into this path to be cached and reused.
        :type build_cache_path: str or NoneType
        :param build_path: Path where to save compiled files. If omitted, a directory will be created in the default temporary path of your OS.
        :type build_path: str or NoneType
        :param build_properties: Override build properties with custom values.
        :type build_properties: list or NoneType
        :param fqbn: Fully Qualified Board Name, e.g.: arduino:avr:uno
        :type fqbn: str or NoneType
        :param output_dir: Save build artifacts in this directory.
        :type output_dir: str or NoneType
        :param port: Upload port, e.g.: COM10 or /dev/ttyACM0
        :type port: str or NoneType
        :param preprocess: Print preprocessed code to stdout instead of compiling.
        :type preprocess: bool or NoneType
        :param show_properties: Show all build properties used instead of compiling.
        :type show_properties: bool or NoneType
        :param upload: Upload the binary after the compilation.
        :type upload: bool or NoneType
        :param verify: Verify uploaded binary after the upload.
        :type verify: bool or NoneType
        :param vid_pid: When specified, VID/PID specific build properties are used, if board supports them.
        :type vid_pid: str or NoneType
        :param warnings: Optional, can be "none", "default", "more" and "all". Defaults to "none". Used to tell gcc which warning level to use (-W flag). (default "none")
        :type warnings: str or NoneType
        :param libraries: List of custom libraries paths
        :type libraries: list or NoneType
        :param optimize_for_debug: Optional, optimize compile output for debugging, rather than for release.
        :type optimize_for_debug: bool or NoneType
        :param export_binaries: If set built binaries will be exported to the sketch folder.
        :type export_binaries: bool or NoneType
        :param programmer: Optional, use the specified programmer to upload.
        :type programmer: str or NoneType
        :param clean: Optional, cleanup the build folder and do not use any cached build.
        :type clean: bool or NoneType
        :param only_compilation_database: Just produce the compilation database, without actually compiling.
        :type only_compilation_database: bool or NoneType
        :return: The output of the command
        :rtype: str or dict
        """
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
