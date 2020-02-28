#!/usr/bin/env python

"""
Installs tbb-4.4.6.

Usage:
    ./installTBB.py <INSTALL_DIR>
"""

import os
import argparse

from buildUtils import (
    DownloadAndExtractArchive,
    ChangeDirectory,
)


APP_NAME = 'tbb'
URL = "https://github.com/01org/tbb/archive/4.4.6.tar.gz"


def InstallTBB(installPrefix):
    # Stage source code.
    if os.path.exists(installPrefix):
        raise RuntimeError("{!r} installation already exists.".format(installPrefix))
    buildDir, srcDir = DownloadAndExtractArchive(APP_NAME, URL)
    ChangeDirectory(srcDir)

    # Build and install from source.



if __name__ == "__main__":
    parser = argparse.ArgumentParser("Installs {}.".format(APP_NAME))
    parser.add_argument('installPrefix', type=str, help="Directory where {} will be installed.".format(APP_NAME))
    args = parser.parse_args()
    InstallTBB(args.installPrefix)

