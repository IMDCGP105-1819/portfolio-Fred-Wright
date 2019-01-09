from Classes import *
from Story import *
import cmd
import textwrap
import sys
import os
import time
import random


##There is a bug, doing use at home with the wrong item causes You have already helped here! to show, i dont know what causes this as there is only 1 thing that determines its solved status.

def intro():
    print("This is the normal land of Earth.")
    print("Nothing more, nothing less")
    print("This game was made by Fred Wright, Please Enjoy!")
    print("Type Help if you ever get lost")
    menuScreen()


def menuScreen():
    print("What would you like to do?")
    inputM = input(">>")
    if inputM.lower() == "play":
        startGame()
    elif inputM.lower() == "help":
        helpMenu()
    elif inputM.lower() == "quit":
        sys.exit(0)
    while inputM.lower() not in ['play', 'help', 'quit']:
        print("you cant do that")
        inputM = input(">>")
        if inputM.lower() == "play":
            startGame()
        elif inputM.lower() == "help":
            help()
        elif inputM.lower() == "quit":
            sys.exit(0)

Solutions = 0
Inventory = []
InventroryFull = False
ZoneName = ""
Description = 'description'
Examination = 'examine'
Solved = False
Solved2 = False
Up = 'up', 'north'
Down = 'down', 'south'
Left = 'left', 'west'
Right = 'right', 'east'
Item = 'item'
ItemNeeded = 'itemneeded'
CompleteDescription = ()


solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False, 'b1': False, 'b2': False, 'b3': False, 'b4': False}
ZoneMap = {                           # locations
    'a1': {
          ZoneName: 'Town Hall',
          Description: 'Town hall for all needs and stuff.\n The stall you usually go to is closed however \nAlfred, the owner, is doing repairs \nmaybe we could help him',
          Examination: 'examine',
          CompleteDescription: 'Hello',
          Solved: False,
          Solved2: False,
          Up:'b1',
          Down:'b1',
          Left:'a4',
          Right:'a2',
          Item: 'Multicoloured ball', #for unknown
          ItemNeeded: 'Wooden plank'
    },
    'a2': {
          ZoneName: 'Home',
          Description: 'This is your home.\n You look at your mother reading the local paper.\n she seems to be squinting her eyes \nmaybe we could help her.',
          Examination: 'nothing special',
          CompleteDescription: 'Hello',
          Solved: False,
          Solved2: False,
          Up: 'b2',
          Down: 'b2',
          Left: 'a1',
          Right: 'a3',
          Item: 'Key', # for cells
          ItemNeeded: 'glasses'
    },
    'a3': {
          ZoneName: 'Hellish Path',
          Description: 'Oh no! While walking, you see a demon.\n thankfully he does not notice you, he seems to be looking around\n maybe he needs something',
          Examination: 'examine',
          CompleteDescription: 'Hello',
          Solved: False,
          Solved2: False,
          Up: 'b3',
          Down: 'b3',
          Left: 'a2',
          Right: 'a4',
          Item: 'Mystical fiery bolt', #for highgarden
          ItemNeeded: 'Shovel'
    },
    'a4': {
          ZoneName: 'Unknown place',
          Description: 'An eerie place with no meaning, however where seems to be a circular spot on the floor. \nMaybe we need to place something here.',
          Examination: 'examine',
          CompleteDescription: 'Hello',
          Solved: False,
          Solved2: False,
          Up: 'b4',
          Down: 'b4',
          Left: 'a3',
          Right: 'a1',
          Item: 'jug', #for town hall
          ItemNeeded: 'Multicoloured ball'
    },
    'b1': {
          ZoneName: 'City cells',
          Description: 'While looking at the men and women in the cells you notice a familiar face. \nDad! He needs help, we should help him.',
          Examination: 'examine',
          CompleteDescription: 'Hello',
          Solved: False,
          Solved2: False,
          Up: 'a1',
          Down: 'a1',
          Left: 'b4',
          Right: 'b2',
          Item: 'Shovel', #for river
          ItemNeeded: 'Key'
    },
    'b2': {
          ZoneName: 'River',
          Description: 'While walking across the bank, you see a man. \nHe requires something to get water for his family. \nMaybe we could help',
          Examination: 'examine',
          CompleteDescription: 'Hello',
          Solved: False,
          Solved2: False,
          Up: 'a2',
          Down: 'a2',
          Left: 'b1',
          Right: 'b3',
          Item: 'Bone', #for waterfall
          ItemNeeded: 'jug'

    },
    'b3': {
          ZoneName: 'Waterfall',
          Description: 'While atop of the waterfall, you see a woman screaming for her child. \n Her crying seems to mean she fears the worst.',
          CompleteDescription: 'Hello',
          Examination: 'examine',
          Solved: False,
          Solved2: False,
          Up: 'a3',
          Down: 'a3',
          Left: 'b2',
          Right: 'b4',
          Item: 'Wooden plank', # for hellish
          ItemNeeded: 'Bone'
    },
    'b4': {
          ZoneName: 'Highgarden',
          Description: 'A beautiful place where only the wealthiest live.\n covered in healthy farmland and large castles, it would be a dream to live here.',
          CompleteDescription: 'Hello',
          Solved: False,
          Solved2: False,
          Up: 'a4',
          Down: 'a4',
          Left: 'b3',
          Right: 'b1',
          Item: 'glasses',#for home
          ItemNeeded: 'Mystical fiery bolt'
          },

}
#shows where you are
def showLocation():
    print("#" * (25 + len(ZoneMap[myPlayer.location][ZoneName])))
    print("You have now made it to", ZoneMap[myPlayer.location][ZoneName], ".")
    print("#" * (25 + len(ZoneMap[myPlayer.location][ZoneName])))

def playerInspection():
    if solved_places[myPlayer.location] == True:
        print("\n############################\n")
        print("# ", ZoneMap[myPlayer.location][Description], " #")
        print("\n############################\n")
    else:
        print("Everything seems normal here")

def playerInput():
    print("What do you want to do?")
    task = input(">> ")
    possibleTasks = ['go', 'inventory', 'look', 'inspect', 'use', 'help', 'pick up', 'quit']
    while task.lower() not in possibleTasks:
        print("You cant do that")
        task = input(">>")

    if task.lower() == "inventory":
        playerInventory()

    elif task.lower() == "quit":
        sys.exit(0)

    elif task.lower() == "go":
        move(task.lower())

    elif task.lower() in ['look', 'inspect']:
        playerInspection()

    elif task.lower() == "use":
        playerUse()

    elif task.lower() == "pick up":
        playerPickUp()

    elif task.lower() == "help":
        print("you can do..'go', 'inventory', 'look', 'inspect', 'use', 'help', 'pick up', 'quit'")
        playerInput()

def playerInventory():
    print("\n", ("#" * (4 + len(Inventory))) + "\n")
    print("You have a", Inventory, "in your inventory")
    print("\n", ("#" * (4 + len(Inventory))) + "\n")


def move(myAction):
    print("Where would you like to "+myAction+" to?\n> ")
    where = input(">>")
    if where.lower() in ['north', 'up']:
        destination = ZoneMap[myPlayer.location][Up]
        playerMovement(destination)
    elif where.lower() in ['south', 'down']:
        destination = ZoneMap[myPlayer.location][Down]
        playerMovement(destination)
    elif where.lower() in ['west', 'left']:
        destination = ZoneMap[myPlayer.location][Left]
        playerMovement(destination)
    elif where.lower() in ['east', 'right']:
        destination = ZoneMap[myPlayer.location][Right]
        playerMovement(destination)
    else:
        print("You cant do that, either north, south, west or east")
        where = input(">>")

def helpMenu():
    print("This is my amazing game, you can do play, help or quit")
    print("While playing you can do...'go', 'inventory', 'look', 'inspect', 'use', 'help', 'pick up', 'quit'")
    menuScreen()

def playerPickUp():
    global InventroryFull

    if InventroryFull == False:
        if ZoneMap[myPlayer.location][Solved2] == False:
            print("You picked up", ZoneMap[myPlayer.location][Item], "\nMaybe this could be used somewhere")
            Inventory.append(ZoneMap[myPlayer.location][Item])
            ZoneMap[myPlayer.location][Solved2] = True
            InventroryFull = True
            return InventroryFull
        else:
            print("You have already used this item!")
    else:
        print("You are already holding an item!")

def playerUse():
    global InventroryFull
    global Solutions

    if ZoneMap[myPlayer.location][ItemNeeded] in Inventory:
        print(ZoneMap[myPlayer.location][CompleteDescription])
        Inventory.remove(ZoneMap[myPlayer.location][ItemNeeded])
        InventroryFull = False
        ZoneMap[myPlayer.location][Solved] == True
        Solutions = Solutions + 1
        if ZoneMap[myPlayer.location][ZoneName] == 'Town Hall':
            Town_Hall()
        elif ZoneMap[myPlayer.location][ZoneName] == 'Home':
            Home_Text()
        elif ZoneMap[myPlayer.location][ZoneName] == 'Hellish Path':
            Hellish_Path()
        elif ZoneMap[myPlayer.location][ZoneName] == 'Unknown place':
            Unknown_Place()
        elif ZoneMap[myPlayer.location][ZoneName] == 'City cells':
            City_Cells()
        elif ZoneMap[myPlayer.location][ZoneName] == 'River':
            River_Text()
        elif ZoneMap[myPlayer.location][ZoneName] == 'Waterfall':
            Waterfall_Text()
        elif ZoneMap[myPlayer.location][ZoneName] == 'Highgarden':
            Highgarden_Text()
        if Solutions == 8:
            GameOver()

    if ZoneMap[myPlayer.location][Solved] == True:
        print("You have already helped here!")

    else:
        print(Inventory, "Is not used here")

def playerMovement(destination):
    myPlayer.location = destination
    showLocation()

def gamePlay():
    while myPlayer.GameOver == False:
        playerInput()

def startGame():
    firstQuestion = "What is your name?"
    for character in firstQuestion:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    playerName = input(">>")
    myPlayer.name = playerName

    intro1 = "This is a world where everything makes logical sense.\n"
    intro2 = "Dont question anything\n"
    intro3 = "Lets go.\n"
    for character in intro1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in intro2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in intro3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    gamePlay()


intro()
