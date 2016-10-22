from time import sleep
from os import system, name
from random import randint


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
    
def move_snake(direction,available_space,snake):
    """ Get direction and check if next coordinate is available. If true, moves snake by setting new coordinate as index 0 and removing index -1. snake[-1] coordinate also comes available so append it to "available_space" list """
    x,y = snake[0]
    old_space = snake.pop(-1)
    if direction == "E":
        requested_space = (x+1,y)
        try:
            available_space.remove(requested_space)
        except(ValueError):
            print("Tööt!")
        else:
            snake.insert(0,requested_space)
            available_space.append(old_space)
    elif direction == "W":
        requested_space = (x-1,y)
        try:
            available_space.remove(requested_space)
        except(ValueError):
            print("Tööt!")
        else:
            snake.insert(0,requested_space)
            available_space.append(old_space)
    elif direction == "N":
        requested_space = (x,y-1)
        try:
            available_space.remove(requested_space)
        except(ValueError):
            print("Tööt!")
        else:
            snake.insert(0,requested_space)
            available_space.append(old_space)
    elif direction == "S":
        requested_space = (x,y+1)
        try:
            available_space.remove(requested_space)
        except(ValueError):
            print("Tööt!")
        else:
            snake.insert(0,requested_space)
            available_space.append(old_space)
    else:
        pass
        
def print_room(room, snake, available_space):
    """ For snake room coordinate = x, for available space room coordinate # -- print"""
    for i in range(len(snake)):
        x,y = snake[i]
        room[y][x] = "x"
    for i in range(len(available_space)):
        x,y = available_space[i]
        room[y][x] = "#"
    
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
            
    # Moving the worm in for-loop
    # sleep() for timedelay (in seconds)
    snake = spawn_snake(available_space)
    moves = ["E","E","E","S","S","S","W","W","W","N","N","E","E","E","S","S","S","W","W","W","N","N","E","E","E","S","S","S","W","W","W","N","N","E","E","E","S","S","S","W","W","W","N","N","E","E","E","S","S","S","W","W","W","N","N","E","E","E","S","S","S","W","W","W","N","N"]
    for i in range(len(moves)):
        sleep(0.033)
        cls()
        direction = moves[i]
        move_snake(direction, available_space, snake)
        print_room(room, snake, available_space)

