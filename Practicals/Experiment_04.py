#N-Queens problem
def check_rows(board,N,c):
    for i in range(N):
        if board[i][c]==1:
            return False
    return True

def check_colms(board,N,r):
    for j in range(N):
        if board[r][j]==1:
            return False
    return True

def check_diag(board,N,i,j):
    if 0<i<N-1 and 0<j<N-1 and (board[i-1][j-1]==1 or board[i+1][j+1]==1 or board[i-1][j+1]==1 or board[i+1][j-1]==1):
        return False
    elif (i==0 and 0<j<N and board[i-1][j+1]==1) or (i==N and 0<j<N and board[i-1][j-1]==1):
        return False
        #CONTINUE HERE
        
    return True

def soln_nqueens(board,N):
    board[0][1]=1
    for i in range(N):
        for j in range(N):
            if check_rows(board,N,j) and check_colms(board,N,i) and check_diag(board,N,i,j):
                board[i][j]=1
    return board

def print_board(board,N):
    print('\n')
    for i in range(N):
        for j in range(N):
            print(board[i][j],end="  ")
        print('\n')

#Driver Code
if True:
    N=int(input('Enter the number of Queens: '))
    board=[]
    for i in range(N):
        lst=list()
        for j in range(N):
            lst.append(0)
        board.append(lst)
    
    # print_board(board,N)
    board=soln_nqueens(board,N)
    print_board(board,N)