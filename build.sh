#!/usr/bin/env bash 

# first go into the src folder
cd src/python_uarch_bench

cd deps/uarch-bench
cd libpfm4 
git checkout origin master 
cd ..
make
cd ../..

# go back to the main dir
cd ../..
