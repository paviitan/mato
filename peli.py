from os import system, name as system_name
from random import randint
from msvcrt import getwche, kbhit
from time import time

SPEED = 7

def cls():
    """ Attempts to clear the console depending on OS """
    system('cls' if system_name=='nt' else 'clear')
    
def spawn_snake(available_space):
    """ Spawn snake of lenght 3 to topleft corner of the room """
    snake = available_space[0:3]
    for i in range(len(snake)):
        available_space.remove(snake[i])
    snake.reverse() #so moving can start to east
    return snake
    
def spawn_apple(available_space):
    """ Spawn one apple randomly to available_space """
    apple = []
    n = randint(0,len(available_space)-1)
    apple.append(available_space[n])
    return apple
    
def check_if_empty(list):
    """ Checks if list is depleted """
    if len(list) == 0:
        return True
    else:
        return False
        
def get_keypress():
    timeout = 1.0/SPEED
    start_time = time()
    keypress = None
    while True:
        if kbhit():
            keypress = getwche()
            break
        elif time() - start_time > timeout:
            break
    if keypress == "a":
        return "Left"
    elif keypress == "d":
        return "Right"
    elif keypress == "q":
        quit()
    else:
        return "Forward"

def turn_snake(direction, available_space, snake):
    """ Turns snake relative to previous direction IF available """
    x1,y1 = snake[0]
    last_direction = direction
    directions = ["N","W","S","E"]
    d_coords = {"N":(0,-1), "W":(-1,0), "S":(0,1), "E":(1,0)}
    turn = get_keypress()
    if turn == "Right":
        index = directions.index(direction) - 1
        try:
            new_direction = directions[index]
        except(IndexError):
            new_direction = directions[-1]
        x2,y2 = d_coords[new_direction]
        if available_space.count((x1+x2,y1+y2)) != 1:
            return last_direction
        else:
            return new_direction
    elif turn == "Left":
        index = directions.index(direction) + 1
        try:
            new_direction = directions[index]
        except(IndexError):
            new_direction = directions[0]
        x2,y2 = d_coords[new_direction]
        if available_space.count((x1+x2,y1+y2)) != 1:
            return last_direction
        else:
            return new_direction
    else:
        return last_direction
  
    
def move_snake(direction, available_space, snake, apple):
    """ Moves snake. On apple, extend the snake. Return false on losing conditions """
    x1,y1 = snake[0]
    d_coords = {"N":(0,-1), "W":(-1,0), "S":(0,1), "E":(1,0)}
    x2, y2 = d_coords[direction]
    #If met with an apple
    if apple.count((x1+x2,y1+y2)) != 0:
        snake.insert(0,(x1+x2,y1+y2))
        available_space.remove((x1+x2,y1+y2))
        apple.remove((x1+x2,y1+y2))
        return True
    #If met with an empty space
    elif available_space.count((x1+x2,y1+y2)) != 0:
        snake.insert(0,(x1+x2,y1+y2))
        available_space.remove((x1+x2,y1+y2))
        tail = snake.pop(-1)
        available_space.append(tail)
        return True
    else:
        return False
        
def init_room(height = 11, width = 11):
    """ Initializes 10x10 room and list of available coordinates. Additional borders for better viewing pleasure """
    room = []
    available_space = []
    
    for y in range(height):
        room.append([])
        for x in range(width):
            room[-1].append("-")
    #available area for playing
    for y in range(1,len(room)-1):
        for x in range(1,len(room[y])-1):
            available_space.append((x,y)) #for collecting tuples of available coordinates
    return(room, available_space)
    
def print_room(room, snake, apple, available_space):
    """ Print the room """
    for i in range(len(snake)):
        x,y = snake[i]
        room[y][x] = "x"
    for i in range(len(available_space)):
        x,y = available_space[i]
        room[y][x] = " "
    try:
        x,y = apple[-1]
        room[y][x] = "o"
    except(IndexError):
        pass
    for line in room:
        print(" ".join(line))

if __name__ == "__main__":
    """ Main game loop """
    flag_victory = False
    room, available_space = init_room(20,20)
    #moving worm with keypress
    #msvcrt / getwch only works on windows
    snake = spawn_snake(available_space)
    apple = spawn_apple(available_space)
    direction = "E"
    while True:
        if check_if_empty(available_space) == False:
            if check_if_empty(apple) == True:
                apple = spawn_apple(available_space)
            else:
                direction = turn_snake(direction, available_space, snake)
                cls()
                if move_snake(direction, available_space, snake, apple) == True:
                    print_room(room, snake, apple, available_space)
                else:
                    break
        else:
            flag_victory = True
            break
    print_room(room, snake, apple, available_space)
    if flag_victory == True:
        print("You win!")
    else:
        print("You lose!")
    
    
   

