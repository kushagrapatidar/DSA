class Node:
    prev=None
    data=None
    next=None
    pos=None

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
    
def insert_beg(head,data):
    newNode=Node()
    newNode.data=data
    newNode.next,head.prev=head,newNode
    head=newNode
    return head

def insert_bet(head,tail,pos,data):
    if pos==1:
        head=insert_beg(head,data)
    elif pos>tail.pos:
        tail=insert_end(tail,data)
    else:            
        currNode=head
        while currNode.pos<pos-1:
            currNode=currNode.next
        nextNode=currNode.next

        if nextNode!=None:
            newNode=Node()
            newNode.data=data
            newNode.prev,currNode.next=currNode,newNode
            newNode.next,nextNode.prev=nextNode,newNode

    return head,tail

def insert_end(tail,data):
    newNode=Node()
    newNode.data=data
    newNode.prev,tail.next=tail,newNode
    tail=newNode
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
            if temp.pos==pos:
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
    try:
        try:
            data=int(data)
        except ValueError:
            data=float(data)
    except ValueError:
                data=str(data)
    
    if head==None or tail==None:
        print("The List is Empty!!\nCreating the first Node...")
        head=Node()
        head.data=data
        head.pos=1
        tail=head

    else:
        ch=input(f"Enter the position of insertion:'B' for Beginnig, 'E' for End or Position between 1 and {tail.pos+1}: ")
    
        try:
            ch=int(ch)
            head,tail=insert_bet(head,tail,ch,data)
        except ValueError:
            if ch=='B' or ch=='b':
                head=insert_beg(head,data)
            elif ch=='E' or ch=='e':
                tail=insert_end(tail,data)
    
    set_pos(head)
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
    
    set_pos(head)
    return head,tail

def reverse(head,tail):
    temp=head
    while temp!=None:
        temp.prev,temp.next=temp.next,temp.prev
        temp=temp.prev
    head,tail=tail,head
    set_pos(head)
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
head=tail=None

num=int(input('Enter the number of elements: '))
for _ in range(num):
    head,tail=insert(head,tail)

#Test List
#beg - 'List'
#beg - 'Linked'
#end - 'is'
#end - 'a'
#1 - 'Doubly'
#7 - 'Structure'
#6 - 'Data'

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