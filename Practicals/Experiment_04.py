#N-Queens problem
# def check_rows(board,N,c):
#     for i in range(N):
#         if board[i][c]==1:
#             return False
#     return True

# def check_colms(board,N,r):
#     for j in range(N):
#         if board[r][j]==1:
#             return False
#     return True

# def check_diag(board,N,i,j):
#     if 0<i<N-1 and 0<j<N-1 and (board[i-1][j-1]==1 or board[i+1][j+1]==1 or board[i-1][j+1]==1 or board[i+1][j-1]==1):
#         return False
#     elif (i==0 and 0<j<N and board[i-1][j+1]==1) or (i==N and 0<j<N and board[i-1][j-1]==1):
#         return False
#         #CONTINUE HERE
        
#     return True

# def soln_nqueens(board,N):
#     board[0][1]=1
#     for i in range(N):
#         for j in range(N):
#             if check_rows(board,N,j) and check_colms(board,N,i) and check_diag(board,N,i,j):
#                 board[i][j]=1
#     return board

def set_row_colm(board,i,j):
    for _ in range(len(board)):
        if board[i][_]!=1:
            board[i][_]='O'
        if board[_][j]!=1:
            board[_][j]='O'
    return board

def set_diag(board,i,j):

    tempi,tempj=i,j
    print(tempi,tempj)
    while tempi>=0 and tempj>=0:
        if board[tempi][tempj]!=1:
            board[tempi][tempj]='O'
        tempi-=1
        tempj-=1
    
    print(tempi,tempj)
    tempi,tempj=i,j
    print(tempi,tempj)
    while 0<=tempi<N and 0<=tempj<N:
        if board[tempi][tempj]!=1:
            board[tempi][tempj]='O'
        tempi+=1
        tempj+=1

    tempi,tempj=i,j
    while 0<=tempi<N and tempj>=0:
        if board[tempi][tempj]!=1:
            board[tempi][tempj]='O'
        tempi+=1
        tempj-=1

    tempi,tempj=i,j
    while tempi>=0 and 0<=tempj<N:
        if board[tempi][tempj]!=1:
            board[tempi][tempj]='O'
        tempi-=1
        tempj+=1
    
    return board

def soln_nqueens(board,N):
    if N>0:
        board[0][1]=1
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