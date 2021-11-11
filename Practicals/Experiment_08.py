class TreeNode:
    data=None
    right=None
    left=None

def insert(key,root=None):
    if root==None:
        root=TreeNode()
        root.data=key
        return root
    else:
        if root.data==key:
            return root
        elif root.data<key:
            root.right=insert(key,root.right)
        else:
            root.left=insert(key,root.left)
    return root

def printBST_incr(root):
    if root:
        printBST_incr(root.left)
        print(root.data)
        printBST_incr(root.right)

n=int(input('Enter the number of nodes: '))
r=None
for i in range(n):
    if r==None:
        r=insert(int(input('Enter Node data: ')))
    else:
        insert(int(input('Enter Node data: ')),r)
print('\n')
printBST_incr(r)
#Test Case
    # r=insert(50)
    # insert(30,r)
    # insert(20,r)
    # insert(40,r)
    # insert(70,r)
    # insert(60,r)
    # insert(80,r)

