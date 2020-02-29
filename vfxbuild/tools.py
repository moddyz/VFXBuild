"""
Common tools for installation & building VFX software.

Snippets taken from USD/build_scripts/build_usd.py
"""

import os
import argparse
import urllib2
import subprocess
import shlex
import tarfile
import glob
import shutil
import multiprocessing
import tempfile

from softwarePackage import GetSoftwarePackage


def PrintInfo(message):
    print("[INFO] {}".format(message))


def GetCPUCount():
    try:
        return multiprocessing.cpu_count()
    except NotImplementedError:
        return 1


def MakeDirectories(directoryPath):
    if not os.path.isdir(directoryPath):
        PrintInfo("Making directories: {!r}".format(directoryPath))
        os.makedirs(directoryPath)
    else:
        PrintInfo("{!r} already exists! Skipping making directory.".format(directoryPath))


def ChangeDirectory(directoryPath):
    PrintInfo("Changing directory: {!r}".format(directoryPath))
    os.chdir(directoryPath)


def CopyFiles(srcPattern, dstDir):
    srcFiles = glob.glob(srcPattern)
    if not srcFiles:
        raise RuntimeError("File(s) to copy {srcPattern} not found".format(srcPattern=srcPattern))

    for srcFile in srcFiles:
        PrintInfo("Copying {srcFile} to {dstDir}\n" .format(srcFile=srcFile, dstDir=dstDir))
        shutil.copy(srcFile, dstDir)


def CopyDirectory(srcDir, dstDir):
    if os.path.isdir(dstDir):
        PrintInfo("Deleting {dstDir}\n" .format(dstDir=dstDir))
        shutil.rmtree(dstDir)

    PrintInfo("Copying {srcDir} to {dstDir}\n" .format(srcDir=srcDir, dstDir=dstDir))
    shutil.copytree(srcDir, dstDir)


def RunCommand(command):
    PrintInfo("Running shell command {!r}".format(command))
    process = subprocess.Popen(shlex.split(command))
    process.wait()


def DownloadURL(url, dstFilePath):
    if os.path.exists(dstFilePath):
        PrintInfo("{!r} already exists! Skipping download.".format(dstFilePath))
        return False

    PrintInfo("Downloading {} -> {}".format(url, dstFilePath))
    command = "curl {progress} -L -o {filename} {url}".format(
        progress="-#",
        filename=dstFilePath,
        url=url
    )
    RunCommand(command)

    return True


def ExtractArchive(srcFile, dstPath):
    archive = tarfile.open(srcFile)
    rootDir = archive.getnames()[0].split('/')[0]
    unpackDir = os.path.join(dstPath, rootDir)
    if not os.path.exists(unpackDir):
        PrintInfo("Unpacking {} -> {}".format(srcFile, unpackDir))
        archive.extractall(dstPath)
    else:
        PrintInfo("{!r} already exists! Skipping unpack.".format(unpackDir))

    return rootDir


def DownloadAndExtractSoftware(name, version):
    softwarePackage = GetSoftwarePackage(name, version)

    # Create staging directories.
    stagingDir = os.path.join(tempfile.gettempdir(), 'staging', name)
    MakeDirectories(stagingDir)

    # Download and extract.
    downloadDst = os.path.join(stagingDir, os.path.split(softwarePackage.sourceLocation)[1])
    DownloadURL(softwarePackage.sourceLocation, downloadDst)
    rootName = ExtractArchive(downloadDst, stagingDir)

    # Create source dir.
    srcDir = os.path.join(stagingDir, rootName)

    return srcDir


def ParseInstallArgs(softwareName):
    parser = argparse.ArgumentParser("Build and install software.")

    parser.add_argument(
        '-n',
        '--name',
        type=str,
        default=softwareName,
        help="Number of cores used to build",
    )

    parser.add_argument(
        '-v',
        '--version',
        type=str,
        required=True,
        help="Version of the software to install."
    )

    parser.add_argument(
        '-j',
        '--numCores',
        type=int,
        default=GetCPUCount(),
        help="Number of cores used to build",
    )

    parser.add_argument(
        'installPrefix',
        type=str,
        help="Directory where software will be installed."
    )

    args = parser.parse_args()
    return args
