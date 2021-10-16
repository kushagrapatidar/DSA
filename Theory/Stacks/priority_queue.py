# Priority Queue implementation in Python


# Function to heapify the tree
def heapify(arr, n, i):
    # Find the largest among root, left child and right child
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    #print("print l r",l,r)
    if l < n and arr[i] < arr[l]:
        #print("left node",arr[l])
        largest = l

    if r < n and arr[largest] < arr[r]:
        #print("right node",arr[r])
        largest = r

    # Swap and continue heapifying if root is not largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# Function to insert an element into the tree
def insert(array, newNum):
    size = len(array)
    array.append(newNum)
    i=size//2
    while i>-1 and i<=size//2:
        heapify(array, size, i)
        i-=1


#Driver Code
arr = []

insert(arr, 3)
insert(arr, 4)
#insert(arr, 9)
#insert(arr, 5)
#insert(arr, 2)
print("max heap",arr)
#deleteNode(arr,9)
#print("After deleting an element: ", arr)
#print("root node is:")
#rootnode(arr)