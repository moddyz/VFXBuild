"""
Tools to query software packages.
"""

__all__ = [
    'GetSoftwarePackage',
]

import collections

SoftwarePackage = collections.namedtuple(
    'SoftwarePackage',
    ['name', 'version', 'sourceLocation', 'dependencies']
)


def _GetGccPackage(version):
    return SoftwarePackage(
        "gcc",
        version,
        "ftp://ftp.gnu.org/gnu/gcc/gcc-{version}/gcc-{version}.tar.gz".format(
            version=version
        ),
        []
    )


def _GetBoostPackage(version):
    return SoftwarePackage(
        "boost",
        version,
        "https://sourceforge.net/projects/boost/files/boost/{version}/boost_{versionUnderscored}.tar.gz".format(
            version=version,
            versionUnderscored=version.replace(".", "_")
        ),
        []
    )


def _GetGLEWPackage(version):
    return SoftwarePackage(
        "glew",
        version,
        "https://downloads.sourceforge.net/project/glew/glew/{version}/glew-{version}.tgz".format(
            version=version,
        ),
        []
    )


def _GetTBBPackage(version):
    return SoftwarePackage(
        "glew",
        version,
        "https://github.com/01org/tbb/archive/{version}.tar.gz".format(
            version=version,
        ),
        []
    )


def _GetOpenSubdivPackage(version):
    return SoftwarePackage(
        "openexr",
        version,
        "https://github.com/PixarAnimationStudios/OpenSubdiv/archive/v{versionUnderscored}.zip".format(
            versionUnderscored=version.replace(".", "_"),
        ),
        ["glew"]
    )


_SOFTWARE_PACKAGE_LOOKUP = dict([
    ("gcc", _GetGccPackage),
    ("boost", _GetBoostPackage),
    ("glew", _GetGLEWPackage),
    ("tbb", _GetTBBPackage),
    ("opensubdiv", _GetOpenSubdivPackage),
])


def GetSoftwarePackage(name, version):
    getPackageFn = _SOFTWARE_PACKAGE_LOOKUP[name]
    return getPackageFn(version)
