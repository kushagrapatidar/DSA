def find_height(arr,height,i=0):
    if 2*i+1<len(arr):
        height+=1
        i=2*i+1
        height=find_height(arr,height,i)
    return height

def calc_height(tree_head):
    while tree_head!=None:
        print(tree_head.data+" ")
        tree_head=tree_head.left
    return 0