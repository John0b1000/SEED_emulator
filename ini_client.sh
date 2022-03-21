#!/bin/bash

# file: ini_client.sh
#

# this file sends a message from the client
#

# start the client and send the message
#
cd rsa-diffie-hellman
python3 client.py $1 $2

#
# end of file
