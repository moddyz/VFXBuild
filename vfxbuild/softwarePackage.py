"""
Tools to query software packages.
"""

import os
import json

__all__ = [
    "GetAvailableSoftwareVersions",
    "GetSoftwarePackage",
]


def GetAvailableSoftwareVersions(name):
    """
    Get all the available versions of a named software.

    Args:
        name (str): name of the software.

    Returns:
        list: available versions.
    """
    return _SOFTWARE_PACKAGE_LOOKUP.get(name, [])


def GetSoftwarePackage(name, version):
    """
    Get the software package for the specified name & version.

    Args:
        name (str): name of the software.
        version (str): version of the software.

    Returns:
        SoftwarePackage: retrieved package.

    Raises:
        KeyError: if requested software package is not registered.
    """
    packageVersions = _SOFTWARE_PACKAGE_LOOKUP[name]
    return packageVersions[version]


class SoftwareDependency:
    """
    Description of a software dependency, with the target name and whether or not it is a mandatory dependency.
    """

    def __init__(self, name, mandatory=True):
        self.name = name
        self.mandatory = mandatory


class SoftwarePackage:
    """
    A representation of a versioned software package.

    Provides information on the download location, and dependencies.

    Args:
        name (str): name of the software package.
        version (str): version of the software package.
        sourceLocation (str): location to download this software.

    Keyword Args:
        dependencies (list): `SoftwareDependency`s encoding all the software dependencies of the current package.
    """

    def __init__(self, name, version, sourceLocation, dependencies=None):
        self.name = name
        self.version = version
        self.sourceLocation = sourceLocation
        self.dependencies = dependencies or []

    def GetId(self):
        """
        Get the unique string identifier for this software package, which is the concatenation
        of the name and version with a hyphen delimiter.
        """
        return "-".join(name, version)


# Directory name where the software package descriptors are stored.
_SOFTWARE_PACKAGES_DIR = "softwarePackages"

# dict of software name -> (dict of version -> SoftwarePackage)
_SOFTWARE_PACKAGE_LOOKUP = {}


def _PopulateSoftwarePackages():
    softwarePackagesDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), _SOFTWARE_PACKAGES_DIR)
    for path in os.listdir(softwarePackagesDir):
        packagePath = os.path.join(softwarePackagesDir, path)
        with open(packagePath, 'r') as packageFile:
            packageData = json.load(packageFile)

            # Construct SoftwarePackage.
            dependencies = [SoftwareDependency(dep["name"], mandatory=dep["mandatory"])
                            for dep in packageData.get("dependencies", [])]
            softwarePackage = SoftwarePackage(
                packageData["name"],
                packageData["version"],
                packageData["sourceLocation"],
                dependencies=dependencies
            )

            # Insert into look-up table.
            _SOFTWARE_PACKAGE_LOOKUP.setdefault(packageData["name"], {})
            if softwarePackage.version in _SOFTWARE_PACKAGE_LOOKUP[packageData["name"]]:
                raise KeyError("Software package '{id}' already exists!".format(softwarePackage.GetId()))
            _SOFTWARE_PACKAGE_LOOKUP[packageData["name"]][softwarePackage.version] = softwarePackage


# Populate on import.
_PopulateSoftwarePackages()
