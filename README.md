# VFXBuild

Build and installation recipes for a collection of open-source software commonly used in VFX.

A lot of the procedures are copied from `build_scripts/build_usd.py` which is shipped with [USD](https://github.com/PixarAnimationStudios).

These scripts have only been tested on Linux.

Source code will be downloaded to `/tmp` to be built.

## Example Usages

```bash
./installBoost.sh -v 1.61.0 /apps/boost/1.61.0
./installGLEW.sh -v 2.0.0 /apps/glew/2.0.0
./installTBB.sh -v 4.4.6 /apps/tbb/4.4.6
./installOpenSubdiv.py --glew-location /apps/glew/2.0.0/ --version 3.1.1 /apps/opensubdiv/3.1.1
./installUSD.py --glew-location /apps/glew/2.0.0/ --tbb-location /apps/tbb/4.4.6/ --boost-location /apps/boost/1.61.0/ --opensubdiv-location /apps/opensubdiv/3.1.1/ -v 20.02 /apps/usd/20.02
```

## Pre-requisites

- `curl`


## Todo

- Single installation entry point.
- VFX Platform support.
- Option to choose GCC compiler version and dependencies.
- Support for MacOS and Windows.
