def find_height(tree_head):
    left=right=tree_head
    max_height=min_height=0
    while left!=None or right!=None:
        if left!=None:
            max_height+=1
            left=left.left
        if right!=None:
            min_height+=1
            right=right.next
    return max_height,min_height