"""
Tools to query software packages.
"""

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
]

import collections

SoftwarePackage = collections.namedtuple(
    'SoftwarePackage',
    ['name', 'version', 'sourceLocation', 'dependencies']
)

# Software package identifiers.
GCC = "gcc"
BOOST = "boost"
GLEW = "glew"
TBB = "tbb"
OPENSUBDIV = "opensubdiv"
USD = "usd"
BLOSC = "blosc"
OPENEXR = "openexr"


def _GetGccPackage(version):
    return SoftwarePackage(
        GCC,
        version,
        "ftp://ftp.gnu.org/gnu/gcc/gcc-{version}/gcc-{version}.tar.gz".format(
            version=version
        ),
        []
    )


def _GetBoostPackage(version):
    return SoftwarePackage(
        BOOST,
        version,
        "https://sourceforge.net/projects/boost/files/boost/{version}/boost_{versionUnderscored}.tar.gz".format(
            version=version,
            versionUnderscored=version.replace(".", "_")
        ),
        []
    )


def _GetGLEWPackage(version):
    return SoftwarePackage(
        GLEW,
        version,
        "https://downloads.sourceforge.net/project/glew/glew/{version}/glew-{version}.tgz".format(
            version=version,
        ),
        []
    )


def _GetTBBPackage(version):
    return SoftwarePackage(
        TBB,
        version,
        "https://github.com/01org/tbb/archive/{version}.tar.gz".format(
            version=version,
        ),
        []
    )


def _GetOpenSubdivPackage(version):
    return SoftwarePackage(
        OPENSUBDIV,
        version,
        "https://github.com/PixarAnimationStudios/OpenSubdiv/archive/v{versionUnderscored}.zip".format(
            versionUnderscored=version.replace(".", "_"),
        ),
        [GLEW]
    )


def _GetUSDPackage(version):
    return SoftwarePackage(
        USD,
        version,
        "https://github.com/PixarAnimationStudios/USD/archive/v{version}.tar.gz".format(
            version=version,
        ),
        [GLEW, TBB, BOOST, OPENSUBDIV]
    )


def _GetBloscPackage(version):
    return SoftwarePackage(
        BLOSC,
        version,
        "https://github.com/Blosc/c-blosc/archive/v{version}.tar.gz".format(
            version=version,
        ),
        []
    )


def _GetOpenExrPackage(version):
    return SoftwarePackage(
        BLOSC,
        version,
        "https://github.com/AcademySoftwareFoundation/openexr/archive/v{version}.tar.gz".format(
            version=version,
        ),
        []
    )


_SOFTWARE_PACKAGE_LOOKUP = dict([
    (GCC, _GetGccPackage),
    (BOOST, _GetBoostPackage),
    (GLEW, _GetGLEWPackage),
    (TBB, _GetTBBPackage),
    (OPENSUBDIV, _GetOpenSubdivPackage),
    (USD, _GetUSDPackage),
    (BLOSC, _GetBloscPackage),
    (OPENEXR, _GetOpenExrPackage),
])


def GetSoftwarePackage(name, version):
    getPackageFn = _SOFTWARE_PACKAGE_LOOKUP[name]
    return getPackageFn(version)
