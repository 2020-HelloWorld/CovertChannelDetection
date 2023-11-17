#!/bin/sh
cd "./tcp_override"
make rm
# make clean

cd "../ttl_prevent"
make rm
# make clean

rm -rf temp_json