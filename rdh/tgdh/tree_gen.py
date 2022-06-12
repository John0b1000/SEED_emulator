# file: tree_gen.py
#

from Tree import Tree
import sys

# determine the number of nodes
#
nodes = input("Enter the number of group members: ")
NUM_NODES = int(nodes)-1

# instantiate the Tree class
#
tree = Tree()

# add the proper number of members
#
print("")
print("Generating binary tree with " + nodes + " nodes ...\n")
for i in range(NUM_NODES):
   tree.insertNewUser()
    
# print the tree
#
print(tree)
