#!/usr/bin/env python

import os

from vfxbuild.tools import (
    CreateSoftwareInstallArgumentParser,
    DownloadAndExtractSoftware,
    ChangeDirectory,
    CMakeBuildAndInstall,
)

from vfxbuild.softwarePackage import OPENEXR


def InstallOpenEXR(context):
    # Stage source code.
    if os.path.exists(context.installPrefix):
        raise RuntimeError("{!r} installation already exists.".format(context.installPrefix))

    srcDir = DownloadAndExtractSoftware(context.name, context.version)
    ChangeDirectory(srcDir)

    cmakeArgs = []
    CMakeBuildAndInstall(srcDir, context.installPrefix, cmakeArgs, numCores=context.numCores)


if __name__ == "__main__":
    args = CreateSoftwareInstallArgumentParser(OPENEXR)
    InstallOpenEXR(args)