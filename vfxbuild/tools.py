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
import zipfile
import glob
import shutil
import multiprocessing
import tempfile

from softwarePackage import GetAvailableSoftwareVersions, GetSoftwarePackage


def PrintInfo(message):
    """
    Shim around print to add a [INFO] prefix.
    """
    print("[INFO] {}".format(message))


def GetCPUCount():
    """
    Get the CPU count.  Shim around multiprocessing.cpu_count().
    """
    try:
        return multiprocessing.cpu_count()
    except NotImplementedError:
        return 1


def MakeDirectories(directoryPath):
    """
    Fail-safe directory hierarchy creation.

    Args:
        directoryPath (str): directory path to create.
    """
    if not os.path.isdir(directoryPath):
        PrintInfo("Making directories: {!r}".format(directoryPath))
        os.makedirs(directoryPath)
    else:
        PrintInfo(
            "{!r} already exists! Skipping directories creation.".format(directoryPath)
        )


def RemoveDirectory(directoryPath):
    """
    Fail-safe directory removal.

    Args:
        directoryPath (str): directory to remove.
    """
    if os.path.isdir(directoryPath):
        PrintInfo("Deleting {directory}\n".format(directory=directoryPath))
        shutil.rmtree(directoryPath)
    else:
        PrintInfo(
            "{!r} does not exist. Skipping directory removal.".format(directoryPath)
        )


def ChangeDirectory(directoryPath):
    """
    Shim around os.chdir for changing to a new working directory.
    """
    PrintInfo("Changing directory: {!r}".format(directoryPath))
    os.chdir(directoryPath)


def CopyFiles(srcPattern, dstDir):
    """
    Copy files matching ``srcPattern`` into ``dstDir``.

    Args:
        srcPattern (str): the glob pattern to match names of files.
        dstDir (str): the destination directory to copy all the files to.
    """
    srcFiles = glob.glob(srcPattern)
    if not srcFiles:
        raise RuntimeError(
            "File(s) to copy {srcPattern} not found".format(srcPattern=srcPattern)
        )

    for srcFile in srcFiles:
        PrintInfo(
            "Copying {srcFile} to {dstDir}\n".format(srcFile=srcFile, dstDir=dstDir)
        )
        shutil.copy(srcFile, dstDir)


def CopyDirectory(srcDir, dstDir):
    """
    Shim around ``shutil.copytree`` whicih prints out useful information.
    """
    RemoveDirectory(dstDir)
    PrintInfo("Copying {srcDir} to {dstDir}\n".format(srcDir=srcDir, dstDir=dstDir))
    shutil.copytree(srcDir, dstDir)


def RunCommand(command, expectedCode=0):
    """
    Execute a shell command ``command``, expecting ``expectedCode`` return code.

    Args:
        command (str): the full shell command to run.
        expectedCode (int): the expected return code of the command.

    Raises:
        RuntimeError: if the actual return code of the command does not match the expected code.
    """
    PrintInfo("Running shell command {!r}".format(command))
    process = subprocess.Popen(shlex.split(command))
    returnCode = process.wait()
    if returnCode != expectedCode:
        raise RuntimeError(
            "Got a non-0 return code '{returnCode}' from {command}".format(
                returnCode=returnCode, command=command
            )
        )


def CMakeBuildAndInstall(srcDir, installPrefix, cmakeArgs, numCores=GetCPUCount()):
    """
    Run CMake build & install from source code.

    Args:
        srcDir (str): path to the source code.
        installPrefix (str): location to install the built software.
        cmakeArgs (list): list of CMake arguments.
    """
    buildDir = os.path.join(srcDir, "build")
    RemoveDirectory(buildDir)
    MakeDirectories(buildDir)
    ChangeDirectory(buildDir)

    cmakeCmd = " ".join(
        ["cmake", '-DCMAKE_INSTALL_PREFIX="{}"'.format(installPrefix),]
        + cmakeArgs
        + [srcDir]
    )
    RunCommand(cmakeCmd)
    cmakeBuildCmd = " ".join(
        ["cmake", "--build .", "--target install", "--", "-j {}".format(numCores)]
    )
    RunCommand(cmakeBuildCmd)


def DownloadURL(url, dstPath):
    """
    Download the ``url`` and save to disk at ``dstPath``.

    Args:
        url (str): the URL to download.
        dstPath (str): the file path to save the downloaded file.
    """
    if os.path.exists(dstPath):
        PrintInfo("{!r} already exists! Skipping download.".format(dstPath))

    PrintInfo("Downloading {} -> {}".format(url, dstPath))
    command = "curl {progress} -L -o {filename} {url}".format(
        progress="-#", filename=dstPath, url=url
    )
    RunCommand(command)


def ExtractArchive(srcArchive, dstPath):
    """
    Extracts the archive ``srcArchive`` into ``dstPath``.

    Args:
        srcArchive (str): path to the archive file.
        dstPath (str): parent path to extract the archive into.

    Returns:
        str: the path to the root directory of the extracted archive.
    """
    if tarfile.is_tarfile(srcArchive):
        archive = tarfile.open(srcArchive)
        rootDir = archive.getnames()[0].split("/")[0]
    elif zipfile.is_zipfile(srcArchive):
        archive = zipfile.ZipFile(srcArchive)
        rootDir = archive.namelist()[0].split("/")[0]

    extractedDir = os.path.join(dstPath, rootDir)

    if not os.path.exists(unpackDir):
        PrintInfo("Unpacking {} -> {}".format(srcArchive, unpackDir))
        archive.extractall(dstPath)
    else:
        PrintInfo("{!r} already exists! Skipping unpack.".format(unpackDir))

    return extractedDir


def DownloadAndExtractSoftware(name, version):
    """
    Downloads the software of ``name`` and ``version``, and extracts
    it to a temporary location.

    Args:
        name (str): name of the software.
        version (str): version of the software.

    Returns:
        str: path to the root of the extracted software.
    """
    softwarePackage = GetSoftwarePackage(name, version)

    # Create temporary staging directories.
    stagingDir = os.path.join(tempfile.gettempdir(), "staging", name)
    MakeDirectories(stagingDir)

    # Download and extract.
    downloadDst = os.path.join(
        stagingDir, os.path.split(softwarePackage.sourceLocation)[1]
    )
    DownloadURL(softwarePackage.sourceLocation, downloadDst)
    extractedDir = ExtractArchive(downloadDst, stagingDir)

    # Create source dir.
    sourceDir = os.path.join(stagingDir, os.path.basename(extractedDir))

    return sourceDir


def CreateSoftwareInstallArgumentParser(softwareName):
    """
    Create an ``argparse.ArgumentParser`` with appropriate arguments building and
    installing ``softwareName``.

    Args:
        softwareName (str): name of the software.

    Returns:
        argparse.ArgumentParser: dynamically populated argument parser.
    """
    parser = argparse.ArgumentParser("Build and install software.")

    parser.add_argument(
        "-n",
        "--name",
        type=str,
        default=softwareName,
        help="Name of the software to install.",
    )

    parser.add_argument(
        "-v",
        "--version",
        type=str,
        choices=GetAvailableSoftwareVersions(softwareName),
        required=True,
        help="Version of the software to install.",
    )

    # Parse known args up to this point.
    # argparse will list the available version if version is *not* supplied!
    args, remainingArgs = parser.parse_known_args()

    # Look-up the dependencies - which dependent on the name & version being supplied.
    softwarePackage = GetSoftwarePackage(softwareName, args.version)
    for dependency in softwarePackage.dependencies:
        parser.add_argument(
            "--{name}-location".format(name=dependency.name),
            type=str,
            required=dependency.mandatory,
            help="Location of {!r} dependency.".format(dependency.name),
            default="",
        )

    # Add the rest of the goodness.
    parser.add_argument(
        "-j",
        "--numCores",
        type=int,
        default=GetCPUCount(),
        help="Number of cores used to build",
    )

    parser.add_argument(
        "installPrefix", type=str, help="Directory where software will be installed."
    )

    # Rebuild parsed arguments, and extend with the un-parsed ones.
    fullArgs = ["--name", args.name, "--version", args.version]
    fullArgs.extend(remainingArgs)

    # Parse again, with the full data.
    args = parser.parse_args(fullArgs)
    return args
