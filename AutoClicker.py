from tkinter import *
from tkinter.messagebox import showinfo
import Main

def aboutWindow():
    showinfo("About Me", "My name is Max Shapira, this is a my clicker for the game 'Clicker Heroes'")


def Window():
    AutoClicker = Tk()
    AutoClicker.title("Auto Clicker for Clicker Heroes")
    AutoClicker.geometry("500x280")

    AutoClicker.columnconfigure(0, weight=1)
    AutoClicker.columnconfigure(1, weight=3)
    AutoClicker.rowconfigure(0, weight=1)
    AutoClicker.rowconfigure(1, weight=3)

    menuBar = Menu(AutoClicker)
    FileMenu = Menu(menuBar, tearoff=0)
    FileMenu.add_command(label="Exit", command=lambda: exit(1))
    menuBar.add_cascade(label="File", menu=FileMenu)

    AboutMenu = Menu(AutoClicker, tearoff=0)
    AboutMenu.add_command(label="Contact")
    AboutMenu.add_command(label="About", command=lambda: aboutWindow())
    menuBar.add_cascade(label="About", menu=AboutMenu)

    AutoClicker.config(menu=menuBar)

    OptionLevel = Checkbutton(AutoClicker, text="Control levels", height=1, width=10, variable=Main.LevelControl, onvalue=True, offvalue=False)
    OptionUpgrade = Checkbutton(AutoClicker, text="Control Upgrades", height=1, width=13, variable=Main.UpgradeControl, onvalue=True, offvalue=False)

    OptionLevel.place(relx=0.09, rely=0.35, anchor='w')
    OptionLevel['font'] = ("Lato", 14)
    OptionUpgrade.place(relx=0.091, rely=0.44, anchor='w')
    OptionUpgrade['font'] = ("Lato", 14)

