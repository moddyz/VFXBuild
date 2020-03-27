#!/usr/bin/env python

import os

from vfxbuild.tools import (
    CreateSoftwareInstallArgumentParser,
    DownloadAndExtractSoftware,
    ChangeDirectory,
    CMakeBuildAndInstall,
)


def InstallOpenImageIO(context):
    # Stage source code.
    if os.path.exists(context.installPrefix):
        raise RuntimeError("{!r} installation already exists.".format(context.installPrefix))

    srcDir = DownloadAndExtractSoftware(context.name, context.version)
    ChangeDirectory(srcDir)

    cmakeArgs = [
        '-DBOOST_ROOT="{}"'.format(context.boost_location),
        '-DILMBASE_ROOT="{}"'.format(context.openexr_location),
    ]
    CMakeBuildAndInstall(srcDir, context.installPrefix, cmakeArgs, numCores=context.numCores)


if __name__ == "__main__":
    args = CreateSoftwareInstallArgumentParser("openimageio")
    InstallOpenImageIO(args)
