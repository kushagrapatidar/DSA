def print_graph(graph):
    n=len(graph)
    print('   ',end='')
    [print(x,end="  ") for x in range(1,n+1)]
    print('\n')
    for i in range(1,n+1):
        print(i,end="  ")
            
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
    print("\n")
 
