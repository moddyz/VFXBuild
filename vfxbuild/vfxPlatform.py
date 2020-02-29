"""
Tools to query VFX Platform specification.

https://vfxplatform.com/
"""

import collections
from softwarePackage import *

__all__ = [
    'GetVFXPlatform',
    'GetVFXPlatforms',
]

VFXPlatform = collections.namedtuple('VFXPlatform', ['year', 'packages'])
_VFX_PLATFORMS = {}


def _DefineVFXPlatform(year):
    _VFX_PLATFORMS[year] = VFXPlatform(year, {})
    return _VFX_PLATFORMS[year]


def _AddVFXPackage(vfxPlatform, softwarePackage):
    vfxPlatform.packages[softwarePackage.name] = softwarePackage


_vfx2014 = _DefineVFXPlatform("CY2014")
_AddVFXPackage(_vfx2014, _GetGccPackage("4.1.2")
_AddVFXPackage(_vfx2014, _GetBoostPackage("1.53.0")


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
