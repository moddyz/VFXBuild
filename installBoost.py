#!/usr/bin/env python

"""
Installs boost-1.61.0.

Usage:
    ./installBoost.py <INSTALL_DIR>
"""

import os
import argparse

from VFXBuild.tools import (
    ParseInstallArgs,
    DownloadAndExtractArchive,
    MakeDirectories,
    ChangeDirectory,
    RunCommand,
)


APP_NAME = "boost"
URL = "https://sourceforge.net/projects/boost/files/boost/1.61.0/boost_1_61_0.tar.gz"


def InstallBoost(context):
    # Stage source code.
    if os.path.exists(context.installPrefix):
        raise RuntimeError("{!r} installation already exists.".format(context.installPrefix))

    srcDir = DownloadAndExtractArchive(APP_NAME, URL)
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
    args = ParseInstallArgs(APP_NAME)
    InstallBoost(args)

