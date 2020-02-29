#!/usr/bin/env python

"""
Installs boost-1.61.0.

Usage:
    ./installBoost.py <INSTALL_DIR>
"""

import os
import argparse

from vfxbuild.tools import (
    ParseInstallArgs,
    DownloadAndExtractSoftware,
    MakeDirectories,
    ChangeDirectory,
    RunCommand,
)


def InstallBoost(context):
    # Stage source code.
    if os.path.exists(context.installPrefix):
        raise RuntimeError("{!r} installation already exists.".format(context.installPrefix))

    srcDir = DownloadAndExtractSoftware(context.name, context.version)
    ChangeDirectory(srcDir)

    # Build dir.
    buildDir = os.path.join(srcDir, 'build')
    MakeDirectories(buildDir)

    # Build & install from source.
    bootstrapCmd = "./bootstrap.sh --prefix=\"{}\"".format(context.installPrefix)
    RunCommand(bootstrapCmd)

    MakeDirectories(context.installPrefix)
    b2Cmd = " ".join([
        "./b2",
        "--prefix={}".format(context.installPrefix),
        "--build-dir={}".format(buildDir),
        "-j{}".format(context.numCores),
        "address-model=64",
        "link=shared",
        "runtime-link=shared",
        "threading=multi",
        "-a",
        "install"
    ])
    RunCommand(b2Cmd)


if __name__ == "__main__":
    args = ParseInstallArgs("boost")
    InstallBoost(args)
