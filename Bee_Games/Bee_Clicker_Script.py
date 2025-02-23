#make a system instead of it instatly givig you honey. it actually stores up and when you call harvest it picked up all the stored honey.

import time
import threading # use threading to make honey production happen in the background until harvest is called ||||| threading.Join() waits for the thread to be done before going on.
import random

bee = 0
honey = 0
bees_honey = 0
command = ""




def StartGame():
    passive_honey.start()
    actions()



def honey_production():
    global honey
    global command
    global bees_honey
    while command != "exit":
        bees_honey += 1 # (additional_honey) * honey_multiplier}} bee_honey is var name
        time.sleep(1)


def sell_honey():
    global honey



def actions():
    global honey
    global bees_honey
    command = ""
    while command != "exit":
        command = input("")
        if command == "harvest":
            print(f"harvesting {bees_honey} honey from beehive")
            honey += bees_honey
            bees_honey = 0
            print(f"you now have {honey} jars of honey")
        elif input == "sell":
            sell_honey()
        elif command == "exit":
            print("Leaving The Farm!")




#Threads
passive_honey = threading.Thread(target=honey_production)



StartGame()