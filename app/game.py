from app import database as db
from app import actions as act
from app import settings
story = """
Welcome to the adventurous world of Pokemon
Here your goal is to catch as many pokemon that you can, and
train them to become a Pokemon master! As you advance through your story
you will be able to battle Gym Leaders and other trainers to level up your pokemon.

"""
def printIntro():
    intro = """
                                      ,'\
        _.----.        ____         ,'  _\   ___    ___     ____
    _,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
    \      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
     \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
       \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
        \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
         \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
          \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
           \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
            \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                    `'                            '-._|


    """
    print(intro)
    return

def printBye():
    msg = """
    `;-.          ___,
      `.`\_...._/`.-"`
        \        /      ,
        /()   () \    .' `-._
       |)  .    ()\  /   _.'
       \  -'-     ,; '. <
        ;.__     ,;|   > \
       / ,    / ,  |.-'.-'
      (_/    (_/ ,;|.<`
        \    ,     ;-`
         >   \    /
        (_,-'`> .'
             (_,'
    """
    print(msg)

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
        act.chooseStartingPokemon(settings.trainerID)
        return

    if ans == "2":
        name = input("\nPlease enter your trainer ID number: ")
        settings.trainerID = name
        print("Welcome back "+db.currentUser(name)+"!\n")
        print("The journey continues...\n\n")
        return
    elif ans =="exit":
        setGameOver(True)
        exit(0)
    else:
        print("\nType 'exit' to quit or\n")
        askIfNew()
    return

def setGameOver(bool):
    settings.gameOver = bool
    return settings.gameOver

def getGameOver():
    return settings.gameOver

def actions():
    msg = """
    Press:\n\t1 to list your current pokemon party
    \t2 to list your current location
    \t3 to list pokemon that can be found at current location
    \t4 to list available towns
    \t5 to travel to a new location
    \t6 to attempt to catch a wild pokemon
    \t7 to battle the gym leader in current town
    \t8 list inventory
    \t9 list details of a pokemon
    \t10 give item to pokemon
    \t-------------------------------------------
    \texit to exit the game
    """
    print(msg)
    ans = input("action: ")
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
        act.travel(settings.trainerID)
    if ans == "exit":
        setGameOver(True)
    if ans =="6":
        act.catchPokemon(settings.trainerID)
    if ans =="8":
        act.listInventory()
    if ans == "9":
        act.pokeDetails()
    if ans == "10":
        act.giveItemToPoke()


