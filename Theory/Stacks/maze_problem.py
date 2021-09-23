#Function to create a Maze
def Maze(r,c):
    maze=list()
    for _ in range(c):
        row=list()
        for _2 in range(r):
            row.append(_2+(c*_))
        maze.append(row)
    return maze

#Function to create walls in the maze
def setwall(lst, maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[j][i]=='S' or maze[j][i]=='E':
                continue
            elif maze[j][i] not in lst:
                maze[j][i]=1
            else:
                maze[j][i]=0
    return maze

#Function to create the start point
def setstart(start,maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if i+(len(maze)*j)==start:
                maze[j][i]="S"
    return maze

#Function to create the end point
def setend(end,maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if i+(len(maze)*j)==end:
                maze[j][i]="E"
    return maze

#Function to reset the Maze to the initial state
def reset(start,end,lst,maze):
    maze=Maze(len(maze),len(maze[0]))
    maze=setstart(start,maze)
    maze=setend(end,maze)
    maze=setwall(lst,maze)
    return maze

#Function to find path in the Maze
def findpath(prev,curr,path,maze): 
    return path

#Function to print Maze
def print_maze(maze):
    for _ in maze:
        print(_)

#Driver Code
if True:
    #Genrate a maze
    r_n_c=input('Enter the number of rows and columns: (Format: rows,columns)\n')
    [r,c]=r_n_c.split(',')
    r,c=int(r),int(c)
    maze=Maze(r,c)
    print_maze(maze)

    #Taking input of start and end
    start=input(f'Enter the Start index in range 0 to {r*c-1}:\n')
    end=input(f'Enter the End index in range 0 to {r*c-1} except '+start+':\n')
    boundries=list()
    for i in range(len(maze)):
        if i==0 or i==c-1:
            j=0
            while j<r:
                boundries.append(i+c*j)
                j+=1
        else:
            boundries.append(i+0)
            boundries.append(i+(r-1)*c)
    #print(boundries)

    if start==end and start not in boundries and end not in boundries:
        print('Start and End cannot be placed at the given indices!!')
    else:
        #Setting Starting and Ending points
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
        print_maze(maze)

        #Find Path
        #path=[]
        #path=findpath((si,sj),(ei,ej),path,maze)

        #Reset Maze
        #maze=reset(start,end,wall_list,maze)
        #print_maze(maze)
    
    
#Maze 1
    #Maze Shape: 7x7
    #Walls: 0,1,2,3,4,5,6,7,13,14,15,16,18,21,23,25,27,28,32,33,34,35,37,41,42,44,45,46,47,48
    #Start: 43
    #End: 20