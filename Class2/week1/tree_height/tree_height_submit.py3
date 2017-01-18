import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class TreeHeight:
        def __init__(self):
            self.tree = None
    
        def read(self):
            n = int(sys.stdin.readline())
            parent = list(map(int, sys.stdin.readline().split()))
            self._createTree(parent)
    
        def build_tree(self, parent):
            self._createTree(parent)
    
        def _createNode(self, parent, i, created, root):
 
            # If this node is already created
            if created[i] is not None:
                return

            # Create a new node and set created[i]
            created[i] = Node(i)

            # If 'i' is root, change root pointer and return
            if parent[i] == -1:
                root[0] = created[i] # root[0] denotes root of the tree
                return

            # If parent is not created, then create parent first
            if created[parent[i]] is None:
                self._createNode(parent, parent[i], created, root )

            # Find parent pointer
            p = created[parent[i]]

            # If this is first child of parent
            if p.left is None:
                p.left = created[i]
            # If second child
            else:
                p.right = created[i]


        # Creates tree from parent[0..n-1] and returns root of the
        # created tree
        def _createTree(self, parent):
            n = len(parent)

            created = [None for i in range(n+1)]

            root = [None]
            for i in range(n):
                self._createNode(parent, i, created, root)

            self.tree = root[0]
        
        
        def _count_depth(self, tree):
            if not self.tree:
                return 0
            left_depth = self._count_depth(self.tree.left)
            right_depth = self._count_depth(self.tree.right)
            if left_depth>right_depth:
                return 1+left_depth
            else:
                return 1+right_depth
             
        def compute_height(self):
            if not self.tree:
                return 1
            else:
                return self._count_depth(self.tree)

def main():
    #n = int(sys.stdin.readline())
    #parent = list(map(int, sys.stdin.readline().split()))
    print("here")
    #th = TreeHeight()
    #th.read()
    #print(th.compute_height())