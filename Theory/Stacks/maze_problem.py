#Function to create a Maze
def Maze(r,c):
    maze=list()
    for _ in range(r):
        col=list()
        for _2 in range(c):
            col.append(_+(r*_2))
        maze.append(col)
    return maze

#Function to create walls in the maze
def setwall(lst, maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j]=='S' or maze[i][j]=='E':
                continue
            elif maze[i][j] not in lst:
                maze[i][j]=1
            else:
                maze[i][j]=0
    return maze

#Function to create the start point
def setstart(start,maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if i+(len(maze)*j)==start:
                maze[i][j]="S"
    return maze

#Function to create the end point
def setend(end,maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if i+(len(maze)*j)==end:
                maze[i][j]="E"
    return maze

#Function to reset the Maze to the initial state
def reset(lst,maze):
    maze=setwall(lst,maze)
    return maze

#Function to find path in the Maze
def findpath(prev,curr,path,maze): 
    return path


#Driver Code

#Genrate a maze
r_n_c=input('Enter the number of rows and columns: (Format: rows,columns)\n')
[r,c]=r_n_c.split(',')
r,c=int(r),int(c)
maze=Maze(r,c)


#Setting Starting and Ending points
start=input(f'Enter the Start index in range 0 to {r*c-1}:\n')
end=input(f'Enter the End index in range 0 to {r*c-1} except '+start+':\n')
boundries=list()
for i in range(len(maze)):
    if i==0 or i==r-1:
        j=0
        while j<c:
            boundries.append(i+r*j)
            j+=1
    else:
        boundries.append(i+0)
        boundries.append(i+(c-1)*r)
#print(boundries)

if start==end and start not in boundries and end not in boundries:
    print('Start and End cannot be placed at the given indices!!')
else:
    start=int(start)
    end=int(end)
    maze=setstart(start,maze)
    maze=setend(end,maze)

    #Put Walls
    walls=input(f'Enter the wall indices in range 0 to {r*c-1} except {start,end}: (Format 0,1,2,...)\n')
    wall_list=walls.split(',')
    #print(wall_list)
    for i in range(len(wall_list)):
        wall_list[i]=int(wall_list[i])
    maze=setwall(wall_list, maze)
    print(maze)

    #path=[]
    #path=findpath((si,sj),(ei,ej),path,maze)
    
#Maze 1
    #Maze Shape: 7x7
    #Walls: 0,1,2,3,4,5,6,7,13,14,15,16,18,21,23,25,27,28,32,33,34,35,37,40,41,42,44,45,46,47,48
    #Start: 42
    #End: 20