class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        
def printPostorder(root):
 
    if root:
 
        # First recur on left child
        printPostorder(root.left)
 
        # the recur on right child
        printPostorder(root.right)
 
        # now print the data of node
        print(root.val)

root = Node("K")
root.left = Node("A")
root.right = Node("H")
root.left.left = Node("E")
root.right.left = Node("F")
root.right.right = Node("D")
root.right.right.right = Node("G")
root.left.right = Node("C")
root.right.right.right.left = Node("B")
 

printPostorder(root)