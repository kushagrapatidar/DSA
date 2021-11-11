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

