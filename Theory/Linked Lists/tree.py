class TreeNode:
    data=None
    right=None
    left=None
class Node:
    data=None
    next=None

#Insert Operations    
def insert_end(tree_root,leaf,data):
    newNode=Node()
    newNode.data=data
    if leaf==None:
        tree_root=leaf=newNode
    else:
        leaf.next=newNode
        leaf=newNode
    
    return tree_root,leaf

def create_tree(tree_root):
    tree_lst=[]
    while tree_root!=None:
        tree_lst.append(tree_root)
        tree_root=tree_root.next
    tree=[]
    for i in range(len(tree_lst)):
        tree_node=TreeNode()
        tree_node.data=tree_lst[i].data
        tree.append(tree_node)
    #[print(_.data,end=" ") for _ in tree_lst]
    for i in range(len(tree)//2):
        try:
            tree[i].left,tree[i].right=tree[2*i+1],tree[2*i+2]
        except IndexError:
            tree[i].left=tree[2*i+1]
    tree_tree_root=tree[0]
    return tree_tree_root

def make_tree():
    ch=int(input("Enter the number of elements: "))
    tree_root=tail=None
    while ch>0:
        data=input('Enter the data: ')
        tree_root,tail=insert_end(tree_root,tail,data)
        ch-=1

    tree_tree_root=create_tree(tree_root)
    return  tree_tree_root
