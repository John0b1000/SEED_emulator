#!/bin/zsh

# file: tcp_write_tool.sh
#

# This script runs the tcpdump command to capture network traffic.
# A binary file containing the data is written.
#

# run the tcpdump command (sudo privilege required)
#
sudo tcpdump -i any -c32 -w $1 port 9000

#
# end of file
