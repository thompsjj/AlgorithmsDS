# python3

import sys, threading
from collections import deque
from copy import copy

class Node:
    def __init__(self, key):
        self.key = key
        self.children = []

class TreeHeight:
        
    def __init__(self):
        self.tree = None
   
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.tree = self._build_tree(self.parent)
        
    def _build_tree(self, parents):
        N = len(parents)
        nodes = [Node(i) for i in range(N)]
        for c in range(N):
            if parents[c] == -1:
                root = nodes[c]
            else:
                nodes[parents[c]].children.append(nodes[c])

        return root
        
    def compute_height(self):
        
        # recursion over list-tree
        root = copy(self.tree)
        Q = deque()
        Q.append(root)
        height = 0
        
        while True:
            
            nodeCount = len(Q)
            if not nodeCount:
                return height
            else:
                height +=1 
            
            while nodeCount > 0:
                currentNode = Q.popleft()
                for c in currentNode.children:
                    Q.append(c)
                
                nodeCount -= 1

def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())

main()