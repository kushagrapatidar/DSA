class Tree:
    data=None
    right=None
    left=None
class Node:
    data=None
    next=None

#Insert Operations    
def insert_end(tail,data):
    newNode=Node()
    newNode.data=data
    if tail==None:
        tail=newNode
    else:
        tail.next=newNode
        tail=newNode
    
    return tail

def create_tree(head):
    tree=[]
    while head!=None:
        tree.append(head)
        head=head.next
    
    tree_head=tree[0]
    return tree_head

def make_tree():
    ch=input("Enter the number of elements: ")
    head=tail=None
    data=input('Enter the data: ')
    head=tail=insert_end(tail,data)
    while ch>1:
        data=input('Enter the data: ')
        insert_end(tail,data)
    tree_head=create_tree(head)
    return  tree_head