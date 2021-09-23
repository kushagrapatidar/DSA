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

def findpath(prev,curr,path,maze): 
    return path
#Driver Code
r_n_c=input('Enter the number of rows and columns: ')
[r,c]=r_n_c.split()
maze=Maze(r,c)
walls=input('Enter the wall indices:')
wall_list=walls.split(',')
for i in range(len(wall_list)):
    wall_list[i]=wall_list[i].split(',')
    for j in range(wall_list[i]):
        wall_list[i][j]=wall_list[i][j]#Continue from here"(num","num)"
setwall(wall_list)
start=input('Enter the source: ')
end=input('Enter the end: ')
[si,sj]=start.split()
[ei,ej]=end.split()
setstart(si,sj,maze)
setend(ei,ej,maze)
path=[]
path=findpath((si,sj),(ei,ej),path,maze)
