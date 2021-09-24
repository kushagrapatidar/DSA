import numpy as np

#Function to create a Maze
def make_maze(r,c):
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
    maze=make_maze(len(maze),len(maze[0]))
    maze=setstart(start,maze)
    maze=setend(end,maze)
    maze=setwall(lst,maze)
    return maze

#Function to find path in the Maze 
def findpath(curr_i,curr_j,path,maze):
    if 0<=curr_i<len(maze) and 0<=curr_j<len(maze[curr_i]):  
        if maze[curr_j][curr_i]=='S':
            path+=[curr_i,curr_j]
        
        if maze[curr_j][curr_i]=='E':
            path+=[curr_i,curr_j]
    
        elif 0==curr_i or curr_i==len(maze)-1 or 0==curr_j or curr_j==len(maze[curr_i])-1: #CONTINUE HERE
            if 0==curr_i or curr_i==len(maze)-1 and (0!=curr_j and curr_j!=len(maze[curr_i])-1):
                if 0==curr_i:
                    print("")
                elif curr_i==len(maze)-1:
                    print("")
            elif (0!=curr_i and curr_i!=len(maze)-1) and 0==curr_j or curr_j==len(maze[curr_i])-1:
                print("")
            return path
    
        elif 0<curr_i<len(maze)-1 and 0<curr_j<len(maze[curr_i])-1:

            if maze[curr_j-1][curr_i]==1:
                maze[curr_j-1][curr_i]="X"
                path+=[curr_i,curr_j-1]
                path=findpath(curr_i,curr_j-1,maze,path)

            elif maze[curr_j+1][curr_i]==1:
                maze[curr_j+1][curr_i]="X"
                path+=[curr_i,curr_j+1]
                path=findpath(curr_i,curr_j+1,maze,path)

            elif maze[curr_j][curr_i-1]==1:
                maze[curr_j][curr_i-1]="X"
                path+=[curr_i-1,curr_j]
                path=findpath(curr_i-1,curr_j,maze,path)

            elif maze[curr_j][curr_i+1]==1:
                maze[curr_j][curr_i+1]="X"
                path+=[curr_i+1,curr_j]
                path=findpath(curr_i+1,curr_j,maze,path)
        
            else:
                maze[curr_j][curr_i]='O'
                path-=[curr_i,curr_j]
                [curr_i,curr_j]=path[len(path)-1]
                path=findpath(curr_i,curr_j,maze,path)    
        
    return path

#Function to color the starting & ending points, walls and spaces accordingly
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

#Driver Code
if True:

    #Genrate a maze
    r_n_c=input('Enter the number of rows and columns: (Format: rows,columns)\n')
    [r,c]=r_n_c.split(',')
    r,c=int(r),int(c)
    maze=make_maze(r,c)
    #print(np.array(maze))

    #Taking input of start and end
    start=input(f'Enter the Start index in range 0 to {r*c-1}:\n')
    end=input(f'Enter the End index in range 0 to {r*c-1} except '+start+':\n')

    #Creating a list of boundry elements
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

        for i in range(len(wall_list)):
            wall_list[i]=int(wall_list[i])
        maze=setwall(wall_list, maze)
        '''
        print("\n")
        for _ in range(len(maze)):
            for _2 in range(len(maze[_])):
                if maze[_][_2]==0:
                    print(colored(150, 150, 150, '\u25C6 '),end="")                     
                elif maze[_][_2]=='S' or maze[_][_2]=='E':
                    print(colored(0, 255, 255, maze[_][_2]+' '),end="")
                elif maze[_][_2]=='X':
                    print(colored(255, 255, 0, '\u2022 '),end="")
                else:
                    print(colored(0, 0, 0, '  '),end="")
            print("\n")
        print("\n")
        '''

    #'''
    #Find Path 
        for _ in range(len(maze)):
            for _2 in range(len(maze[_])):
                if _2+_*r==start:
                    start_i=_
                    start_j=_2
        path=list()
        path=findpath(start_i,start_j,path,maze)
        
    #Print the solved Maze or reset if no path found
        (i,j)=path[len(path)-1]
        if maze[j][i]=='E':          
            for _ in range(len(maze)):
                for _2 in range(len(maze[_])):
                    if (_,_2) not in path:
                        continue
                    else:
                     maze[_2][_]='X'
            
            print("\n")
            for _ in range(len(maze)):
                for _2 in range(len(maze[_])):
                    if maze[_][_2]==0:
                        print(colored(150, 150, 150, '\u25C6 '),end="")                     
                    elif maze[_][_2]=='S' or maze[_][_2]=='E':
                        print(colored(0, 255, 255, maze[_][_2]+' '),end="")
                    elif maze[_][_2]=='X':
                        print(colored(255, 255, 0, '\u2022 '),end="")
                    else:
                        print(colored(0, 0, 0, '  '),end="")
                print("\n")
            print("\n")
                     
        else:
            print("No path found for the given configuration!!\n")
            print("Resetting the maze...")
        #Reset Maze
            maze=reset(start,end,wall_list,maze)
    #'''
    
#Maze 1
    #Maze Shape: 7x7
    #Walls: 0,1,2,3,4,5,6,7,13,14,15,16,18,21,23,25,27,28,32,33,34,35,37,41,42,44,45,46,47,48
    #Start: 43
    #End: 20

#Maze 2
    #Maze Shape: 10x10
    #Walls: 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,36,40,41,42,44,46,48,50,51,52,56,58,63,64,69,70,71,73,74,76,77,80,81,86,87,88,89,90,91,92,93,94,95,96,97,98,99
    #Start: 30
    #End: 79