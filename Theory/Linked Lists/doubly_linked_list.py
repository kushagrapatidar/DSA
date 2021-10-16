class Node:
    prev=None
    data=None
    next=None
    pos=None

def set_pos(head):
    head.pos=0
    temp=head
    currPos=0
    while temp!=None:
        currPos=temp.pos
        temp=temp.next
        try:
            temp.pos=currPos+1
        except AttributeError:
            continue
    
def insert_beg(head,data):
    if head==None:
        head.data=data
        head.pos=0
        return head
    else:
        newNode=Node()
        newNode.data=data
        newNode.next,head.prev=head,newNode
        head=newNode
        set_pos(head)
        return head

def insert_bet(head,tail,pos,data):
    if head.data==None:
        print("There is no node in the list\nCreating the first node...\n")
        head.data=data
        head.pos=0
        return head
    else:
        if pos==1:
            head=insert_beg(head,data)
        else:            
            try:
                currNode=head

                while currNode.pos<pos-2:
                    currNode=currNode.next
                nextNode=currNode.next
        
                if nextNode!=None:
                    newNode=Node()
                    newNode.data=data
                    newNode.prev,currNode.next=currNode,newNode
                    newNode.next,nextNode.prev=nextNode,newNode
            except AttributeError:
                tail=insert_end(head,tail,data)

        set_pos(head)
        return head,tail

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
        tail=newNode
        set_pos(head)
        return tail

def delete_beg(head):
    print(f"Data at the deleted Node: {head.data}")
    temp=head
    head=None
    head=temp.next
    head.prev=None
    set_pos(head)
    return head

def delete_bet(head,tail,pos):
    if pos==1:
        head=delete_beg(head)
    else:
        temp=head
        while temp!=None:
            if temp.pos==pos-1:
                print(f"Data at the deleted Node: {temp.data}")
                break
            temp=temp.next
        try:
            temp.prev.next,temp.next.prev=temp.next,temp.prev
            temp=None
        except AttributeError:
            tail=delete_end(tail)
    set_pos(head)
    return head,tail

def delete_end(tail):
    print(f"Data at the deleted Node: {tail.data}")
    temp=tail
    tail=None
    tail=temp.prev
    tail.next=None
    return tail

def insert(head,tail):
    data=input('Enter the data: ')
    if isinstance(data, int):
        data=int(data)
    if head==None or tail==None:
        print("The List is Empty!!")

    else:
        ch=input(f"Enter the position of insertion:'B' for Beginnig, 'E' for End or Position between 1 and {tail.pos+1}: ")
    
        if isinstance(ch, int):
            ch=int(ch)
            head,tail=insert_bet(head,tail,ch,data)
        elif ch=='B' or ch=='b':
            head=insert_beg(head,data)
        elif ch=='E' or ch=='e':
            tail=insert_end(head,tail,data)
    
    return head,tail

def delete(head,tail):
    if head==None or tail==None:
        print("The List is Empty!!")
    else:
        ch=input(f"Enter the position of deletion:'B' for Beginnig, 'E' for End or Position between 1 and {tail.pos+1}: ")
        if isinstance(ch, int):
            ch=int(ch)
            head,tail=delete_bet(head,tail,ch)
        elif ch=='B' or ch=='b':
            head=delete_beg(head)
        elif ch=='E' or ch=='e':
            tail=delete_end(tail)
    
    return head,tail


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

tail=insert_end(head,tail,"is")
tail=insert_end(head,tail,"a")

head,tail=insert_bet(head,tail,1,"Doubly")
head,tail=insert_bet(head,tail,7,"Structure")
head,tail=insert_bet(head,tail,6,"Data")

print("Initial Linked List: ")
data,posStr=traverse(head)
print(data+"\n"+posStr)

print("\n")
head,tail=delete_bet(head,tail,5)

head=delete_beg(head)

tail=delete_end(tail)

print("\nLinked List after deletion: ")
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