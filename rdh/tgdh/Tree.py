"""
class tree
each leaf node would have copy of the tree
each copy has different public and private vars
tree functions :
add node              ]
delete node           ] - Basic functions

merge subtree
remove subtree
assign groups

"""

""" 

Simplifications made on 5/25/21
Focus on Join Protocol
Remove plotting capabilities

"""

from Node import Node
from collections import deque
class Tree(object):
    def __init__(self,maxSize = 30000):
        self.root = Node(0,self)
        self.array = [self.root] + list([None]*(2*maxSize+10))
        self.nodeCount = 1
        self.queue = deque()
        self.queue.append(self.root)
    def left(self,node):
        x =  self.array[2*node.id + 1]
        return x
    def right(self,node):
        x =  self.array[2*node.id + 2]
        return x
    def parent(self,node):
        if(node.id==0):
            x =  node
        else:
            x =  self.array[((node.id)-1)//2]
        return x 
    def setLeft(self,x,target):
        self.array[2*x.id + 1] = target
    def setRight(self,x,target):
        self.array[2*x.id + 2] = target
    def setParent(self,x,target):
        if(x.id==0):
            return 
        self.array[(x.id-1)//2] = target
    def setLeaf(self,x):
        self.setLeft(x,None)
        self.setRight(x,None)
        x.isLeaf=True
    def findSponsor(self):
        front = self.queue[0]
        self.queue.popleft()
        return front
    def createNode(self):
        newNode = Node(self.nodeCount,self)
        self.nodeCount+=1
        return newNode
    def insertNewUser(self):
        sponsor = self.findSponsor()
        leftNewNode = self.createNode()
        self.queue.append(leftNewNode)
        rightNewNode = self.createNode()
        self.queue.append(rightNewNode)
        self.setParent(leftNewNode,sponsor)
        self.setParent(rightNewNode,sponsor)
        leftNewNode.copyDataFrom(sponsor)
        sponsor.isLeaf = False
        self.setLeft(sponsor,leftNewNode)
        self.setRight(sponsor,rightNewNode)
        sponsor.recalculateKeyPath()
    def verifyTreeIntegrity(self):
        return self.root.verifyIntegrity()
    def __str__(self):
        output =""
        lines, *_ = self.root.recursivePrint()
        for line in lines:
            output+=line
            output+='\n'
        return output
