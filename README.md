# VFXBuild

Build and installation recipes for a collection of open-source VFX software.  

A lot of the procedures are simply copied from `build_scripts/build_usd.py` which is shipped with [USD](https://github.com/PixarAnimationStudios).

These scripts have only been tested on Linux.

Source code will be downloaded to `/tmp` to be built.

## Example usages

```bash
./installBoost.sh -v 1.55.0 /apps/boost/1.55.0
./installGLEW.sh -v 2.0.0 /apps/glew/2.0.0
./installTBB.sh -v 4.4.6 /apps/tbb/4.4.6
```

## Pre-requisites

- `curl`


## Motivation

Offer a simple way to build & install different versions of common software used in VFX.  

Not intended to be a full-on software management solution - mainly for the convenience of a home user.


## TODO

- Single installation entry point.
- VFX Platform support.
- Option to choose GCC compiler version and dependencies.
- Support for MacOS and Windows.
