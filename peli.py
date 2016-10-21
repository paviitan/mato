def spawn_snake(available_space):
    """ Spawn snake of lenght 3 to topleft corner of the room """
    snake = available_space[0:3]
    for i in range(len(snake)):
        available_space.remove(snake[i])
    snake.reverse()
    return snake
    
def move_snake(direction,available_space,snake):
    """ Get direction and check if next coordinate is available. If true, moves snake by setting new coordinate as index 0 and removing index -1. -1 index also comes available so append it to "available_space" list """
    x,y = snake[0]
    old_space = snake.pop(-1)
    if direction == "E":
        asked_space = (x+1,y)
        try:
            available_space.remove(asked_space)
        except(IndexError):
            pass
        else:
            snake.insert(0,asked_space)
            available_space.append(old_space)
    elif direction == "W":
        pass
    elif direction == "N":
        pass
    elif direction == "S":
        pass
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
    """ For testing game logic, lets create 10x10 room and list of available coordinates. """
    room = []
    available_space = []
    snake = []
    for y in range(10):
        room.append([])
        for x in range(10):
            room[-1].append("#")
    for y in range(len(room)):
        for x in range(len(room[y])):
            available_space.append((x,y)) #for collecting tuples of available coordinates
    
    snake = spawn_snake(available_space)
    print_room(room,snake,available_space)
    direction = "E"
    move_snake(direction,available_space,snake)
    print_room(room,snake,available_space)
    move_snake(direction,available_space,snake)
    print_room(room,snake,available_space)
    move_snake(direction,available_space,snake)
    print_room(room,snake,available_space)