#!/bin/sh
cd -
cd "./tcp_override"
make rm
# make clean
cd -
cd "./ttl_prevent"
make rm
# make clean
cd -
rm -rf temp_json