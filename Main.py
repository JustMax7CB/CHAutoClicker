import keyboard
import mouse
import time
from pyautogui import position, size
from PIL import ImageGrab
import AutoClicker


Screenshot = ImageGrab.grab()
EnabledColor = None
EnabledMouseOnColor = None
DisabledColor = None
DisabledMouseOnColor = None

### Variables For The App ##

UpgradeControl = False
LevelControl = False

###########################

def InitializeColors():
    global EnabledColor, EnabledMouseOnColor, DisabledColor, DisabledMouseOnColor
    EnabledColor = (97, 191, 255)  # Pos(ScreenSize[0] * 0.109375, ScreenSize[1] * 0.3611111)
    EnabledMouseOnColor = (194, 249, 254)
    DisabledColor = (48, 95, 127)
    DisabledMouseOnColor = (47, 90, 0)


##### Constant Coordinates and Colors ####
# positions are relative to 1920x1080 resolution(Full screen)
ScreenSize = size()
MonsterRelativePos = (0.752604, 0.61574074)
Hero1ButtonRelativePos = (0.109375, 0.3611111)
NextLevelRelativePos = (0.802083, 0.0648148)

MonsterPos = (int(ScreenSize[0] * MonsterRelativePos[0]), int(ScreenSize[1] * MonsterRelativePos[1]))
NextLevelPos = (int(ScreenSize[0] * 0.802083), int(ScreenSize[1] * 0.0648148))

UnInitColor = ((158, 101, 13), (150, 95, 11), (142, 90, 9))


##########################################
def getPosition():
    ok = 1
    while 1:
        print(position())


class Hero:
    def __init__(self, Position, Num):
        self.x = Position[0]
        self.y = Position[1]
        if Num == 1:
            self.state = 1
        self.state = -1

    def setState(self, State):
        self.state = State

    def getPos(self):
        return self.x, self.y

    def Press(self):
        mouse.move(self.x, self.y)
        mouse.click()
        CheckHero(self)


def scanScreen():
    global Screenshot
    Screenshot = ImageGrab.grab()


def CheckHero(hero):
    if Screenshot.getpixel(hero.getPos()) in (EnabledColor, EnabledMouseOnColor):
        hero.setState(1)
    elif Screenshot.getpixel(hero.getPos()) in (DisabledColor, DisabledMouseOnColor):
        hero.setState(0)


def CollectCoins():
    for i in range(int(MonsterPos[0] - 100), int(MonsterPos[0] + 100)):
        for j in range(int(MonsterPos[1]), int(MonsterPos[1] + 100)):
            mouse.move(i, j)


def main():
    def Upgrades():
        if Hero1.state == 1:
            Hero1.Press()

    def Levels():
        if int(time.time() * 100) % 60 == 0:
            mouse.move(NextLevelPos[0], NextLevelPos[1])
            mouse.click()
    AutoClicker.Window()
    scanScreen()
    InitializeColors()
    Hero1Pos = (int(ScreenSize[0] * Hero1ButtonRelativePos[0]), int(ScreenSize[1] * Hero1ButtonRelativePos[1]))
    Hero1 = Hero(Hero1Pos, 1)
    run = None
    while True:
        if keyboard.is_pressed('shift') and keyboard.is_pressed('a'):
            run = True
        while run:
            scanScreen()
            CheckHero(Hero1)
            mouse.move(MonsterPos[0], MonsterPos[1])
            mouse.click()
            if UpgradeControl:
                Upgrades()
            if LevelControl:
                Levels()
            if int(time.time() * 100) % 60 == 0:
                CollectCoins()
            if keyboard.is_pressed('shift') and keyboard.is_pressed('b'):
                run = False
            if keyboard.is_pressed('s'):
                exit(1)
        if keyboard.is_pressed('s'):
            exit(1)




if __name__ == '__main__':
    main()
    AutoClicker.mainloop()
