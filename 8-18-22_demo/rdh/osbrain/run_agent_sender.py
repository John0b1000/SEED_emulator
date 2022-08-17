# file: run_agent_sender.py
#
'''This file creates a remote sending agent on a distributed system.'''


# import modules
#
import sys
import os
import time
from osbrain import config, NSProxy, run_agent
from cryptography.hazmat.primitives import serialization
from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# function: get_crl
#
def get_crl(file):
    with open(file, 'rb') as f:
        crl = x509.load_pem_x509_crl(f.read())
        return crl
#
# end function: get_crl

# function: get_cert
#
def get_cert(file):
    with open(file, 'rb') as f:
       cert = x509.load_pem_x509_certificate(f.read())
       return cert
#
# end function: get_cert

# function: get_crl_file
#
def get_crl_file(file):
    os.system(f"sqlite3 {file} \"SELECT crl FROM view_crls WHERE name='LabCA-intermediate'\" | base64 -d | openssl crl -inform DER -out LabCA-intermediate.pem")
#
# end function: get_crl_file

# function: get_cert_file
#
def get_cert_file(file, agent):
    os.system(f"sqlite3 {file} \"SELECT cert FROM view_certs WHERE name='{agent}'\" | base64 -d | openssl x509 -inform DER -out {agent}.crt")
#
# end function: get_cert_file 

# function: verify
#
def verify(crl, cert):
    if crl.get_revoked_certificate_by_serial_number(cert.serial_number) is not None:
        return False
    else:
        return True
#
# end function: verify

# function: read_public_key
#
def read_public_key(cert):
    public_key_encode = cert.public_key()
    public_key_decode = public_key_encode.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)
    if isinstance(public_key_encode, rsa.RSAPublicKey):
        print(f"The public key is: \n{public_key_decode}")
    return public_key_encode
#
# end function: read_public_key

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
    # the publishing alias will be the same as the agent alias
    #
    alias = argv[3]
    agent = run_agent(alias, nsaddr=nameserver_addr, addr=argv[1])
    time.sleep(2)

    # get receiver info
    #
    r_alias = argv[4]
    r_agent = nameserver_proxy.proxy(r_alias)
    r_addr = r_agent.addr(r_alias)
    agent.connect(r_addr, alias=r_alias)
    print(f"Connected to agent {r_alias}!")

    # enter the message
    #
    message = input("Enter message here: ")

    # ensure that the certificate has not been revoked
    #
    get_crl_file('seed_demo.xdb')
    get_cert_file('seed_demo.xdb', 'UserA')
    crl = get_crl('LabCA-intermediate.pem')
    cert = get_cert('UserA.crt')
    if verify(crl, cert):
        public_key = read_public_key(cert)
        ciphertext = public_key.encrypt(bytes(message, encoding='utf-8'), padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
    else:
        print(f"The certificate of {r_alias} has been revoked")
        ciphertext =  "Your certificate has been revokved."
    print(f"Sending message to {r_alias} ...")
    agent.send(r_alias, ciphertext)
    reply = agent.recv(r_alias)
    print(f"Reply received: {reply}")

    # the nameserver will stop this program
    #
#
# end function: main

# begin gracefully
#
if __name__ == "__main__":
    main(sys.argv)

#
# end file: run_agent_sender.py