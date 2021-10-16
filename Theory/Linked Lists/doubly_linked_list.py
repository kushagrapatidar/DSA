class Node:
    prev=None
    data=None
    next=None
    pos=None

def insert_beg(head,data):
    if head==None:
        head.data=data
        head.pos=0
        return head
    else:
        newNode=Node()
        newNode.data=data
        newNode.next,head.prev=head,newNode
        newNode.pos=0
        temp=newNode
        while head!=None:
            head.pos=temp.pos+1
            temp=head
            head=head.next
        return newNode

def insert_bet(head,pos,data):
    if head.data==None:
        print("There is no node in the list\nCreating the first node...\n")
        head.data=data
        head.pos=0
        return head
    else:
        newNode=Node()
        newNode.data=data
        currNode=temp=head

        while currNode.pos<pos-1:
            currNode=currNode.next
        nextNode=currNode.next

        newNode.prev,currNode.next=currNode,newNode
        newNode.next,nextNode.prev=nextNode,newNode

        currPos=0
        while temp!=None:
            currPos=temp.pos
            temp=temp.next
            temp.pos=currPos+1
            currNode=temp
        return currNode

def insert_end(head,tail,data):
    if tail==None:
        head.data=data
        head.pos=0
        tail=head
        return tail
    else:
        newNode=Node()
        newNode.data=data
        newNode.prev,tail.next=tail,newNode
        newNode.pos=tail.pos+1
        return newNode

def traverse(head):
    temp=head
    data=""
    while temp!=None:
        data=data+" "+str(temp.data)
        temp=temp.next
    data=data[1:]
    return data

#Driver Code
head=Node()
tail=Node()

tail=head=insert_beg(head,"List")
head=insert_beg(head,"Linked")
head=insert_beg(head,"Doubly")
tail=insert_end(head,tail,"is")
tail=insert_end(head,tail,"Data")
tail=insert_end(head,tail,"Structure")
tail=insert_bet(head,5,"a")

data=traverse(head)
print(data)