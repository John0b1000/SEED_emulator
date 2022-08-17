# file: run_ns.py
#
'''This file creates a shared nameserver.'''


# import modules
#
import sys
import os
import time
from osbrain import config, run_nameserver, NameServer

# function: main
#
def main(argv):
    '''This is the main function.'''

    # set TCP as the default transport protocol
    #
    config['TRANSPORT'] = 'tcp'
    
    # create the nameserver
    #
    nameserver = run_nameserver(argv[1])

    while len(nameserver.agents()) < 2:
        time.sleep(5)
        print("Agents registered in the nameserver:")
        for alias in nameserver.agents():
            print(f'>> {alias}')
    
    print("All agents registed with the nameserver!")

    print("The nameserver will close in 2 minutes ...")
    time.sleep(60)
    print("The nameserver will close in 1 minute ...")
    time.sleep(30)
    print("The nameserver will close in 30 seconds ...")
    time.sleep(20)
    for i in range(10, 0, -1):
        print(f"Nameserver closing in {i} seconds")
        time.sleep(1)

    # shutdown the nameserver
    #
    nameserver.shutdown()

    # clean up the directory
    #
    os.system("rm *.crt *.pem")
#
# end function: main

# begin gracefully
#
if __name__ == "__main__":
    main(sys.argv)

#
# end file: run_ns.py