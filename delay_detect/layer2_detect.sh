#!/bin/sh
# Function to handle SIGINT signal
cleanup() {
    echo "Caught SIGINT, cleaning up..."
    
    # Kill all background processes
    kill 0
    
    # Exit the script
    exit 1
}

cd -
# Trap SIGINT and call the cleanup function
trap cleanup SIGINT
./delay_detect/packet_capture > "./temp_json/layer2_logs.txt" 
cd -