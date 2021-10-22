def check_heap(tree_root):
    if tree_root==None:
        return False
    
    if tree_root.left==None and tree_root.right==None:
        return True
    
    if tree_root.left!=None and tree_root.right!=None:
        return check_heap(tree_root.left) and check_heap(tree_root.right)
    
    return False