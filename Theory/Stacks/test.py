def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
  
maze=[
['0', '0', '0' ,'0' ,'0', '0', '0'],
['0' ,'1' ,'1' ,'X' ,'X' ,'X' ,'0'],
['0' ,'0' ,'0' ,'X' ,'0', 'X', 'E'],
['0', '1', '0', 'X', '0', '1', '0'],
['0', 'X', 'X', 'X', '0', '0', '0'],
['0' ,'X' ,'0' ,'1' ,'1' ,'1' ,'0'],
['0' ,'S' ,'0' ,'0' ,'0' ,'0', '0']]
for _ in range(len(maze)):
    for _2 in range(len(maze[_])):
        if maze[_][_2]=='0':
            print(colored(255, 255, 255, maze[_][_2]),end="")                     
        elif maze[_][_2]=='S' or maze[_][_2]=='E':
            print(colored(255, 255, 0, maze[_][_2]),end="")
        elif maze[_][_2]=='X':
            print(colored(0, 255, 255, maze[_][_2]),end="")
        else:
            print(colored(0, 0, 0, maze[_][_2]),end="")
    print("\n")