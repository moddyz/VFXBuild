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
    PrintInfo("Unpacking {} -> {}".format(srcFile, dstPath))
    archive = tarfile.open(srcFile)
    archive.extractall(dstPath)
    rootDir = archive.getnames()[0].split('/')[0]
    return rootDir


def GetArchiveRootName(srcFile):
    archive = tarfile.open(srcFile)
    rootDir = archive.getnames()[0].split('/')[0]
    return rootDir
