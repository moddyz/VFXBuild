#!/usr/bin/env python

import os
import argparse

from vfxbuild.tools import (
    CreateSoftwareInstallArgumentParser,
    DownloadAndExtractSoftware,
    ChangeDirectory,
    CMakeBuildAndInstall,
)


def InstallUSD(context):
    # Stage source code.
    if os.path.exists(context.installPrefix):
        raise RuntimeError("{!r} installation already exists.".format(context.installPrefix))

    srcDir = DownloadAndExtractSoftware(context.name, context.version)
    ChangeDirectory(srcDir)

    cmakeArgs = [
        '-DCMAKE_INSTALL_PREFIX="{}"'.format(context.installPrefix),
        '-DCMAKE_PREFIX_PATH="{}"'.format(context.installPrefix),
        '-DCMAKE_BUILD_TYPE=Debug',

        # TBB
        '-DTBB_USE_DEBUG_BUILD=ON',
        '-DTBB_INCLUDE_DIRS="{}"'.format(os.path.join(context.tbb_location, 'include')),
        '-DTBB_tbb_LIBRARY_DEBUG="{}"'.format(os.path.join(context.tbb_location, 'lib', 'libtbb_debug.so')),
        '-DTBB_tbb_LIBRARY_RELEASE="{}"'.format(os.path.join(context.tbb_location, 'lib', 'libtbb.so')),

        # Boost
        '-DBoost_INCLUDE_DIR="{}"'.format(os.path.join(context.boost_location, 'include')),
        '-DBoost_LIBRARY_DIR_DEBUG="{}"'.format(os.path.join(context.boost_location, 'lib')),
        '-DBoost_LIBRARY_DIR_RELEASE="{}"'.format(os.path.join(context.boost_location, 'lib')),

        # Glew
        '-DGLEW_INCLUDE_DIR="{}"'.format(os.path.join(context.glew_location, 'include')),
        '-DGLEW_LIBRARY="{}"'.format(os.path.join(context.glew_location, 'lib64', 'libGLEW.so')),

        # OpenSubdiv
        '-DOPENSUBDIV_INCLUDE_DIR="{}"'.format(os.path.join(context.opensubdiv_location, 'include')),
        '-DOPENSUBDIV_OSDCPU_LIBRARY="{}"'.format(os.path.join(context.opensubdiv_location, 'lib', 'libosdCPU.so')),
        '-DOPENSUBDIV_OSDGPU_LIBRARY="{}"'.format(os.path.join(context.opensubdiv_location, 'lib', 'libosdGPU.so')),

        '-DPXR_ENABLE_PYTHON_SUPPORT=ON',
        '-DBUILD_SHARED_LIBS=ON',
        '-DPXR_BUILD_DOCUMENTATION=OFF',
        '-DPXR_BUILD_TESTS=OFF',
        '-DPXR_BUILD_IMAGING=ON',
        '-DPXR_BUILD_USD_IMAGING=ON',
        '-DPXR_BUILD_USDVIEW=ON',
        '-DPXR_ENABLE_PTEX_SUPPORT=OFF',
        '-DPXR_ENABLE_OPENVDB_SUPPORT=OFF',
        '-DPXR_BUILD_EMBREE_PLUGIN=OFF',
        '-DPXR_BUILD_PRMAN_PLUGIN=OFF',
        '-DPXR_BUILD_OPENIMAGEIO_PLUGIN=OFF',
        '-DPXR_BUILD_OPENCOLORIO_PLUGIN=OFF',
        '-DPXR_BUILD_ALEMBIC_PLUGIN=OFF',
        '-DPXR_BUILD_DRACO_PLUGIN=OFF',
        '-DPXR_BUILD_MATERIALX_PLUGIN=OFF',
        '-DPXR_BUILD_KATANA_PLUGIN=OFF',
        '-DPXR_BUILD_HOUDINI_PLUGIN=OFF',
    ]

    CMakeBuildAndInstall(srcDir, context.installPrefix, cmakeArgs, numCores=context.numCores)


if __name__ == "__main__":
    args = CreateSoftwareInstallArgumentParser("usd")
    InstallUSD(args)
