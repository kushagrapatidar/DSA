
def get_node_connectivity(i,index,graph,lst=None):
    if lst!=None and i==index:
        return lst
    if lst==None:
        lst=list()
    if i not in lst:
        lst.append(i)
    
    for j in range(len(graph[i])):
        if graph[i][j]==1:
            lst=get_node_connectivity(i,index,graph,lst)
    return lst

def check_connectivity(graph):
    bool_val=True
    lst=list()
    for i in range(len(graph)):
        lst.append(get_node_connectivity(i,i,graph))
    for i in range(len(lst)):
        if len(lst[i])!=len(graph):
            bool_val=False
            break
    return bool_val

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
    graph=[[0,0,0,1],
           [1,0,0,0],
           [0,0,0,1],
           [0,1,1,0]]
    print_graph(graph)
    print("\033[1;37;40m")
    
    if check_connectivity(graph):
        print('The graph is strongly connected.')
    else:
        print('The graph is not strongly connected.')
 
