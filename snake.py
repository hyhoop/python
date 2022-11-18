import readchar
from random import randint
import os

MAP_WIDTH = 20
MAP_HEIGHT = 15
POS_X = 0
POS_Y = 1
NUM_OF_OBJECTS = 1
TAIL_LENGTH = 0

my_positon = [0, 0]
end_game = False
map_objects = []
tail = []

while end_game == False:
    while len(map_objects) != NUM_OF_OBJECTS:
        new_object = [randint(0, MAP_WIDTH - 1), randint(0, MAP_HEIGHT)]

        if new_object not in map_objects and new_object != my_positon:
            map_objects.append(new_object)
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for cordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for cordinate_x in range(MAP_WIDTH):
            char_to_set = " "
            object_in_cell = None
            tail_in_cell = None

            for tail_piece in tail:
                if tail_piece[POS_X] == cordinate_x and tail_piece[POS_Y] == cordinate_y:
                    char_to_set = "@"
                    tail_in_cell = tail_piece

            for objects in map_objects:
                if objects[POS_X] == cordinate_x and objects[POS_Y] == cordinate_y:
                    char_to_set = "*"
                    object_in_cell = objects

            if my_positon[POS_X] == cordinate_x and my_positon[POS_Y] == cordinate_y:
                char_to_set = "@"
                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    TAIL_LENGTH += 1
                if tail_in_cell:
                    end_game = True

            print(" {} ".format(char_to_set), end="")

        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    direction = readchar.readchar()

    if direction == "w":
        my_positon[POS_Y] -= 1
        tail.insert(1, my_positon.copy())
        my_positon[POS_Y] %= MAP_HEIGHT
        tail = tail[:TAIL_LENGTH]
    elif direction == "a":
        my_positon[POS_X] -= 1
        my_positon[POS_X] %= MAP_WIDTH
        tail.insert(1, my_positon.copy())
        tail = tail[:TAIL_LENGTH]
    elif direction == "s":
        my_positon[POS_Y] += 1
        my_positon[POS_Y] %= MAP_HEIGHT
        tail.insert(1, my_positon.copy())
        tail = tail[:TAIL_LENGTH]
    elif direction == "d":
        my_positon[POS_X] += 1
        my_positon[POS_X] %= MAP_WIDTH
        tail.insert(1, my_positon.copy())
        tail = tail[:TAIL_LENGTH]
    elif direction == "q":
        end_game = True

    os.system("cls")
