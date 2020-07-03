# VFXBuild

Build and installation recipes for a collection of open-source software commonly used in VFX.

Much of the procedures are originally referenced from `build_scripts/build_usd.py` which is shipped with [USD](https://github.com/PixarAnimationStudios).  Thanks!

## Table of Contents

- [Usage](#usage)
- [Requirements](#requirements)
- [Build Status](#build-status)
- [Planned work](#planned-work)

## Usage

The installation scripts are intended to be run from the root of the locally cloned repository.

These scripts have only been tested on Linux.  Source code will be downloaded to `/tmp` to be built.

```bash
./installBoost.py --version 1.61.0 /apps/boost/1.61.0
./installGLEW.py --version 2.0.0 /apps/glew/2.0.0
./installTBB.py --version 2017_U7 /apps/tbb/2017_U7
./installBlosc.py --version 1.17.1 /apps/blosc/1.17.1
./installOpenEXR.py --version 2.4.1 /apps/openexr/2.4.1
./installGLFW.py --version 3.3.2 /apps/glfw/3.3.2

./installOpenSubdiv.py \
    --version 3.1.1 \
    --glew-location /apps/glew/2.0.0/ \
    /apps/opensubdiv/3.1.1

./installOpenVDB.py \
    --version 7.0.0 \
    --boost-location /apps/boost/1.61.0/ \
    --tbb-location /apps/tbb/2017_U7/ \
    --openexr-location /apps/openexr/2.4.1/ \
    --blosc-location /apps/blosc/1.17.1/ \
    --glfw-location /apps/glfw/3.3.2/ \
    /apps/openvdb/7.0.0

./installUSD.py \
    --version 20.05 \
    --glew-location /apps/glew/2.0.0/ \
    --tbb-location /apps/tbb/2017_U7/ \
    --boost-location /apps/boost/1.61.0/ \
    --opensubdiv-location /apps/opensubdiv/3.1.1/ \
    /apps/usd/20.05

./installOpenImageIO.py \
    --version 2.1.12.0 \
    --boost-location /apps/boost/1.61.0/ \
    --openexr-location /apps/openexr/2.4.1/ \
    /apps/openimageio/2.1.12.0
```


## Requirements

Base requirements:
- `curl`

Extra per-software requirements may need to be installed, for example:
- `CMake >=-3.10` (for CMake-based projects)
- `jinja2` (for USD)
- `doxygen` and `graphviz` for building documentation.

## Build Status

|       | master | 
| ----- | ------ | 
|Ubuntu-18.04 | [![Build Status](https://travis-ci.com/moddyz/VFXBuild.svg?branch=master)](https://travis-ci.com/moddyz/VFXBuild) |


## Planned work

- Support for MacOS.
- Support for Windows.
