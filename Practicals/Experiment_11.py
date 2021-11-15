start=0
end=0
def make_path(i,lst,lst2):
    
    return lst2

def find_path(i,graph):
    lst=dict()
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j]==1:
                if i not in lst.keys():
                    lst[i]=[[i,j]]
                else:
                    lst[i].append([i,j])
    print(lst)
    lst2=list()
    lst2.append(start)
    lst2=make_path(start,lst,lst2)
    # print(lst2)
    for i in range(len(lst2)):
        lst2[i]+=1
    return lst2

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
    start,end=start-1,end-1
    path=find_path(start,graph)
    print(path)
    print("\033[0;37;40m")

