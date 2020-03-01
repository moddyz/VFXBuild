# VFXBuild

Build and installation recipes for a collection of open-source software commonly used in VFX.

A lot of the procedures are copied from `build_scripts/build_usd.py` which is shipped with [USD](https://github.com/PixarAnimationStudios).

These scripts have only been tested on Linux.

Source code will be downloaded to `/tmp` to be built.

## Example Usage

```bash
./installBoost.py -v 1.61.0 /apps/boost/1.61.0
./installGLEW.py -v 2.0.0 /apps/glew/2.0.0
./installTBB.py -v 4.4.6 /apps/tbb/4.4.6
./installOpenSubdiv.py --glew-location /apps/glew/2.0.0/ --version 3.1.1 /apps/opensubdiv/3.1.1
./installUSD.py --glew-location /apps/glew/2.0.0/ --tbb-location /apps/tbb/4.4.6/ --boost-location /apps/boost/1.61.0/ --opensubdiv-location /apps/opensubdiv/3.1.1/ -v 20.02 /apps/usd/20.02
```

## Pre-requisites

- `curl`


## To Do

- VFX platform support.
- Support for MacOS and Windows.
- Automated testing.
