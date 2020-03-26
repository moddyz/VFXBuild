# VFXBuild

Build and installation recipes for a collection of open-source software commonly used in VFX.

A lot of the procedures are copied from `build_scripts/build_usd.py` which is shipped with [USD](https://github.com/PixarAnimationStudios).

These scripts have only been tested on Linux.

Source code will be downloaded to `/tmp` to be built.

## Example Usage

```bash
./installBoost.py -v 1.61.0 /apps/boost/1.61.0
./installGLEW.py -v 2.0.0 /apps/glew/2.0.0
./installTBB.py -v 2017_U7 /apps/tbb/2017_U7
./installBlosc.py -v 1.17.1 /apps/blosc/1.17.1
./installOpenEXR.py -v 2.4.1 /apps/openexr/2.4.1
./installGLFW.py --version 3.3.2 /apps/glfw/3.3.2

./installOpenSubdiv.py --version 3.1.1 \
    --glew-location /apps/glew/2.0.0/ \
    /apps/opensubdiv/3.1.1

./installOpenVDB.py --version 7.0.0 \
    --boost-location /apps/boost/1.61.0/ \
    --tbb-location /apps/tbb/2017_U7/ \
    --openexr-location /apps/openexr/2.4.1/ \
    --blosc-location /apps/blosc/1.17.1/ \
    --glfw-location /apps/glfw/3.3.2/ \
    /apps/openvdb/7.0.0

./installUSD.py \
    --version 20.02 \
    --glew-location /apps/glew/2.0.0/ \
    --tbb-location /apps/tbb/2017_U7/ \
    --boost-location /apps/boost/1.61.0/ \
    --opensubdiv-location /apps/opensubdiv/3.1.1/ \
    -v 20.02 /apps/usd/20.02
```

## Pre-requisites

- `curl`


## To Do

- VFX platform support.
- Support for MacOS and Windows.
- Automated testing.
