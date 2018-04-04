from app import database as db
import random


def listCaughtPokemon(tID):
    con = db.mySqlCon()
    cursor = con.cursor()
    query = "select * from wild_pokemon_caught_by_trainers where trainers_tID like "+str(tID)
    cursor.execute(query)
    result = cursor.fetchall()
    print (result)
    if len(result) < 1:
        print("You have not caught any pokemon!")
    else:
        print("here is all your pokemans: ")
        for poke in result:
            print("\t"+pokeID2Name(poke[0]))


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
        print("\t"+pokeID2Name(poke[0]))
    return result

def pokeID2Name(pID):
    con = db.mySqlCon()
    cursor = con.cursor()
    query = "select pName from wild_pokemon where pID like "+str(pID)
    cursor.execute(query)
    result = cursor.fetchone()
    return result[0]

def catchPokemon(tID):
    pokeList = listLocalPokemon(tID)

    choice = pokeList[random.randrange(len(pokeList)-1)]
    print(choice[0])
    print("A wild "+pokeID2Name(choice[0])+" has appeared!")
    ans = input("Press 1 to battle or 2 to run away!")
    if ans == "1":
        print("//TODO implement: battle")

    if ans == "2":
        print("run away")

    return

def wildPokemon(pID):
    pokemon = pokeID2Name(pID)
    if random.randRange(100) < 25:
        print("You did a thing! %s", pokemon)
    return


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
