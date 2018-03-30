import database as db
import mysql.connector

#Global Variables
story = """
Welcome to the adventurous world of Pokemon\n
Here your goal is to catch as many pokemon that you can, and\n
train them to become a Pokemon master! As you advance through your story\n
you will be able to battle Gym Leaders and other trainers to level up your pokemon. \n

"""

def storyString():
    return story


def askIfNew():
    prompt = "Press:\n\t1 if you are a new trainer\n\t2 if you are an existing trainer: "
    ans = input(prompt)
    if ans == "1":
        print("Please enter a name to create your Pokemon trainer ")
        name = input("Trainer Name: ")
        gen = input("Trainer Gender: ")
        print(db.createUser(name, gen))
        return
    if ans == "2":
        name = input("\nPlease enter your trainer ID number: ")
        print("Welcome back "+db.currentUser(name)+"!\n")
        print("The journey continues...\n\n")
        return
    if ans =="exit":
        exit(0)
    else:
        print("\nType 'exit' to quit or\n")
        askIfNew()
    return

def mySqlCon():
    return mysql.connector.connect(user=db.getUserName(), database='pokemon')

def main():
    print (storyString())
    askIfNew()


if __name__ == "__main__":
    main()





