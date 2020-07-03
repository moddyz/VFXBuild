#!/usr/bin/env python

import os

from vfxbuild.tools import (
    CreateSoftwareInstallArgumentParser,
    DownloadAndExtractSoftware,
    ChangeDirectory,
    MakeDirectories,
    RunCommand,
    CopyFiles,
    CopyDirectory,
)


def InstallTBB(context):
    # Stage source code.
    if os.path.exists(context.installPrefix):
        raise RuntimeError(
            "{!r} installation already exists.".format(context.installPrefix)
        )

    srcDir = DownloadAndExtractSoftware(context.name, context.version)
    ChangeDirectory(srcDir)

    # Build from source.
    makeCmd = " ".join(["make", "-j{}".format(context.numCores),])
    RunCommand(makeCmd)

    # Install by copying files.
    MakeDirectories(context.installPrefix)
    libPath = os.path.join(context.installPrefix, "lib")
    includePath = os.path.join(context.installPrefix, "include")
    MakeDirectories(libPath)
    MakeDirectories(includePath)

    CopyFiles("build/*_release/libtbb*.*", libPath)
    CopyFiles("build/*_debug/libtbb*.*", libPath)
    CopyDirectory("include/serial", os.path.join(includePath, "serial"))
    CopyDirectory("include/tbb", os.path.join(includePath, "tbb"))


if __name__ == "__main__":
    args = CreateSoftwareInstallArgumentParser("tbb")
    InstallTBB(args)
