from Crypto.Random.random import randint
from Crypto.Util import number
class Node(object):
    g = 2
    p = number.getPrime(2048)
    def __init__(self,id,tree):
        self.id = id
        self.key = randint(1,int(Node.p-1))
        self.bKey = pow(Node.g,self.key,Node.p)
        self.isLeaf = True
        self.tree = tree
    def left(self):
        return self.tree.left(self)
    def right(self):
        return self.tree.right(self)
    def isLeftChild(self):
        return self.parent().left()==self
    def isRightChild(self):
        return self.parent().right()==self
    def parent(self):
        return self.tree.parent(self)
    def setLeft(self,node):
        self.tree.setLeft(self,node)
    def setRight(self,node):
        self.tree.setRight(self,node)
    def setParent(self,node):
        self.tree.setParent(self,node)
    def copyDataFrom(self,source, resetSource = True):
        self.key = source.key
        self.bKey = source.bKey
        if(resetSource):
            source.key = 0
            source.bKey = 0
    def recalculateKeyPath(self):
        curNode = self
        while(1):
            if(not curNode.isLeaf):
                curNode.key = pow(curNode.right().bKey,curNode.left().key,Node.p)
                curNode.bKey = pow(Node.g,curNode.key,Node.p)
            
            parNode = curNode.parent()
            if(parNode==curNode):
                return 
            else:
                curNode=parNode
    def verifyIntegrity(self):
        if self.isLeaf :
            
            if (self.left() is None and self.right() is None and self.verifyNodeIntegrity()):
                return True
            else:
                print("Broken leaf node in tree at id =  ",self.id)
                return False
        else:
            
            if (self.left().verifyIntegrity() and self.right().verifyIntegrity()) and self.verifyNodeIntegrity() and (self.left() is not None and self.right() is not None):
                return True
            print("Broken tree at id =  ",self.id)
            return False
    def verifyNodeIntegrity(self):
        if self.bKey == pow(Node.g,self.key,Node.p):
            return True
        print("Broken node at id = ",self.id)
        return False
    def recursivePrint(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right() is None and self.left() is None:
            line = '%s' % self.id
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right() is None :
            lines, n, p, x = self.left().recursivePrint()
            s = '%s' % self.id
            u = len(s)
            firstLine = (x + 1) * ' ' + (n - x - 1) * '_' + s
            secondLine = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [firstLine, secondLine] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left() is None :
            lines, n, p, x = self.right().recursivePrint()
            s = '%s' % self.id
            u = len(s)
            firstLine = s + x * '_' + (n - x) * ' '
            secondLine = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [firstLine, secondLine] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left().recursivePrint()
        right, m, q, y = self.right().recursivePrint()
        s = '%s' % self.id
        u = len(s)
        firstLine = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        secondLine = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [firstLine, secondLine] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2