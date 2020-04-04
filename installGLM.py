#!/usr/bin/env python

import os

from vfxbuild.tools import (
    CreateSoftwareInstallArgumentParser,
    DownloadAndExtractSoftware,
    ChangeDirectory,
    MakeDirectories,
    CopyDirectory,
)


def InstallGLM(context):
    # Stage source code.
    if os.path.exists(context.installPrefix):
        raise RuntimeError("{!r} installation already exists.".format(context.installPrefix))

    srcDir = DownloadAndExtractSoftware(context.name, context.version)
    ChangeDirectory(srcDir)

    # Install by copying files.
    MakeDirectories(context.installPrefix)
    includePath = os.path.join(context.installPrefix, 'include')
    MakeDirectories(includePath)
    CopyDirectory("glm", os.path.join(includePath, "glm"))


if __name__ == "__main__":
    args = CreateSoftwareInstallArgumentParser("glm")
    InstallGLM(args)
