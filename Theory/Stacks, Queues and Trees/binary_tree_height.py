def find_height(arr,height,i=0):
    if 2*i+1<len(arr):
        height+=1
        i=2*i+1
        height=find_height(arr,height,i=0)
    return height
arr=[2,3,9,4,5]
height=find_height(arr,0)
print(f'Height of the tree{arr} is {height}')