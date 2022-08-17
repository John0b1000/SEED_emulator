# file: run_agent_receiver.py
#
'''This file creates a remote receiving agent on a distributed system.'''


# import modules
#
import sys
import os
import time
from osbrain import config, NSProxy, run_agent
from Pyro4 import errors
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# function: read_private_key
#
def read_private_key(file):
    print(f"Reading private key ...")
    with open(file, 'rb') as f:
        private_key_encode = load_pem_private_key(f.read(), None)
        private_key_decode = private_key_encode.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.TraditionalOpenSSL, encryption_algorithm=serialization.NoEncryption())
        if isinstance(private_key_encode, rsa.RSAPrivateKey):
            print(f"The private key is: \n{private_key_decode}")
    return private_key_encode
#
# end function: read_private_key

# function: get_private_key
#
def get_private_key(file, agent):
    os.system(f"sqlite3 {file} \"SELECT private FROM view_private WHERE name='{agent}'\" | base64 -d | openssl pkcs8 -inform DER > {agent}.pem")
#
# end function: get_private_key

# function: log_message
#
def reply(agent, message):
    '''This helper function handles text messages.'''

    time.sleep(1)
    agent.log_info(f'Received: {message}')
    if message != "Your certificate has been revokved.":
        get_private_key('seed_demo.xdb', 'UserA')
        private_key = read_private_key('UserA.pem')
        plaintext = private_key.decrypt(message,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
        print(f"Decrypted: {plaintext}")
    return('Message successfully received!')
#
# end function: log_message

# function: main
#
def main(argv):
    '''This is the main function.'''

    # set TCP as the default transport protocol
    #
    config['TRANSPORT'] = 'tcp'

    # connect to the nameserver
    #
    nameserver_addr = argv[2]
    nameserver_proxy = NSProxy(nsaddr=nameserver_addr)

    # create the remote agent
    #
    alias = argv[3]
    agent = run_agent(alias, nsaddr=nameserver_addr, addr=argv[1])
    agent.bind('REP', alias=alias, handler=reply)
    time.sleep(2)

    # receive a message
    #
    s_alias = argv[4]
    print(f"Waiting for message from {s_alias} ...")
    while True:
        try:
            nameserver_proxy.proxy(s_alias)
            print(f"Agent {s_alias} detected in nameserver!")
            time.sleep(1)
            break
        except errors.NamingError:
            time.sleep(1)

    # the nameserver will stop this program
    #
#
# end function: main

# begin gracefully
#
if __name__ == "__main__":
    main(sys.argv)

#
# end file: run_agent_receiver.py