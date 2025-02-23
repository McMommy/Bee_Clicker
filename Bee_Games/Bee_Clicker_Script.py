#make a system instead of it instatly givig you honey. it actually stores up and when you call harvest it picked up all the stored honey.

import time
import threading # use threading to make honey production happen in the background until harvest is called
import random

Bee = 0
Honey = 0
Command = ""




def StartGame():
    Actions()



#def Increase_Honey():
   # global Honey
   # Stored_Honey = 0
   # if  
   #     while Honey <= 10:
    #        Stored_Honey += 1
    #        time.sleep(2)
   # elif



def Actions():
    global Honey
    Command = ""
    while Command != "exit":
        Command = input("")
        if Command == "harvest":
            Increase_Honey()
        #elif input == "":
            #Choose_Bee()
        elif Command == "exit":
            print("Leaving The Farm!")



StartGame()