#Function to check the validity of the given heap as perfect or not
def check_heap(tree_root):
    left=tree_root.left
    right=tree_root.right

    if left.left!=None and left.right!=None and right.left!=None and right.right!=None:
        if tree_root==None:
            return False
    
        if left==None and right==None:
            return True
    
        if left!=None and right!=None:
            return (check_heap(left) and check_heap(right))
    
    return False