def make_path(i,lst,lst2):
    nodes=lst[i]
    for j in range(len(nodes)):
        if nodes[j][1] not in lst2:
            lst2.append(nodes[j][1])
            lst2=make_path(nodes[j][1],lst,lst2)
    return lst2

def find_path(start,end,graph):
    lst=dict()
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j]==1:
                if i not in lst.keys():
                    lst[i]=[[i,j]]
                else:
                    lst[i].append([i,j])
    print(lst)
    lst3=list()
    for i in lst.keys():
        lst2=list()
        lst2.append(i)
        lst2=make_path(i,lst,lst2)
        lst3.append(lst2)
        print(lst2)
        # lst2=list()
        # for _ in lst3:
        #     if _.index(start)<_.index(end):
        #         lst2.append(_[_.index(start):_.index(end)+1])
        # length=0
        # lst3=list()
        # for i in range(len(lst2)):
        #     if length==0:
        #         lst3=lst2[i]
        #         length=len(lst2[i])
        #     if len(lst2[i])<length:
        #         lst3=lst2[i]
        #         length=len(lst2[i])
        
    return lst3

def print_graph(graph):
    n=len(graph)
    print('   ',end='')
    [print(f'\033[1;33;40m{x}',end="  ") for x in range(1,n+1)]
    print('\n')
    for i in range(1,n+1):
        print(f'\033[1;31;40m{i}\033[1;37;40m',end="  ")
            
        for j in range(1,n+1):
            print(f'{graph[i-1][j-1]}',end="  ")
        print("\n")

#Driver Code
if True:
    #Strongly Connected Graph
    graph=[[0,0,0,1,1],
           [1,0,0,0,0],
           [0,0,0,1,0],
           [0,1,1,0,0],
           [1,0,0,0,0]]
    #Strongly Connected Graph
    # graph=[[0,0,0,1],
    #        [1,0,0,0],
    #        [0,0,0,1],
    #        [0,1,1,0]]
    print_graph(graph)
    print("\033[1;37;40m")
    start=int(input('Enter the starting vertex: '))
    end=int(input('Enter the ending vertex: '))
    path=find_path(start,end,graph)
    print("\033[0;37;40m")

