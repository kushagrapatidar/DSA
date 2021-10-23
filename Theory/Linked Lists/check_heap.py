#Function to check if a tree is perfect or not
def isperfect(tree_root):
    from binary_tree_height import find_height_ll
    max_height,min_height=find_height_ll(tree_root)
    
    val=(max_height==min_height)
    if val:
        print("Perfect Tree")
    else:
        print("Not Perfect Tree")

#Function to check if the tree is full or not
def isfull(tree_root):
    if tree_root==None:
        return False
    
    if tree_root.left==None and tree_root.right==None:
        return True
    
    if tree_root.left!=None and tree_root.right!=None:
        return (isfull(tree_root.left) and isfull(tree_root.right))
    
    return False
