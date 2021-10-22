class TreeNode:
    data=None
    right=None
    left=None
class Node:
    data=None
    next=None

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

def create_tree(head):
    tree_lst=[]
    while head!=None:
        tree_lst.append(head)
        head=head.next
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
    tree_head=tree[0]
    return tree_head

def make_tree():
    ch=int(input("Enter the number of elements: "))
    head=tail=None
    while ch>0:
        data=input('Enter the data: ')
        head,tail=insert_end(head,tail,data)
        ch-=1

    tree_head=create_tree(head)
    return  tree_head
