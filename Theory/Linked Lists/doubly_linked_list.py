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

        while currNode.pos<pos-2:
            currNode=currNode.next
        nextNode=currNode.next

        newNode.prev,currNode.next=currNode,newNode
        newNode.next,nextNode.prev=nextNode,newNode

        currPos=0
        while temp!=None:
            currPos=temp.pos
            temp=temp.next
            try:
                temp.pos=currPos+1
                currNode=temp
            except AttributeError:
                continue
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

def delete_beg(head):
    if head==None:
        print("The Linked List Is Empty!!")
        return None
    else:
        print(f"Data at the deleted Node: {head.data}")
        temp=head
        head=None
        head=temp.next
        head.prev=None
        return head

def delete_bet(head,pos):
    if head==None:
        print("The Linked List Is Empty!!")
    else:
        temp=head
        while temp!=None:
            if temp.pos==pos-1:
                print(f"Data at the deleted Node: {head.data}")
                break
            temp=temp.next
        prevNode,nextNode=temp.prev,temp.next
        prevNode.next,nextNode.prev=nextNode,prevNode
        temp=None

    

def delete_end(tail):
    if tail==None:
        print("The Linked List Is Empty!!")
        return None
    else:
        print(f"Data at the deleted Node: {tail.data}")
        temp=tail
        tail=None
        tail=temp.prev
        tail.next=None
        return tail

def traverse(head):
    temp=head
    data=""
    posStr=""
    while temp!=None:
        data+=str(temp.data)+" "
        posStr+=str(temp.pos)+" "
        temp=temp.next

    return data,posStr

#Driver Code
head=Node()
tail=Node()

tail=head=insert_beg(head,"List")
head=insert_beg(head,"Linked")
head=insert_beg(head,"Doubly")

tail=insert_end(head,tail,"is")
tail=insert_end(head,tail,"Structure")

tail=insert_bet(head,5,"a")
tail=insert_bet(head,6,"Data")

data,posStr=traverse(head)
print(data+"\n"+posStr)

#Tail Traverse
#if True:
    #data=""
    #while tail!=None:
    #    data=tail.data+" "+data
    #    tail=tail.prev
    #data=data[:-1]
    #print("\n"+data)