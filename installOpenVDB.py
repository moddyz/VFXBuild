#!/usr/bin/env python

import os
import argparse

from vfxbuild.tools import (
    CreateSoftwareInstallArgumentParser,
    DownloadAndExtractSoftware,
    ChangeDirectory,
    CMakeBuildAndInstall,
)

from vfxbuild.softwarePackage import OPENVDB


def InstallOpenVDB(context):
    # Stage source code.
    if os.path.exists(context.installPrefix):
        raise RuntimeError("{!r} installation already exists.".format(context.installPrefix))

    srcDir = DownloadAndExtractSoftware(context.name, context.version)
    ChangeDirectory(srcDir)

    cmakeArgs = [
        '-DTBB_ROOT="{}"'.format(context.tbb_location),
        '-DBOOST_ROOT="{}"'.format(context.boost_location),
        '-DOPENEXR_ROOT="{}"'.format(context.openexr_location),
        '-DILMBASE_ROOT="{}"'.format(context.openexr_location),
        '-DBLOSC_ROOT="{}"'.format(context.blosc_location),
    ]

    CMakeBuildAndInstall(srcDir, context.installPrefix, cmakeArgs, numCores=context.numCores)


if __name__ == "__main__":
    args = CreateSoftwareInstallArgumentParser(OPENVDB)
    InstallOpenVDB(args)
