#!/usr/bin/env python

"""
Installs boost-1.61.0.

Usage:
    ./installBoost.py <INSTALL_DIR>
"""

import os
import argparse

from buildUtils import (
    DownloadAndExtractArchive,
    ChangeDirectory,
)


URL = "https://sourceforge.net/projects/boost/files/boost/1.61.0/boost_1_61_0.tar.gz"


def InstallBoost(installPrefix):
    # Stage source code.
    if os.path.exists(installPrefix):
        raise RuntimeError("{!r} installation already exists.".format(installPrefix))
    buildDir, srcDir = DownloadAndExtractArchive(APP_NAME, URL)
    ChangeDirectory(srcDir)

    # Build & install from source.
    bootstrapCmd = "./bootstrap.sh --prefix=\"{}\"".format(installPrefix)
    RunCommand(bootstrapCmd)

    b2Cmd = " ".join([
        "./b2",
        "--prefix={}".format(installPrefix),
        "--build-dir={}".format(buildDir),
        "-j8",
        "address-model=64",
        "link=shared",
        "runtime-link=shared",
        "threading=multi",
        "-a",
        "install"
    ])
    RunCommand(b2Cmd)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Installs boost.")
    parser.add_argument('installPrefix', type=str, help="Directory where boost will be installed.")
    args = parser.parse_args()
    InstallBoost(args.installPrefix)

