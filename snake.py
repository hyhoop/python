import readchar as readchar
from random import randint
import os

POS_X = 0
POS_Y = 1
NUM_OF_OBJECTS = 20
TAIL_LENGTH = 0

my_position = [2,1]
end_game = False
map_objects = []
tail = []
score = 0

map_draw = """\
########################################
##                               #######
##                               #######
#############################       ####
#########          ##########       ####
#########           #########    #######
########     ###                 #######
#######     #####                #######
######     ##################    #######
#####      ##################         ##
######      #################         ##
#######                ######    #######
########                  ###    #######
####################     ####    #######
###################     #####    #######
##################     ######    #######
#################     #######    #######
#################      #####     #######
##################      ###     ########
###                            #########
###                            #########
########################################
########################################
########################################"""

# MAP_WIDTH = 20
# MAP_HEIGHT = 15



draw_to_list = [list(row) for row in map_draw.split("\n")]

MAP_WIDTH = len(draw_to_list[0])
MAP_HEIGHT = len(draw_to_list)


while not end_game:
    while len(map_objects) != NUM_OF_OBJECTS:
        new_object = [randint(0, MAP_WIDTH - 1), randint(0, MAP_HEIGHT - 1)]

        if new_object not in map_objects and new_object != my_position and new_object not in tail and\
                draw_to_list[new_object[POS_Y]][new_object[POS_X]] != "#":
            map_objects.append(new_object)

    print("+" + "-" * MAP_WIDTH * 2 + "+")

    for cordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for cordinate_x in range(MAP_WIDTH):
            char_to_set = "  "
            object_in_cell = None
            tail_in_cell = None

            if draw_to_list[cordinate_y][cordinate_x] == "#":
                char_to_set = " #"

            for tail_piece in tail:
                if tail_piece[POS_X] == cordinate_x and tail_piece[POS_Y] == cordinate_y:
                    char_to_set = " @"
                    tail_in_cell = tail_piece

            for objects in map_objects:
                if objects[POS_X] == cordinate_x and objects[POS_Y] == cordinate_y:
                    char_to_set = " X"
                    object_in_cell = objects

            if my_position[POS_X] == cordinate_x and my_position[POS_Y] == cordinate_y:
                char_to_set = " @"
                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    TAIL_LENGTH += 1
                    score += 1
                if tail_in_cell:
                    end_game = True

            print("{}".format(char_to_set), end="")

        print("|")

    print("+" + "-" * MAP_WIDTH * 2 + "+")

    direction = readchar.readchar()
    movement = None

    if direction == "w":
        movement =[my_position[POS_X], (my_position[POS_Y]-1) % MAP_HEIGHT]
    elif direction == "a":
        movement = [(my_position[POS_X]-1) % MAP_WIDTH ,my_position[POS_Y]]
    elif direction == "s":
        movement =[my_position[POS_X], (my_position[POS_Y]+1) % MAP_HEIGHT]
    elif direction == "d":
        movement = [(my_position[POS_X]+1) % MAP_WIDTH ,my_position[POS_Y]]
    elif direction == "q":
        end_game = True

    if movement:
        if draw_to_list[movement[POS_Y]][movement[POS_X]] != "#":
            tail.insert(0, my_position.copy())
            tail = tail[:TAIL_LENGTH]
            my_position = movement

    os.system("cls")
    print("score: {}".format(score))

print("GAME OVER")
