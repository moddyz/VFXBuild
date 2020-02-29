# VFXBuild

Build and installation recipes for a collection of open-source VFX software.

These scripts have only been tested on Linux.

Source code will be downloaded to `/tmp` to be built.

## Example usages

```bash
./installBoost.sh -v 1.55.0 /apps/boost/1.55.0
./installGLEW.sh -v 2.0.0 /apps/glew/2.0.0
./installTBB.sh -v 4.4.6 /apps/tbb/4.4.6
```

## TODO

- Single installation entry point.
- VFX Platform support.

## Pre-requisites

- `curl`
