"""
    Trees
"""

class Node(object):
    def __init__(self):
        self.data = None
        self.lChild = None
        self.rChild = None

    # adding children
    def add(self, node):
        if (not self.lChild):
            self.lChild = node
        elif(not self.rChild):
            self.rChild = node
        else:
            print("Can't add more than two children.")

rootNode = Node(0)





