#!/usr/bin/env python

import os
import argparse

from vfxbuild.tools import (
    CreateSoftwareInstallArgumentParser,
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
        "--layout=tagged",
        "-j{}".format(context.numCores),
        "variant=debug",
        "variant=release",
        "address-model=64",
        "link=shared",
        "runtime-link=shared",
        "threading=multi",
        "-a",
        "install"
    ])
    RunCommand(b2Cmd)


if __name__ == "__main__":
    args = CreateSoftwareInstallArgumentParser("boost")
    InstallBoost(args)
