# 7-20-22 Commands

**Run tcpdump on router 150 node**
```
tcpdump -i any -w data.pcap  
```
**Run the nameserver on soldier 1**
```
python3 run_ns.py 10.152.0.71:9090
```
**Run the receiver on soldier 4**
```
python3 run_agent_receiver.py 10.151.0.72:9090 10.152.0.71:9090 soldier4 soldier2
```
**Run the sender on soldier 2**
```
python3 run_agent_sender.py 10.150.0.73:9090 10.152.0.71:9090 soldier2 soldier4
```
**Send the message from soldier 2 to soldier 4**
```
Hello, this is a test message!
```
**Show contents of tcpdump**
```
tcpdump -qns 0 -X -r data.pcap | grep Hello -A 2 -B 5
```
