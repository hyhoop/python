from random import randint
import os
import readchar
from colorama import init,Fore
from time import sleep
init()
charizar_died = False






def charizar():
    charizar_game = False

    CHARIZAR_LIFE = 10
    YOUR_LIFE = 10

    charizar_life = 10
    your_life = 10

    print("\n¡TE TOCA LUCHAR CONTRA...CHARIZARRRR!\n")
    sleep(1.1)
    while not charizar_died:

        bar_life_charizar = int(charizar_life * 10 / CHARIZAR_LIFE)
        bar_life_you = int(your_life * 10 / YOUR_LIFE)

        print("CHARIZAR: {}{}".format( "#" * bar_life_charizar, " " * (10 - bar_life_charizar)))
        print("YOU:      {}{}".format("#" * bar_life_you, " " * (10 - bar_life_you)))

        print("\nTURNO DE CHARIZAR")
        sleep(1)
        ataque_charizar = randint(1,2)
        if ataque_charizar == 1:
            print("\nCharizar ataca con ataque cachondo, te quita 5 de vida")
            your_life -= 1
        elif ataque_charizar == 2:
            print("Charizar ataca con ataque de sensual, te quita 3 de vida")


        input("Enter para continuar...")
        os.system("cls")



        if your_life <= 0:
            charizar_game = True
            break

    return charizar_game





POS_X = 0
POS_Y = 1
NUM_OF_COACHS = 3
coach1 = [11,8]
pokemons = 0

map = """\
##############################
#                            #
##########      ##############
##########              #  ###
####                       ###
####   ###############  ######
####  ################  ######
####  ##########    ##   #####
####        ##    #####   ####
##########  ##  ########   ###
##########      ########   ###
######################     ###
###################        ###
##############################
##############################"""

map = [list(row) for row in map.split("\n")]
MAP_WIDTH = len(map[0])
MAP_HEIGHT = len(map)
my_position = [10, 8]
end_game = False

# While principal
while not end_game:

    print("+" + "-" * MAP_WIDTH * 2 + "+")

    for cordinate_y in range(MAP_HEIGHT):

        print("|", end="")

        for cordinate_x in range(MAP_WIDTH):
            char_to_draw = "  "
            charizar_in_cell = None

            if coach1[POS_X] == cordinate_x and coach1[POS_Y] == cordinate_y:
                char_to_draw = " &"
                charizar_in_cell = True
            if map[cordinate_y][cordinate_x] == "#":
                char_to_draw = " #"

            if my_position[POS_X] == cordinate_x and my_position[POS_Y] == cordinate_y:
                char_to_draw = Fore.LIGHTCYAN_EX + ' @' + Fore.RESET

                if charizar_in_cell:
                    os.system("cls")
                    end_game = charizar()

            print("{}".format(char_to_draw), end="")

        print("|")

    print("+" + "-" * MAP_WIDTH * 2 + "+")

    direction = readchar.readchar()
    new_position = None

    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]
    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]
    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]
    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]
    elif direction == "q":
        break

    if new_position:
        if map[new_position[POS_Y]][new_position[POS_X]] != "#":
            my_position = new_position

    os.system("cls")

    print("Pokemons defeated {}".format(pokemons))

os.system("cls")