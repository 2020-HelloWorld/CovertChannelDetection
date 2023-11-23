#!/bin/bash
cd delay_detect
make
cd ..

cd delay_queue
make 
cd ..

cd tcp_override
make
cd ..

cd ttl_detect
make 
cd ..

cd ttl_prevent
make 
cd ..

