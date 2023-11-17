#!/bin/sh
cd -
python3 ./delay_detect/process_flows.py
cd -
python3 ./delay_detect/flow_capture.py
cd -