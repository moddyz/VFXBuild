#!/usr/bin/env python

import os
import argparse

from buildUtils import (
    PrintInfo,
    DownloadURL,
    MakeDirectories,
    UnpackArchive,
    GetArchiveRootName,
    ChangeDirectory,
    RunCommand
)


URL = "https://sourceforge.net/projects/boost/files/boost/1.61.0/boost_1_61_0.tar.gz"
ARCHIVE_ROOT_NAME = 'boost_1_61_0'


def InstallBoost(installPrefix):
    if os.path.exists(installPrefix):
        raise RuntimeError("{!r} installation already exists.".format(installPrefix))

    PrintInfo("Current working directory: {}".format(os.getcwd()))

    stagingDir = os.path.join(os.getcwd(), 'staging', 'boost')
    MakeDirectories(stagingDir)

    downloadDst = os.path.join(stagingDir, os.path.split(URL)[1])
    if DownloadURL(URL, downloadDst):
        rootName = Unpack(downloadDst, stagingDir)
    else:
        rootName = GetArchiveRootName(downloadDst)

    buildDir = os.path.join(stagingDir, 'build')
    MakeDirectories(buildDir)

    srcDir = os.path.join(stagingDir, rootName)
    ChangeDirectory(srcDir)

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

