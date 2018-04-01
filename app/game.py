from app import database as db
from app import actions as act
from app import settings
story = """
Welcome to the adventurous world of Pokemon\n
Here your goal is to catch as many pokemon that you can, and\n
train them to become a Pokemon master! As you advance through your story\n
you will be able to battle Gym Leaders and other trainers to level up your pokemon. \n

"""
over = False

def init():
    settings.gameOver = False
def storyString():
    return story

def connectedTowns():
    return

def askIfNew():
    settings.gameOver = False
    prompt = "Press:\n\t1 if you are a new trainer\n\t2 if you are an existing trainer: "
    ans = input(prompt)
    if ans == "1":
        print("Please enter a name to create your Pokemon trainer ")
        name = input("Trainer Name: ")
        gen = input("Trainer Gender: ")
        print(db.createUser(name, gen))
        settings.trainerID = db.getNewtID()
        return
    if ans == "2":
        name = input("\nPlease enter your trainer ID number: ")
        settings.trainerID = name
        print("Welcome back "+db.currentUser(name)+"!\n")
        print("The journey continues...\n\n")
        return
    elif ans =="exit":
        settings.gameOver = True
        exit(0)
    else:
        print("\nType 'exit' to quit or\n")
        askIfNew()
    return

def actions():
    msg = """
    Press:\n\t1 to list your current pokemon party
    \t2 to list your current location
    \t3 to list pokemon that can be found at current location
    \t4 to list available towns
    \t5 to travel to a new location
    \tto attempt to catch a wild pokemon
    \texit to exit
    """
    prompt = (msg)
    ans = input(prompt)
    print("\n")
    if ans == "1":
        act.listCaughtPokemon(settings.trainerID)
    if ans == "2":
        act.listLocation(settings.trainerID)
    if ans == "3":
        act.listLocalPokemon(settings.trainerID)
    if ans == "4":
        act.listTowns()
    if ans == "5":
        #act.catchPokemon(settings.trainerID)
        act.travel(settings.trainerID)


