#!/usr/bin/env python

"""
Installs tbb-4.4.6.

Usage:
    ./installTBB.py <INSTALL_DIR>
"""

import os

from buildUtils import (
    ParseInstallArgs,
    DownloadAndExtractArchive,
    ChangeDirectory,
    MakeDirectories,
    RunCommand,
    CopyFiles,
    CopyDirectory,
)


APP_NAME = 'tbb'
URL = "https://github.com/01org/tbb/archive/4.4.6.tar.gz"


def InstallTBB(context):
    # Stage source code.
    if os.path.exists(context.installPrefix):
        raise RuntimeError("{!r} installation already exists.".format(context.installPrefix))

    srcDir = DownloadAndExtractArchive(APP_NAME, URL)
    ChangeDirectory(srcDir)

    # Build from source.
    makeCmd = " ".join([
        "make",
        "-j{}".format(context.numCores),
    ])
    RunCommand(makeCmd)

    # Install by copying files.
    MakeDirectories(context.installPrefix)
    libPath = os.path.join(context.installPrefix, 'lib')
    includePath = os.path.join(context.installPrefix, 'include')
    MakeDirectories(libPath)
    MakeDirectories(includePath)

    CopyFiles("build/*_release/libtbb*.*", libPath)
    CopyFiles("build/*_debug/libtbb*.*", libPath)
    CopyDirectory("include/serial", os.path.join(includePath, "serial"))
    CopyDirectory("include/tbb", os.path.join(includePath, "tbb"))


if __name__ == "__main__":
    args = ParseInstallArgs(APP_NAME)
    InstallTBB(args)

