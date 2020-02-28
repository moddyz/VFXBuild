#!/usr/bin/env python

"""
Installs glew-2.0.0.

Usage:
    ./installGLEW.py <INSTALL_DIR>
"""

import os

from buildUtils import (
    ParseInstallArgs,
    DownloadAndExtractArchive,
    ChangeDirectory,
    MakeDirectories,
    RunCommand,
)


APP_NAME = 'glew'
URL = "https://downloads.sourceforge.net/project/glew/glew/2.0.0/glew-2.0.0.tgz"


def InstallGLEW(context):
    # Stage source code.
    if os.path.exists(context.installPrefix):
        raise RuntimeError("{!r} installation already exists.".format(context.installPrefix))

    srcDir = DownloadAndExtractArchive(APP_NAME, URL)
    ChangeDirectory(srcDir)

    MakeDirectories(context.installPrefix)
    makeCmd = 'make GLEW_DEST="{instDir}" -j{procs} install'.format(
        instDir=context.installPrefix,
        procs=context.numCores
    )
    RunCommand(makeCmd)


if __name__ == "__main__":
    args = ParseInstallArgs(APP_NAME)
    InstallGLEW(args)

