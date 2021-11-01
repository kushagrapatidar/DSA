#N-Queens problem
def set_row_colm(board,i,j):
    for _ in range(len(board)):
        if board[i][_]!=1:
            board[i][_]='O'
    for _ in range(len(board)):
        if board[_][j]!=1:
            board[_][j]='O'
    return board

def set_diag(board,i,j):
    #For diagonally upward on left
    tempi,tempj=i,j
    while tempi>=0 and tempj>=0:
        if board[tempi][tempj]!=1:
            board[tempi][tempj]='O'
        tempi-=1
        tempj-=1
    
    #For diagonally downward on right
    tempi,tempj=i,j
    while 0<=tempi<N and 0<=tempj<N:
        if board[tempi][tempj]!=1:
            board[tempi][tempj]='O'
        tempi+=1
        tempj+=1

    #For diagonally downward on left
    tempi,tempj=i,j
    while 0<=tempi<N and tempj>=0:
        if board[tempi][tempj]!=1:
            board[tempi][tempj]='O'
        tempi+=1
        tempj-=1

    #For diagonally upward on right
    tempi,tempj=i,j
    while tempi>=0 and 0<=tempj<N:
        if board[tempi][tempj]!=1:
            board[tempi][tempj]='O'
        tempi-=1
        tempj+=1
    
    return board

def soln_nqueens(board,N):
    if N>0:
        if N==len(board):
            board[0][1]=1
            board=set_row_colm(board,0,1)
            print_board(board,len(board))
            board=set_diag(board,0,1)
        
        for i in range(len(board)):
            if 1 not in board[i]:
                for j in range(len(board)):
                    if board[i][j]!=1 and board[i][j]!='O':
                        board[i][j]=1
                        board=set_row_colm(board,i,j)
                        print_board(board,len(board))
                        board=set_diag(board,i,j)
                        break
                break
        board=soln_nqueens(board,N-1)
    return board    

def print_board(board,N):
    # for i in range(N):
    #     for j in range(N):
    #         if board[i][j]=='O':
    #             board[i][j]=0
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