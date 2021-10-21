def find_height(arr,height,i=0):
    if 2*i+1<len(arr):
        height+=1
        i=2*i+1
        height=find_height(arr,height,i)
    return height

def calc_height(head):
    return None