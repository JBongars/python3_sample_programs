
from random import randint

def go():
    colors = ('R', 'G', 'B', 'Y', 'O', 'P')

    sizeOfGame = 5
    numberOfTurns = 20
    solution = []

    try:
        player_count = int(input("Enter number of players: "))
    except (NameError, ValueError):
        player_count = 1 

    player_name = [None] * player_count
    player_score = [None] * player_count

    for i in range(sizeOfGame):
        solution.append(colors[randint(0, len(colors) - 1)])
        print("[DEBUG] The solution is: ", solution)

    for i in range(player_count):
        player_name[i] = input("Enter player name: ")
        print("index = %d, array = " %(i), player_name)

    # for i in range(numberOfTurns + 1):



    print("[DEBUG] The solution is: ", solution)
    print("[DEBUG] player_name: ", player_name)
    print("[DEBUG] player_score: ", player_score)

