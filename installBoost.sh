#!/bin/bash

set -euxo pipefail

# Parse arguments.
if [ ! $# -eq 1 ]; then
    echo "./installBoost.sh <INSTALL_PREFIX>"
    exit 1
fi

APP_INSTALL_PREFIX=$1

# Early out if already installed.
if [ -d $APP_INSTALL_PREFIX ]; then
    echo "$APP_INSTALL_PREFIX already exists!" 
    exit 0
fi

# Create a staging directory to download source.
mkdir -p staging
cd staging

# Download source to staging dir.
URL="https://sourceforge.net/projects/boost/files/boost/1.61.0/boost_1_61_0.tar.gz"
FILE_NAME="boost_1_61_0.tar.gz"
if [ ! -f $FILE_NAME ]; then
    wget -O $FILE_NAME $URL
else
    echo "$FILE_NAME already exists!" 
fi

# Build!
mkdir -p build
tar -xvf $FILE_NAME
cd boost_1_61_0
./bootstrap.sh --prefix="$APP_INSTALL_PREFIX"
./b2 --prefix=$APP_INSTALL_PREFIX --build-dir=build -j8 address-model=64 link=shared runtime-link=shared threading=multi -a install
