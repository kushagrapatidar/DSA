#Ak[i,j]=min{A[i,j],A[i,k]+A[k,j]}
def floyd_warshall(graph):
    n=len(graph)
    k=1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j]=min(graph[i][j],graph[i][k]+A[k][j])

    return graph

def print_graph(graph):
    n=len(graph)
    for i in range(n):
        for j in range(n):
            if graph[i][j]==float('inf'):
                print('INF',end=" ")
            else:
                print(A[i][j],end=" ")
        print("\n")

INF=float('INF')
graph= [[0,5,INF,10],
    [INF,0,3,INF],
    [INF,INF,0,1],
    [INF,INF,INF,0]]

print_graph(graph)
print(f"\n{len(A)}\n")

graph=floyd_warshall(graph)
print_graph(graph)