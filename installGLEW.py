#!/usr/bin/env python

import os

from vfxbuild.tools import (
    ParseInstallArgs,
    DownloadAndExtractSoftware,
    ChangeDirectory,
    MakeDirectories,
    RunCommand,
)


def InstallGLEW(context):
    # Stage source code.
    if os.path.exists(context.installPrefix):
        raise RuntimeError("{!r} installation already exists.".format(context.installPrefix))

    srcDir = DownloadAndExtractSoftware(context.name, context.version)
    ChangeDirectory(srcDir)

    MakeDirectories(context.installPrefix)
    makeCmd = 'make GLEW_DEST="{instDir}" -j{procs} install'.format(
        instDir=context.installPrefix,
        procs=context.numCores
    )
    RunCommand(makeCmd)


if __name__ == "__main__":
    args = ParseInstallArgs("glew")
    InstallGLEW(args)

