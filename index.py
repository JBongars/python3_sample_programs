
from clear import clear
from time import sleep

from pascal import go as pascal
from mastermind import go as mastermind
from thueMorse import go as thueMorse
from randomWalk import go as randomWalk

options = {
    'pascal': pascal,
    'mastermind': mastermind,
    'thueMorse': thueMorse,
    'randomWalk': randomWalk
}

while True:

    clear()

    print("===============================")
    print("SELECT AN OPTION")
    print("===============================")
    
    for i in range(len(options)):
        print("%s - %s" %(i + 1, list(options)[i]))

    print("===============================")
    print("")

    myOpt = input("Type in option 1 to %s. Type 'exit' to exit... " %(len(options)))
    try:
        myOpt = int(myOpt)
        myOpt = list(options)[myOpt - 1]
    except (NameError, ValueError):
        if myOpt == 'exit':
            break

    options.get(myOpt, lambda: print("Invalid Entry... Please try again"))()

    sleep(1)

        
