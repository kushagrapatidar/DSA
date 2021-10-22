#Driver Code: Singly Linked List
'''if True:
    from singly_linked_list import operate
    head=tail=None
    operate(head,tail)
    #Test List
        #Ins - 'Lists'
        #Ins - beg - 'Linked'
        #Ins - end - 'is'
        #Ins - end - 'a'
        #Ins - 1 - 'Doubly'
        #Ins - 7 - 'Structure'
        #Ins - 6 - 'Data'
        #Trav
        #Srch - 'a'
        #Updt - 'Lists' to 'List'
        #Trav
        #Del - 5
        #Del - beg
        #Del - end
        #Trav
        #Rev
        #Trav
    #'''

#Driver Code: Doubly Linked List
'''if True:
    from doubly_linked_list import operate
    head=tail=None
    operate(head,tail)
    #Test List
        #Ins - 'Lists'
        #Ins - beg - 'Linked'
        #Ins - end - 'is'
        #Ins - end - 'a'
        #Ins - 1 - 'Doubly'
        #Ins - 7 - 'Structure'
        #Ins - 6 - 'Data'
        #Trav
        #Srch - 'a'
        #Updt - 'Lists' to 'List'
        #Trav
        #Del - 5
        #Del - beg
        #Del - end
        #Trav
        #Rev
        #Trav
    #'''

#Driver Code: Circular Linked List
'''if True:
    from circular_linked_list import operate
    head=tail=None
    operate(head,tail)
    #Test List
        #Ins - 'Lists'
        #Ins - beg - 'Linked'
        #Ins - end - 'is'
        #Ins - end - 'a'
        #Ins - 1 - 'Doubly'
        #Ins - 7 - 'Structure'
        #Ins - 6 - 'Data'
        #Trav
        #Srch - 'a'
        #Updt - 'Lists' to 'List'
        #Trav
        #Del - 5
        #Del - beg
        #Del - end
        #Trav
        #Rev
        #Trav
    #'''

#Driver Code: Binary Tree Height
if True:
    from tree import make_tree
    from binary_tree_height import find_height_ll
    from heapyfy import heapyfy
    def print_tree(tree_root):
        left=tree_root.left
        right=tree_root.right
        
        if left!=None:
            print(left.data,end=" ")
        if right!=None:
            print(right.data,end=" ")
        
        print("\n")
        if left!=None:
            print_tree(left)
        print("\n")
        if right!=None:
            print_tree(right)

    tree_root=make_tree()
    tree_root=heapyfy(tree_root)
    #print(tree_root.data)
    #print_tree(tree_root)
    max_height,min_height=find_height_ll(tree_root)
    val=(max_height==min_height)
    if val:
        print("Perfect")
    else:
        print("Not Perfect")
    #Test Cases:
        #arr=[2,3,9,4]
        #max_height = 2, min_height=1
        #arr=[2,3,9,4,5,10,11,6]
        #max_height = 3, min_height = 2 '''