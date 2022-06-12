# Usage on the SEED Emulator
The following sections demonstrate how to utilize the contents of this shared folder on the SEED emulator.
## I. Server-Client Communication (Diffie-Hellman, TCP)
Node A (server):
```
python3 server.py 
```
Node B (client):
```
python3 client.py <ip addr> "Hello world!"
```
## II. Tcpdump Scripts
Router:
```
./tcp_write_tool.sh <filename>.pcap
```
Now, run Section I. Traffic should travel through the router from Node A to Node B. 
To read the file containing the captured traffic:
```
./tcp_read_tool.sh <filename>.pcap
```
## III. Mulitcasting (UDP)
Node B (receiever):
```
python3 mucast_v2.py --mcast-group '224.1.1.2'
```
Node C (receiever):
```
python3 mucast_v2.py --mcast-group '224.1.1.2'
```
Node A (sender):
```
python3 mucast_v2.py --iface='<ip addr>' --join-mcast-groups '224.1.1.2' --bind-group '224.1.1.2' --type rec
```
Now, input messages to Node A for multicasting.
## IV. TGDH
Node A
```
python3 tree_gen.py <number of nodes>
