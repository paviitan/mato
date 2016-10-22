from time import sleep
from os import system, name
from random import randint
from msvcrt import getwche


def cls():
    """ Attempts to clear the console depending on OS """
    system('cls' if name=='nt' else 'clear')
    
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
    available_space.remove(apple[-1])
    return apple
    
def check_apple(apple):
    try:
        check = apple[-1]
    except(IndexError):
        return False
    else:
        return True
        
def check_moves(available_space):
    try:
        check = available_space[-1]
    except(IndexError):
        return False
    else:
        return True
        
def get_keypress():
    keypress = getwche()
    #print(keypress)
    if keypress == "a":
        return "Left"
    elif keypress == "d":
        return "Right"
    elif keypress == "w":
        return "Forward"
    else:
        quit()

def turn_snake(direction):
    """ Turns snake relative to previous direction """
    directions = ["N", "W", "S", "E"]
    turn = get_keypress()
    if turn == "Right":
        index = directions.index(direction)
        try:
            direction = directions[index-1]
        except(IndexError):
            return directions[-1]
        else:
            return direction
    elif turn == "Left":
        directions.reverse()
        index = directions.index(direction)
        try:
            direction = directions[index-1]
        except(IndexError):
            return directions[-1]
        else:
            return direction
    else:
        return direction
    
    
def move_snake(direction,available_space,snake):
    """ Get direction and check if next coordinate is available. If true, moves snake by setting new coordinate as index 0 and removing index -1. snake[-1] coordinate also comes available so append it to "available_space" list """
    x,y = snake[0]
    old_space = snake.pop(-1)
    if direction == "E":
        requested_space = (x+1,y)
        try:
            available_space.remove(requested_space)
        except(ValueError):
            try:
                apple.remove(requested_space)
            except(ValueError):
                print("Tööt!")
            else:
                snake.insert(0,requested_space)
                snake.append(old_space)
        else:
            snake.insert(0,requested_space)
            available_space.append(old_space)
    elif direction == "W":
        requested_space = (x-1,y)
        try:
            available_space.remove(requested_space)
        except(ValueError):
            try:
                apple.remove(requested_space)
            except(ValueError):
                print("Tööt!")
            else:
                snake.insert(0,requested_space)
                snake.append(old_space)
        else:
            snake.insert(0,requested_space)
            available_space.append(old_space)
    elif direction == "N":
        requested_space = (x,y-1)
        try:
            available_space.remove(requested_space)
        except(ValueError):
            try:
                apple.remove(requested_space)
            except(ValueError):
                print("Tööt!")
            else:
                snake.insert(0,requested_space)
                snake.append(old_space)
        else:
            snake.insert(0,requested_space)
            available_space.append(old_space)
    elif direction == "S":
        requested_space = (x,y+1)
        try:
            available_space.remove(requested_space)
        except(ValueError):
            try:
                apple.remove(requested_space)
            except(ValueError):
                print("Tööt!")
            else:
                snake.insert(0,requested_space)
                snake.append(old_space)
        else:
            snake.insert(0,requested_space)
            available_space.append(old_space)
    else:
        pass
        
def print_room(room, snake, apple, available_space):
    """ For snake room coordinate = x, for available space room coordinate # -- print"""
    for i in range(len(snake)):
        x,y = snake[i]
        room[y][x] = "x"
    for i in range(len(available_space)):
        x,y = available_space[i]
        room[y][x] = "#"
    try:
        x,y = apple[-1]
        room[y][x] = "o"
    except(IndexError):
        pass
    for line in room:
        print(" ".join(line))

if __name__ == "__main__":
    """ For testing game logic, creates 10x10 room and list of available coordinates. Spawns snake. Moves snake with list of moves and for-loop """
    room = []
    available_space = []
    snake = []
    apple = []
    for y in range(10):
        room.append([])
        for x in range(10):
            room[-1].append("#")
    for y in range(len(room)):
        for x in range(len(room[y])):
            available_space.append((x,y)) #for collecting tuples of available coordinates
            
    #moving worm with keypress
    #msvcrt / getwch only works on windows
    snake = spawn_snake(available_space)
    direction = "E"
    while True:
        if check_moves(available_space) == True:
            if check_apple(apple) == True:
                sleep(0.033)
                cls()
                move_snake(direction, available_space, snake)
                print_room(room, snake, apple, available_space)
                direction = turn_snake(direction)
            elif check_apple(apple) == False:
                apple = spawn_apple(available_space)
        else:
            print("Voitit pelin!")

   

