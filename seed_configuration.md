# Creating a VLAN with SEED Emulator
# OS: Ubuntu 20.04


## Set up a VLAN on TP Link Switch

1. Plug switch into SEED host PC and assign static IP: 192.168.0.2, 255.255.0.0, 192.168.0.1
2. Configure 802.1Q VLAN at TP Link web GUI: https://192.168.0.1

## Run the SEED Emulator

3. Run example: C03-bring-your-own-internet
   The web client with start automatically
   
## Configure Linux Bridge

4. Find the physical NIC for the ethernet port: ip -br addr | grep -vE 'veth|br'
5. Find the name of the Linux bridge for AS-151 net0: ip -br addr show to 10.151.0.0/24
6. Add the physical interface to the Linux bridge: sudo ip link set <physical_NIC> master <bridge_name>
7. List all interfaces connected to the bridge: ip -br link show master <bridge name>

## Configure SSH on SEED Devices

8. Uncomment and change the following line in /etc/ssh/sshd_config: PermitRootLogin yes
9. Change the root password: passwd root
			      12340987

