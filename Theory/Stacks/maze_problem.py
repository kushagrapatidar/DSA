def Maze(r,c):
    maze=list()
    for _ in range(r):
        col=list()
        for _2 in range(c):
            col.append(1)
        maze.append(col)
    return maze

def setwall(r,c, maze):
    maze[r,c]=0
    return maze

def setstart(r,c,maze):
    maze[r,c]="X"
    return maze

def setend(r,c,maze):
    maze[r,c]="X"
    return maze

def reset(maze):
    return maze
#Driver Code
start=input('Enter the source:')
end=input('Enter the end:')
[si,sj]=start.split()
[ei,ej]=end.split()
path=[]
