"""
Tools to query software packages.
"""

__all__ = [
    'GetGccPackage',
    'GetBoostPackage',
]

import collections

SoftwarePackage = collections.namedtuple('SoftwarePackage', ['name', 'version', 'sourceLocation', 'sourceType'])

#
# Software packages.
#

def GetGccPackage(version):
    return SoftwarePackage(
        "gcc",
        version,
        "ftp://ftp.gnu.org/gnu/gcc/gcc-{version}/gcc-{version}.tar.gz".format(
            version=version
        ),
        "url",
    )


def GetBoostPackage(version):
    return SoftwarePackage(
        "boost",
        version,
        "https://sourceforge.net/projects/boost/files/boost/{version}/boost_{versionUnderscored}.tar.gz".format(
            version=version,
            versionUnderscored=version.replace(".", "_")
        ),
        "url",
    )
