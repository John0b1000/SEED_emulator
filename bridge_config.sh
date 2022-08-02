#!/bin/bash

# Configure the Linux bridge
#
NIC=$(ip -br addr | grep -vE 'veth|br' | grep UP | cut -d' ' -f1)
BR=$(ip -br addr show to 10.151.0.0/24 | cut -d' ' -f1)
sudo ip link set $NIC master $BR
ip -br link show master $BR

#
# end script

