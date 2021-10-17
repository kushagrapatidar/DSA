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

#Insert Operations    
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

########################################################################################################################################################################
#Delete Operations
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

########################################################################################################################################################################
#Miscellaneous Operations
#Reverse Operation
def reverse(head,tail):
    temp=head
    while temp!=None:
        temp.prev,temp.next=temp.next,temp.prev
        temp=temp.prev
    head,tail=tail,head
    set_pos(head)
    return head,tail

#Traverse Operation
def traverse(head):
    temp=head
    data=""
    posStr=""
    while temp!=None:
        data+=str(temp.data)+" "
        posStr+=str(temp.pos)+" "
        temp=temp.next
    
    print(data+"\n"+posStr)

#Sort Operation
def sort(head,tail): #CONTINUE HERE
    return head,tail

#Search Operation
def search(head,data=None):
    pos=[]
    if data==None:
        data=input('Enter the data to be searched: ')
    try:
        try:
            data=int(data)
        except ValueError:
            data=float(data)
    except ValueError:
        data=str(data)
    temp=head
    while temp!=None:
        if temp.data==data:
            pos.append(temp.pos)
        temp=temp.next
    print(f'{data} found at the positions {pos} in the list.')
    return pos

#Update Operation
def update(head):
    olddata=input('Enter the data to be Updated: ')
    newdata=input('Enter the Updated data: ')
    try:
        try:
            olddata=int(olddata)
        except ValueError:
            olddata=float(olddata)
    except ValueError:
        olddata=str(olddata)
    try:
        try:
            newdata=int(newdata)
        except ValueError:
            newdata=float(newdata)
    except ValueError:
        newdata=str(newdata)
    pos=search(head,olddata)
    if len(pos)==0:
        print(f"The list does not contain any data,{olddata}")
    
    else:
        temp=head
        while temp!=None:
            if temp.pos in pos:
                temp.data=newdata
            temp=temp.next
    
########################################################################################################################################################################
#Insert Function
def insert(head,tail):
    data=input('\nEnter the data: ')
    try:
        try:
            data=int(data)
        except ValueError:
            data=float(data)
    except ValueError:
                data=str(data)
    
    if head==None or tail==None:
        print("\nThe List is Empty!!\nCreating the first Node...\n")
        head=Node()
        head.data=data
        head.pos=1
        tail=head
        print("Node created successfully!!")

    else:
        ch=input("Enter the position of insertion:'B' for Beginnig, 'E' for End or Position in numbers greater than or equal to 1: ")
    
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

#Delete Function
def delete(head,tail):
    if head==None or tail==None:
        print("The List is Empty!!")
    else:
        ch=input("Enter the position of deletion:'B' for Beginnig, 'E' for End or Position in numbers greater than or equal to 1: ")
        try:
            ch=int(ch)
            head,tail=delete_bet(head,tail,ch)
        except ValueError:
            if ch=='B' or ch=='b':
                head=delete_beg(head)
            elif ch=='E' or ch=='e':
                tail=delete_end(tail)
    
    set_pos(head)
    return head,tail

########################################################################################################################################################################
#Functions to call insert and delete functions
def call_insert(head,tail):
    num=int(input('Enter the number of elements to be inserted: '))
    for _ in range(num):
        head,tail=insert(head,tail)

    return head,tail

def call_delete(head,tail):
    num=int(input('Enter the number of elements to be deleted: '))
    for _ in range(num):
        head,tail=delete(head,tail)

    return head,tail

########################################################################################################################################################################
#Operate Function to choose the operation
def operate(head,tail):        
    ch=input("Enter the operation:\n'I' to Insert\n'D' to Delete\n'Sr' to Search\n'U' to Update\n'R' to Reverse\n'St' to Sort\n'T' to Traverse\nYour Choice: ")
    if ch=='I' or ch=='i':
        head,tail=call_insert(head,tail)
        
    elif ch=='D' or ch=='d':
        head,tail=call_delete(head,tail)
        
    elif ch=='R' or ch=='r':
        head,tail=reverse(head,tail)
        
    elif ch=='T' or ch=='t':
        traverse(head)
        
    elif ch=='U' or ch=='u':
        update(head)
        
    elif ch.upper()=='SR':
        search(head)
        
    elif ch.upper()=='ST':
        head,tail=sort(head,tail)
        
    else:
        print("Invalid Choice!!\nPlease try again...\n")
        operate(head,tail)
    ch=input("Do you want to conduct more operations??('Y' for yes & 'N' for no): ")
    if ch=='Y' or ch=='y':
        operate(head,tail)

#Tail Traverse
#if True:
    #data=""
    #while tail!=None:
    #    data=tail.data+" "+data
    #    tail=tail.prev
    #data=data[:-1]
    #print("\n"+data)