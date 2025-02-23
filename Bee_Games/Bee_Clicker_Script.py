#make a system instead of it instatly givig you honey. it actually stores up and when you call harvest it picked up all the stored honey.

import time
import threading # use threading to make honey production happen in the background until harvest is called ||||| threading.Join() waits for the thread to be done before going on.
import random

bee = 0
honey = 0
bees_honey = 0
command = ""
bees_working = True



def StartGame():
    passive_honey.start()
    actions()



def honey_production():
    global honey, bees_honey, bees_working
    while bees_working:
        bees_honey += 1 # (additional_honey) * honey_multiplier}} bee_honey is var name
        time.sleep(1)


def harvest_honey():
    global honey, bees_honey
    print(f"harvesting {bees_honey} honey from beehive")
    honey += bees_honey
    bees_honey = 0


def sell_honey():
    pass



def actions():
    global honey, bees_honey, bees_working
    command = ""
    while command != "exit":
        command = input("")
        if command == "harvest":
            harvest_honey()
            print(f"you now have {honey} jars of honey")
        elif command == "sell":
            sell_honey()
        elif command == "exit":
            print("Leaving The Farm!")
            bees_working = False



#Threads
passive_honey = threading.Thread(target=honey_production, daemon=True)



StartGame()