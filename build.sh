#!/usr/bin/env bash 
cd deps/uarch-bench
cd libpfm4 
git checkout origin master 
cd ..
make
cd ../..
