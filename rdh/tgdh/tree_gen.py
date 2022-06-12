# file: tree_gen.py
#

from Tree import Tree
import sys

# determine the number of nodes
#
NUM_NODES = int(sys.argv[1])-1

# instantiate the Tree class
#
tree = Tree()

# add the proper number of members
#
print("")
print("Generating binary tree with " + sys.argv[1] + " nodes ...\n")
for i in range(NUM_NODES):
   tree.insertNewUser()
    
# print the tree
#
print(tree)
