# -*- coding: utf-8 -*-
import os

SEP = '->'

# Version control
GIT = 'git'
HG = 'hg'
GIT_ALIASES = ('git')
HG_ALIASES = ('hg', 'mercurial')
SUPPORTED_VERSION_CONTROL = (GIT, HG)
DEFAULT_VERSION_CONTROL = HG
IGNORE_FILES = {
    GIT: '.gitignore',
    HG: '.hgignore',
}

# Ignore file formats
GLOB = 'glob'
REGEXP = 'regexp'
SUPPORTED_REGEX_FORMAT = (GLOB, REGEXP)
DEFAULT_REGEX_FORMAT = REGEXP

# File extensions to ignore
EXT_OS = ('DS_Store',)
EXT_CORE_TEX = (
    'aux', 'cb', 'cb2', 'fls', 'fmt', 'fot', 'lof', 'log', 'lot', 'out', 'toc',
)
EXT_BIB = ('bbl', 'bcf', 'blg', 'blx.aux', 'blx.bib', 'run.xml')
EXT_BUILD_TOOL = (
    'fdb_latexmk', 'pdfsync', 'synctex(busy)', 'synctex.gz',
    'synctex.gz(busy)',
)
EXT_TO_IGNORE = EXT_OS + EXT_CORE_TEX + EXT_BIB + EXT_BUILD_TOOL


class IgnoreFormatter:
    def __init__(self, regex_format):
        if regex_format not in SUPPORTED_REGEX_FORMAT:
            regex_format = DEFAULT_REGEX_FORMAT
        self.regex_format = regex_format

    def lines(self):
        method = 'lines_{}'.format(self.regex_format)
        return getattr(self, method)()

    def lines_regexp(self):
        lines = list()
        for file_extension in VersionControlIgnoreFileWriter.get_ignore_list():
            lines.append('.*\.{ext}$'.format(ext=file_extension))
        return lines

    def lines_glob(self):
        lines = list()
        for file_extension in VersionControlIgnoreFileWriter.get_ignore_list():
            lines.append('*.{ext}'.format(ext=file_extension))
        return lines


class VersionControlIgnoreFileWriter:
    def __init__(self, version_control_system=None, regex_format=None):
        if version_control_system not in SUPPORTED_VERSION_CONTROL:
            version_control_system = DEFAULT_VERSION_CONTROL
        self.version_control_system = version_control_system
        self.regex_formatter = IgnoreFormatter(regex_format)

    @staticmethod
    def get_ignore_list():
        return set(EXT_TO_IGNORE)

    def get_path(self):
        package_dir = os.path.realpath(os.path.curdir)
        return os.path.join(
            package_dir, IGNORE_FILES[self.version_control_system]
        )

    @staticmethod
    def get_versioning_args():
        version_ctrl = '{{cookiecutter.version_control}}'.lower()
        args = list()
        for versioning_system in SUPPORTED_VERSION_CONTROL:
            ALIASES_VAR = '{}_ALIASES'.format(versioning_system.upper())
            if (True in [
                version_ctrl.startswith(alias)
                for alias in globals()[ALIASES_VAR]
            ]):
                args.append(versioning_system)
                params = version_ctrl.split(SEP)
                if len(params) > 1:
                    args.append(params[-1])
                break
        return args

    def write_ignore_file(self):
        lines_to_write = self.regex_formatter.lines()
        with open(self.get_path(), 'w+') as file_handler:
            regex_format = self.regex_formatter.regex_format
            if self.version_control_system == HG and regex_format != REGEXP:
                file_handler.write("syntax: {}\n".format(regex_format))
            for line in sorted(lines_to_write):
                file_handler.write("{}\n".format(line))


if __name__ == '__main__':
    ignore_file_writer = VersionControlIgnoreFileWriter(
        *VersionControlIgnoreFileWriter.get_versioning_args()
    )
    ignore_file_writer.write_ignore_file()
