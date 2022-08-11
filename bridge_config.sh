#!/bin/bash

# Configure the Linux bridges
#
NIC1=$(ip -br addr | grep -vE 'veth|br' | grep enp | cut -d' ' -f1)
echo "Configuring bridge for interface $NIC1 ..."
BR1=$(ip -br addr show to 10.150.0.0/24 | cut -d' ' -f1)
sudo ip link set $NIC1 master $BR1
ip -br link show master $BR1
sleep 2
NIC2=$(ip -br addr | grep -vE 'veth|br' | grep enx | cut -d' ' -f1)
echo "Configuring bridge for interface $NIC2 ..."
BR2=$(ip -br addr show to 10.152.0.0/24 | cut -d' ' -f1)
sudo ip link set $NIC2 master $BR2
ip -br link show master $BR2
#
# end script

