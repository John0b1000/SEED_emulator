# SEED Emulator Demonstration (6-13-22)
The following sections demonstrate how to utilize the contents of this shared folder on the SEED emulator. This file is a sequence of commands to be executed in order.
## I. Server-Client Communication (Diffie-Hellman, TCP)
Soldier 4 (server):
```
cd /rdh/sc_comm
```
```
python3 server.py 
```
Router 150 (client-side router)
```
cd /rdh/sc_comm
```
```
./tcp_write_tool.sh traffic.pcap
```
Soldier 1 (client):
```
cd /rdh/sc_comm
```
```
python3 client.py 10.151.0.72
```
```
>> hello4
```
*Run this command again to show same message with different encryption.*

Router 150 (client-side router)
```
./tcp_read_tool.sh traffic.pcap
```
## II. Multicasting (UDP)
Soldier 2 (receiever):
```
cd /rdh/multicast
```
```
python3 mucast_v2.py --iface='10.150.0.73' --join-mcast-groups '224.1.1.1' '224.1.1.2' '224.1.1.3' --bind-group '224.1.1.2' --type rec
```
Soldier 3 (receiever):
```
cd /rdh/multicast
```
```
python3 mucast_v2.py --iface='10.150.0.74' --join-mcast-groups '224.1.1.1' '224.1.1.2' '224.1.1.3' --bind-group '224.1.1.2' --type rec
```
Soldier 1 (sender):
```
cd /rdh/multicast
```
```
python3 mucast_v2.py --mcast-group '224.1.1.2'
```
```
>> Hello, everyone!
```
```
>> This is a test message!
```
*Change	one of the receiving groups to show that messages will not go through.*

## III. TGDH
Soldier 1
```
tmux
```
```
Keystroke: C-b "
```
```
Keystroke: C-b o
```
```
top
```
```
Keystroke: C-b o
```
```
cd /rdh/tgdh
```
```
python3 tree_gen.py
```
```
>> 4
```
```
>> 7
```
```
>> 10
```
```
>> 20
```
```
>> 30
```
