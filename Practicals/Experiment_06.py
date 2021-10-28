#Ak[i,j]=min{A[i,j],A[i,k]+A[k,j]}
def floyd_warshall(A):
    n=len(A)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                A[i][j]=min(A[i][j],A[i][k]+A[k][j])

    return A
INF=float('INF')
A= [[0,5,INF,10],
    [INF,0,3,INF],
    [INF,INF,0,1],
    [INF,INF,INF,0]]
    
print(A,"\n")
A=floyd_warshall(A)
print(A)