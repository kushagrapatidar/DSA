class TreeNode:
    data=None
    pos=None
    right=None
    left=None
class Node:
    data=None
    pos=None
    next=None

def set_pos(head):
    head.pos=1
    temp=head
    currPos=1
    while temp!=None:
        currPos=temp.pos
        temp=temp.next
        try:
            temp.pos=currPos+1
        except AttributeError:
            continue

def get_tree(tree_root,tree):
    if tree_root.next!=None:
        tree=get_tree(tree_root.right,tree)
        tree=get_tree(tree_root.left,tree)
    else:
        tree.append(tree_root)
    return tree

def print_tree(tree_root):
    tree=[]
    tree=get_tree(tree_root,tree)
    i=0
    while i<len(tree):
        print(f"{tree[i:pow(2,i)]}")
        i+=pow(2,i)

#Insert Operations    
def insert_end(head,tail,data):
    newNode=Node()
    newNode.data=data
    if tail==None:
        head=tail=newNode
    else:
        tail.next=newNode
        tail=newNode
    
    return head,tail

def create_tree(tree_root):
    tree_lst=[]
    while tree_root!=None:
        tree_lst.append(tree_root)
        tree_root=tree_root.next
    tree=[]
    for i in range(len(tree_lst)):
        tree_node=TreeNode()
        tree_node.data=tree_lst[i].data
        tree_node.pos=tree_lst[i].pos
        tree.append(tree_node)
    #[print(_.data,end=" ") for _ in tree_lst]
    for i in range(len(tree)//2):
        try:
            tree[i].left,tree[i].right=tree[2*i+1],tree[2*i+2]
        except IndexError:
            tree[i].left=tree[2*i+1]
    tree_root=tree[0]
    return tree_root

def make_tree():
    ch=int(input("Enter the number of elements: "))
    head=tail=None
    while ch>0:
        data=input('Enter the data: ')
        head,tail=insert_end(head,tail,data)
        ch-=1
    set_pos(head)
    # temp=head
    # while temp!=None:
    #     print(temp.data,":",temp.pos)
    #     temp=temp.next
    tree_root=create_tree(head)
    return  tree_root
