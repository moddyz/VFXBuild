#!/usr/bin/env python

import os
import argparse

from vfxbuild.tools import (
    CreateSoftwareInstallArgumentParser,
    DownloadAndExtractSoftware,
    MakeDirectories,
    ChangeDirectory,
    CMakeBuildAndInstall,
)


def InstallOpenSubdiv(context):
    # Stage source code.
    if os.path.exists(context.installPrefix):
        raise RuntimeError(
            "{!r} installation already exists.".format(context.installPrefix)
        )

    srcDir = DownloadAndExtractSoftware(context.name, context.version)
    ChangeDirectory(srcDir)

    cmakeArgs = [
        '-DGLEW_LOCATION="{}"'.format(context.glew_location),
        '-DGLEW_LIBRARY="{}"'.format(
            os.path.join(context.glew_location, "lib64", "libGLEW.so")
        ),
        "-DNO_PTEX=ON",
        "-DNO_TBB=ON",
        "-DNO_EXAMPLES=ON",
        "-DNO_TUTORIALS=ON",
        "-DNO_REGRESSION=ON",
        "-DNO_DOC=ON",
        "-DNO_OMP=ON",
        "-DNO_CUDA=ON",
        "-DNO_OPENCL=ON",
        "-DNO_DX=ON",
        "-DNO_TESTS=ON",
    ]

    CMakeBuildAndInstall(
        srcDir, context.installPrefix, cmakeArgs, numCores=context.numCores
    )


if __name__ == "__main__":
    args = CreateSoftwareInstallArgumentParser("opensubdiv")
    InstallOpenSubdiv(args)
