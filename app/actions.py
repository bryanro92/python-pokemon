from app import database as db
import random


def listCaughtPokemon(tID):
    con = db.mySqlCon()
    cursor = con.cursor()
    query = "select * from wild_pokemon_caught_by_trainers where trainers_tID like "+str(tID)
    result = cursor.fetchall(cursor.execute(query))
    print (result)
    cursor.close()
    con.close()

def listLocation(tID):
    con = db.mySqlCon()
    cursor = con.cursor()
    print("tid: ", tID)
    query = "select towns_townID from trainers where tID like "+str(tID)
    cursor.execute(query)
    result = cursor.fetchone()
    print ("town result: ", result[0])
    print ("town name: ", tID2Name(result[0]))
    cursor.close()
    con.close()
    return result[0]

def tID2Name(tID):
    con = db.mySqlCon()
    cursor = con.cursor()
    query = "select townName from towns where townID like "+str(tID)
    cursor.execute(query)
    result = cursor.fetchone()
    print("town name2: ", result[0])
    cursor.close()
    con.close()
    return result[0]

def listLocalPokemon(tID):
    location = listLocation(tID)
    print("location = ",location)
    query = "SELECT wild_pokemon_pID from wild_pokemon_found_in_towns where towns_townID like "+str(location)
    con = db.mySqlCon()
    cursor = con.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    print("results of local pokemon: ",result)
    cursor.close()
    con.close()
    for poke in result:
        print(pokeID2Name(poke[0]))
    return 0

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
    return choice

def listTowns():
    con = db.mySqlCon()
    cursor = con.cursor()
    cursor.execute("SELECT townName from towns")
    result = cursor.fetchall()
    for city in result:
        print("", city)
    return result

def travel(location):

    return
