#Ak[i,j]=min{A[i,j],A[i,k]+A[k,j]}
def floyd_warshall(graph):
    n=len(graph)
    k=1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

    return graph

def print_graph(graph):
    n=len(graph)
    for i in range(n):
        for j in range(n):
            if graph[i][j]==float('inf'):
                print('INF',end="  ")
            else:
                print(f'  {graph[i][j]}',end="  ")
        print("\n")

#Driver Code
if True:
    INF=float('INF')
    graph= [[0,3,INF,7],
        [8,0,2,INF],
        [5,INF,0,1],
        [2,INF,INF,0]]

    print_graph(graph)
    # print(f"\n{len(graph)}\n")

    shortest_path=floyd_warshall(graph)
    print_graph(shortest_path)