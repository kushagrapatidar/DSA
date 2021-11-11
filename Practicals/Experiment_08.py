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

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

r = insert(50)
r = insert(30,r)
r = insert(20,r)
r = insert(40,r)
r = insert(70,r)
r = insert(60,r)
r = insert(80,r)