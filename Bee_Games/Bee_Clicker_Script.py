#make a system instead of it instatly givig you honey. it actually stores up and when you call harvest it picked up all the stored honey.

import time
import threading # use threading to make honey production happen in the background until harvest is called ||||| threading.Join() waits for the thread to be done before going on.
import tkinter as tk
from tkinter import messagebox
import random


class Apiary:
    def __init__(self, root): #root stuff for gui
        self.root = root
        self.root.title("Apiary Farming Game")

        #var
        self.honey = 0
        self.money = 0
        self.bees_honey = 0
        self.additional_honey = 0
        self.bees_working = True

#-----------------------------------------------------------------------------------------------------------
        #setting up the ui
        self.setup_ui()

        # Start Honey Production **after** UI is initialized
        self.start_honey_production()

    def setup_ui(self):
        """ Creates all UI elements. """
        self.info_label = tk.Label(self.root, text="Welcome to Buzzing Meadows!", font=("Arial", 14))
        self.info_label.pack()

        self.honey_label = tk.Label(self.root, text="Honey: 0", font=("Arial", 12))
        self.honey_label.pack()

        self.money_label = tk.Label(self.root, text="Money: 0", font=("Arial", 12))
        self.money_label.pack()

        self.harvest_button = tk.Button(self.root, text="Harvest Honey", command=self.harvest_honey)
        self.harvest_button.pack()

        self.sell_button = tk.Button(self.root, text="Sell Honey", command=self.sell_honey)
        self.sell_button.pack()

        self.buy_hive_button = tk.Button(self.root, text="Buy Beehive ($400)", command=self.add_beehive)
        self.buy_hive_button.pack()

        self.exit_button = tk.Button(self.root, text="Exit", command=self.exit_game)
        self.exit_button.pack()

#-----------------------------------------------------------------------------------------------------------
        #game info starts under :D

    def start_honey_production(self):
        #thread
        self.passive_honey = threading.Thread(target=self.honey_production, daemon=True)
        self.passive_honey.start()

    def honey_production(self):
        while self.bees_working:
            self.bees_honey += 1 + self.additional_honey #* honey_multiplier
            time.sleep(1)


    def harvest_honey(self):
        self.honey += self.bees_honey
        messagebox.showinfo("Harvest", f"You harvested {self.bees_honey} honey!")
        self.bees_honey = 0
        self.update_labels()


    def add_beehive(self):
        if self.money >= 400:
            self.money -= 400
            self.additional_honey += 1
            messagebox.showinfo("Upgrade", "You purchased another hive! More honey is produced now.")
            self.update_labels()
        else:
            messagebox.showwarning("Upgrade", "Not enough money! You need $400.")
        self.update_labels()


    def sell_honey(self):
        if self.honey >0:
            money_from_selling = self.honey * 13
            self.money += money_from_selling
            messagebox.showinfo("Sell", f"You sold {self.honey} honey jars for ${money_from_selling}.")
            self.honey = 0
            self.update_labels()
        else:
            messagebox.showwarning("Sell", "You have no honey to sell!")    


    def update_labels(self):
        self.honey_label.config(text=f"Honey: {self.honey}")
        self.money_label.config(text=f"Money: {self.money}")


    def exit_game(self):
        self.bees_working = False
        self.root.destroy()


    #def inventory(self):
        #print (f"Honey: {self.honey}\nMoney: {self.money}")


    #def actions(self):
    #    command = ""
    #    print("In this world, you own a apaiary and farm honey to sell to your customers. Upgrade your farm and become a millionaire.")
    #    print("Actions:(harvest)(sell)(buy)(inv)(exit)")
    #    while command != "exit":
    #        command = input()
    #        if command == "harvest":
    #            self.harvest_honey()
    #            print(f"you now have {self.honey} jars of honey")
    #        elif command == "sell":
    #            self.sell_honey()
    #        elif command == "buy":
    #            self.add_beehive()
    #        elif command == "inv":
    #            self.inventory()
    #        elif command == "exit":
    #            print("Leaving The Farm!")
    #            self.bees_working = False
    #            break
    #        else:
    #            print("TF you saying!")


def StartGame():
    root = tk.Tk()
    game = Apiary(root)
    root.mainloop()



if __name__  == "__main__":
    StartGame()