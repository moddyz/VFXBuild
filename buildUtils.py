"""
Build utilities.

Snippets taken from USD/build_scripts/build_usd.py
"""

import os
import urllib2
import subprocess
import shlex
import tarfile


def PrintInfo(message):
    print("[INFO] {}".format(message))


def MakeDirectories(directoryPath):
    if not os.path.isdir(directoryPath):
        PrintInfo("Making directories: {!r}".format(directoryPath))
        os.makedirs(directoryPath)


def ChangeDirectory(directoryPath):
    PrintInfo("Changing directory: {!r}".format(directoryPath))
    os.chdir(directoryPath)


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


def UnpackArchive(srcFile, dstPath):
    archive = tarfile.open(srcFile)
    rootDir = archive.getnames()[0].split('/')[0]
    unpackDir = os.path.join(dstPath, rootDir)
    if not os.path.exists(unpackDir):
        PrintInfo("Unpacking {} -> {}".format(srcFile, unpackDir))
        archive.extractall(dstPath)
    else:
        PrintInfo("{!r} already exists! Skipping unpack.".format(unpackDir))

    return rootDir


def DownloadAndExtractArchive(appName, url):
    # Create staging directories.
    stagingDir = os.path.join(os.getcwd(), 'staging', appName)
    MakeDirectories(stagingDir)

    # Download and unpack.
    downloadDst = os.path.join(stagingDir, os.path.split(url)[1])
    DownloadURL(url, downloadDst)
    rootName = UnpackArchive(downloadDst, stagingDir)

    # Create build dir, and return build and source dir paths.
    buildDir = os.path.join(stagingDir, 'build')
    MakeDirectories(buildDir)
    srcDir = os.path.join(stagingDir, rootName)

    return srcDir, buildDir
