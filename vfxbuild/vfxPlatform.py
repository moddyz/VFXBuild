"""
Tools to query VFX Platform specification.

https://vfxplatform.com/
"""

import collections

__all__ = [
    'GetVFXPlatform',
    'GetVFXPlatforms',
]

VFXPlatform = collections.namedtuple('VFXPlatform', ["year", "softwareVersions"])
SoftwareVersion = collections.namedtuple('SoftwareVersion', ["name", "version"])

_VFX_PLATFORMS = {}


def _DefineVFXPlatform(year):
    _VFX_PLATFORMS[year] = VFXPlatform(year, {})
    return _VFX_PLATFORMS[year]


def _AddToPlatform(vfxPlatform, softwareVersion):
    vfxPlatform.softwareVersions[softwareVersion.name] = softwareVersion


_vfx2014 = _DefineVFXPlatform("CY2014")
_AddToPlatform(_vfx2014, SoftwareVersion("gcc", "4.1.2"))
_AddToPlatform(_vfx2014, SoftwareVersion("python", "2.7.3"))
_AddToPlatform(_vfx2014, SoftwareVersion("qt", "4.8.5"))
_AddToPlatform(_vfx2014, SoftwareVersion("pyside", "1.2"))
_AddToPlatform(_vfx2014, SoftwareVersion("openexr", "2.0.1"))
_AddToPlatform(_vfx2014, SoftwareVersion("opensubdiv", "2.3.3"))
_AddToPlatform(_vfx2014, SoftwareVersion("alembic", "1.5.8"))
_AddToPlatform(_vfx2014, SoftwareVersion("fbx", "2015"))
_AddToPlatform(_vfx2014, SoftwareVersion("opencolorio", "1.0.7"))
_AddToPlatform(_vfx2014, SoftwareVersion("boost", "1.53.0"))
_AddToPlatform(_vfx2014, SoftwareVersion("tbb", "4.1"))

_vfx2015 = _DefineVFXPlatform("CY2015")
_AddToPlatform(_vfx2015, SoftwareVersion("gcc", "4.8.2"))
_AddToPlatform(_vfx2015, SoftwareVersion("glibc", "2.12"))
_AddToPlatform(_vfx2015, SoftwareVersion("python", "2.7.3"))
_AddToPlatform(_vfx2015, SoftwareVersion("qt", "4.8.5"))
_AddToPlatform(_vfx2015, SoftwareVersion("pyside", "1.2"))
_AddToPlatform(_vfx2015, SoftwareVersion("openexr", "2.2.0"))
_AddToPlatform(_vfx2015, SoftwareVersion("opensubdiv", "2.5.0"))
_AddToPlatform(_vfx2015, SoftwareVersion("openvdb", "3.0.0"))
_AddToPlatform(_vfx2015, SoftwareVersion("alembic", "1.5.8"))
_AddToPlatform(_vfx2015, SoftwareVersion("fbx", "latest"))
_AddToPlatform(_vfx2015, SoftwareVersion("opencolorio", "1.0.9"))
_AddToPlatform(_vfx2015, SoftwareVersion("boost", "1.55.0"))
_AddToPlatform(_vfx2015, SoftwareVersion("tbb", "4.2"))


def GetVFXPlatforms():
    """
    Returns:
        list: all the vfx platforms.
    """
    return _VFX_PLATFORMS.values()


def GetVFXPlatform(year):
    """
    Returns:
        list: all the vfx platforms.
    """
    return _VFX_PLATFORMS[year]
