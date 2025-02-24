#make a system instead of it instatly givig you honey. it actually stores up and when you call harvest it picked up all the stored honey.

import time
import threading # use threading to make honey production happen in the background until harvest is called ||||| threading.Join() waits for the thread to be done before going on.
import random



class apiary:
    def __init__(self):
        self.honey = 0
        self.money = 0
        self.bees_honey = 0
        self.bees_working = True

        #Threads
        self.passive_honey = threading.Thread(target=self.honey_production, daemon=True)
        self.passive_honey.start()

    def honey_production(self):
        self.bees_working = True
        while self.bees_working:
            self.bees_honey += 1 # (additional_honey) * honey_multiplier}} bee_honey is var name
            time.sleep(1)


    def harvest_honey(self):
        print(f"harvesting {self.bees_honey} honey from beehive")
        self.honey += self.bees_honey
        self.bees_honey = 0


    def sell_honey(self):
        self.money = self.honey * 13
        print(f"you sold {self.honey} honey jars for {self.money} dollars")
        self.honey = 0


    def inventory(self):
        print (f"Honey: {self.honey}\nMoney: {self.money}")


    def actions(self):
        command = ""
        while command != "exit":
            command = input("")
            if command == "harvest":
                self.harvest_honey()
                print(f"you now have {self.honey} jars of honey")
            elif command == "sell":
                self.sell_honey()
            elif command == "inv":
                self.inventory()
            elif command == "exit":
                print("Leaving The Farm!")
                self.bees_working = False
                break
            else:
                print("TF you saying!")


def StartGame():
    bee_farm = apiary()
    bee_farm.actions()

StartGame()