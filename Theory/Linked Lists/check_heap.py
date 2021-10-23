def isperfect(tree_root):
    from binary_tree_height import find_height_ll
    max_height,min_height=find_height_ll(tree_root)
    
    val=(max_height==min_height)
    if val:
        print("Perfect")
    else:
        print("Not Perfect")