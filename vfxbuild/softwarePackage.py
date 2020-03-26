"""
Tools to query software packages.
"""

import collections

__all__ = [
    'GetSoftwarePackage',
    "GCC",
    "BOOST",
    "GLEW",
    "TBB",
    "OPENSUBDIV",
    "USD",
    "BLOSC",
    "OPENEXR",
    "OPENVDB",
    "GLFW",
]

#
# Software package identifiers.
#
GCC = "gcc"
BOOST = "boost"
GLEW = "glew"
TBB = "tbb"
OPENSUBDIV = "opensubdiv"
USD = "usd"
BLOSC = "blosc"
OPENEXR = "openexr"
OPENVDB = "openvdb"
GLFW = "glfw"


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
        mandatoryDependencies (list): `SoftwareDependency`s encoding all the mandatory dependencies of the
            current package.
        optionalDependencies (list): `SoftwareDependency`s encoding all the optional dependencies of the
            current package.
    """

    def __init__(
        self,
        name,
        version,
        sourceLocation,
        mandatoryDependencies=None,
        optionalDependencies=None):

        self.name = name
        self.version = version
        self.sourceLocation = sourceLocation

        mandatoryDependencies = mandatoryDependencies or []
        optionalDependencies = optionalDependencies or []
        self.dependencies = [SoftwareDependency(name, mandatory=True) for name in mandatoryDependencies]
        self.dependencies.extend([SoftwareDependency(name, mandatory=False) for name in optionalDependencies])


def _GetGccPackage(version):
    return SoftwarePackage(
        GCC,
        version,
        "ftp://ftp.gnu.org/gnu/gcc/gcc-{version}/gcc-{version}.tar.gz".format(
            version=version
        ),
    )


def _GetBoostPackage(version):
    return SoftwarePackage(
        BOOST,
        version,
        "https://sourceforge.net/projects/boost/files/boost/{version}/boost_{versionUnderscored}.tar.gz".format(
            version=version,
            versionUnderscored=version.replace(".", "_")
        ),
    )


def _GetGLEWPackage(version):
    return SoftwarePackage(
        GLEW,
        version,
        "https://downloads.sourceforge.net/project/glew/glew/{version}/glew-{version}.tgz".format(
            version=version,
        ),
    )


def _GetTBBPackage(version):
    return SoftwarePackage(
        TBB,
        version,
        "https://github.com/01org/tbb/archive/{version}.tar.gz".format(
            version=version,
        ),
    )


def _GetOpenSubdivPackage(version):
    return SoftwarePackage(
        OPENSUBDIV,
        version,
        "https://github.com/PixarAnimationStudios/OpenSubdiv/archive/v{versionUnderscored}.zip".format(
            versionUnderscored=version.replace(".", "_"),
        ),
        mandatoryDependencies=[
            GLEW,
        ]
    )


def _GetUSDPackage(version):
    return SoftwarePackage(
        USD,
        version,
        "https://github.com/PixarAnimationStudios/USD/archive/v{version}.tar.gz".format(
            version=version,
        ),
        mandatoryDependencies=[
            GLEW,
            TBB,
            BOOST,
            OPENSUBDIV,
        ],
    )


def _GetBloscPackage(version):
    return SoftwarePackage(
        BLOSC,
        version,
        "https://github.com/Blosc/c-blosc/archive/v{version}.tar.gz".format(
            version=version,
        ),
    )


def _GetOpenEXRPackage(version):
    return SoftwarePackage(
        OPENEXR,
        version,
        "https://github.com/AcademySoftwareFoundation/openexr/archive/v{version}.tar.gz".format(
            version=version,
        ),
    )


def _GetGLFWPackage(version):
    return SoftwarePackage(
        GLFW,
        version,
        "https://github.com/glfw/glfw/archive/{version}.tar.gz".format(
            version=version,
        ),
    )


def _GetOpenVDBPackage(version):
    return SoftwarePackage(
        OPENVDB,
        version,
        "https://github.com/AcademySoftwareFoundation/openvdb/archive/v{version}.tar.gz".format(
            version=version,
        ),
        mandatoryDependencies=[
            BOOST,
            TBB,
            OPENEXR,
            BLOSC,
            GLFW,
        ],
    )


_SOFTWARE_PACKAGE_LOOKUP = dict([
    (GCC, _GetGccPackage),
    (BOOST, _GetBoostPackage),
    (GLEW, _GetGLEWPackage),
    (TBB, _GetTBBPackage),
    (OPENSUBDIV, _GetOpenSubdivPackage),
    (USD, _GetUSDPackage),
    (BLOSC, _GetBloscPackage),
    (OPENEXR, _GetOpenEXRPackage),
    (OPENVDB, _GetOpenVDBPackage),
    (GLFW, _GetGLFWPackage),
])


def GetSoftwarePackage(name, version):
    getPackageFn = _SOFTWARE_PACKAGE_LOOKUP[name]
    return getPackageFn(version)
