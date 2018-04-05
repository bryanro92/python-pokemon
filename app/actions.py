from app import database as db
from app import settings
import random


def listCaughtPokemon(tID):
    con = db.mySqlCon()
    cursor = con.cursor()
    query = "select pokemonID from wild_pokemon_caught_by_trainers where trainers_tID like "+str(tID)
    cursor.execute(query)
    result = cursor.fetchall()
    print (result)
    if len(result) < 1:
        print("You have not caught any pokemon!")
    else:
        print("here is all your pokemans: ")
        i = 1
        for poke in result:
            print("\t"+str(i)+") "+trainerPokeID2Name(poke[0]))
            i=i+1

    cursor.close()
    con.close()
    return

def listLocation(tID):
    con = db.mySqlCon()
    cursor = con.cursor()
    query = "select towns_townID from trainers where tID like "+str(tID)
    cursor.execute(query)
    result = cursor.fetchone()
    print ("Current location: ", tID2Name(result[0]))
    cursor.close()
    con.close()
    return result[0]

def tID2Name(tID):
    con = db.mySqlCon()
    cursor = con.cursor()
    query = "select townName from towns where townID like "+str(tID)
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    con.close()
    return result[0]

def listLocalPokemon(tID):
    location = listLocation(tID)
    query = "SELECT wild_pokemon_pID from wild_pokemon_found_in_towns where towns_townID like "+str(location)
    con = db.mySqlCon()
    cursor = con.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    con.close()
    print("Pokemon that can be found here: ")
    for poke in result:
        print("\t"+wildPokeID2Name(poke[0]))
    return result


def wildPokeID2Name(pID):
    con = db.mySqlCon()
    cursor = con.cursor()
    query = "select pName from wild_pokemon where pID like "+str(pID)
    cursor.execute(query)
    result = cursor.fetchone()
    return result[0]

def trainerPokeID2Name(pID):
    con = db.mySqlCon()
    cursor = con.cursor()
    query = "select personalName from wild_pokemon_caught_by_trainers where trainers_tID like "+settings.trainerID+" and pokemonID like "+str(pID)
    cursor.execute(query)
    result = cursor.fetchone()
    return result[0]

def catchPokemon(tID):
    pokeList = listLocalPokemon(tID)

    choice = pokeList[random.randrange(len(pokeList)-1)]
    print(choice[0])
    print("A wild "+wildPokeID2Name(choice[0])+" has appeared!")
    ans = input("Press 1 to battle or 2 to run away: ")
    if ans == "1":
        print("//TODO implement: battle")
        wildPokemon(choice[0])
    if ans == "2":
        print("run away")

    return

def chooseStartingPokemon(tID):
    return 0

def wildPokemon(pID):
    wildPokemon = wildPokeID2Name(pID)
    inBattle = True
    wildHP = 100
    listCaughtPokemon(settings.trainerID)
    ans = input("Select a Pokemon to send out: ")
    print(""+trainerPokeID2Name(ans)+"! I choose you!")

    #print(pokeID2Name(db.returnPokemonIDforTrainer(ans, settings.trainerID)))
    while inBattle:
        ans = input("Press 1 to attempt to catch "+wildPokemon+", or 2 to attack: ")
        if ans == 1:
            rng = random.randRange(100)
            print("Your rng is: ", rng)
            if rng < 25:
                print("You did a thing! %s", wildPokemon)
                return
        if ans == 2:
            print("battle logic!")
            wildHP = wildHP - random.randRange(20)
    return 0



def listTowns():
    con = db.mySqlCon()
    cursor = con.cursor()
    cursor.execute("SELECT townName from towns")
    result = cursor.fetchall()
    print("Towns you can travel to: ")
    i=0
    for city in result:
        print("\t"+str(i)+": "+city[0])
        i=i+1
    return result


def travel(tID):
    listTowns()
    ans = input("Please enter the number for the location you'd like to travel to: ")
    print(ans)
    con = db.mySqlCon()
    cursor = con.cursor()
    query = "UPDATE `pokemon`.`trainers` SET `towns_townID`='"+str(ans)+"' WHERE `tID`='"+str(tID)+"';"
    cursor.execute(query)
    con.commit()
    return
