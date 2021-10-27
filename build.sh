#!/bin/bash
prefix=$(pwd)/InstallArea
cmake -S . -B build -DCMAKE_INSTALL_PREFIX=$prefix || exit -1
cmake --build build || exit -1
cmake --install build || exit -1

