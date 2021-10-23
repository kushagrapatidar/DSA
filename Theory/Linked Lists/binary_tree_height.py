#Height of a Binary Tree(Linked List)
def find_height_ll(tree_root):
    left=right=tree_root
    max_height=min_height=-1       
    while left!=None or right!=None:
        if left!=None:
            max_height+=1
            left=left.left
        if right!=None:
            min_height+=1
            right=right.right

    if max_height==-1:
        return -1,-1
    else:
        return max_height,min_height

#Height of a Binary Tree(List)
def find_height_lst(lst):
    max_height=min_height=-1
    for i,j in range(len(lst)//2):
        if 2*i+1<len(lst):
            max_height+=1
            i=2*i+1
        if 2*j+2<len(lst):
            min_height+=1
            j=2*j+2
    if len(lst)==1:
        min_height=max_height

    if max_height==-1:
        return -1,-1
    else:
        return max_height,min_height
