#!/bin/bash

set -euxo pipefail

if [ "$#" -ne 1 ]; then
    echo "usage: installAll.sh <APP_INSTALL_PREFIX>"
    exit 1
fi

export APP_INSTALL_PREFIX=$1

./installBoost.py --version 1.61.0 ${APP_INSTALL_PREFIX}/boost/1.61.0
./installGLEW.py --version 2.0.0 ${APP_INSTALL_PREFIX}/glew/2.0.0
./installTBB.py --version 2017_U7 ${APP_INSTALL_PREFIX}/tbb/2017_U7
./installBlosc.py --version 1.17.1 ${APP_INSTALL_PREFIX}/blosc/1.17.1
./installOpenEXR.py --version 2.4.1 ${APP_INSTALL_PREFIX}/openexr/2.4.1
./installGLFW.py --version 3.3.2 ${APP_INSTALL_PREFIX}/glfw/3.3.2

./installOpenSubdiv.py \
    --version 3.1.1 \
    --glew-location ${APP_INSTALL_PREFIX}/glew/2.0.0/ \
    ${APP_INSTALL_PREFIX}/opensubdiv/3.1.1

./installOpenVDB.py \
    --version 7.0.0 \
    --boost-location ${APP_INSTALL_PREFIX}/boost/1.61.0/ \
    --tbb-location ${APP_INSTALL_PREFIX}/tbb/2017_U7/ \
    --openexr-location ${APP_INSTALL_PREFIX}/openexr/2.4.1/ \
    --blosc-location ${APP_INSTALL_PREFIX}/blosc/1.17.1/ \
    --glfw-location ${APP_INSTALL_PREFIX}/glfw/3.3.2/ \
    ${APP_INSTALL_PREFIX}/openvdb/7.0.0

./installUSD.py \
    --version 20.02 \
    --glew-location ${APP_INSTALL_PREFIX}/glew/2.0.0/ \
    --tbb-location ${APP_INSTALL_PREFIX}/tbb/2017_U7/ \
    --boost-location ${APP_INSTALL_PREFIX}/boost/1.61.0/ \
    --opensubdiv-location ${APP_INSTALL_PREFIX}/opensubdiv/3.1.1/ \
    ${APP_INSTALL_PREFIX}/usd/20.02
