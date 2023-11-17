#!/bin/sh
cd -
cd "./tcp_override"
make
make rm
make ins
cd -