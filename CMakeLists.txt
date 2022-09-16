cmake_minimum_required(VERSION 3.15)

project(offline)
set(CMAKE_CXX_STANDARD 17 CACHE STRING "")

find_package(junosw)
include(PKG)

add_subdirectory(ExamplePyAlg)

include(JUNOSetupScripts)
include(JUNOInstallOfflineSetup)
