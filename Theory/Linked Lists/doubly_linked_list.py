class Node:
    prev=None
    data=None
    next=None

def insert_end(currNode,nextNode,data):
    if currNode.data==None:
        currNode.data=data
        return currNode
    else:
        nextNode.data=data
        nextNode.prev=id(currNode.next)
        currNode.next=id(nextNode.prev)
        return nextNode

def insert_beg(currNode,prevNode,data):
    if currNode.data==None:
        currNode.data=data
        return currNode
    else:
        prevNode.data=data
        prevNode.next=id(currNode.prev)
        currNode.prev=id(prevNode.next)
        return prevNode

#Driver Code
head=Node()
tail=Node()
currNode=Node()
newNode=Node()

currNode=insert_beg(currNode,newNode,"List")
head=currNode=insert_beg(currNode,newNode,"Linked")
currNode=insert_end(currNode,newNode,"is")
currNode=insert_end(currNode,newNode,"a")
currNode=insert_end(currNode,newNode,"Data")
tail=currNode=insert_end(currNode,newNode,"Structure")

