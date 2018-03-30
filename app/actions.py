from app import database as db
import random


def listCaughtPokemon(tID):
    con = db.mySqlCon()
    cursor = con.cursor()
    query = "select * from wild_pokemon_caught_by_trainers where trainers_tID like "+str(tID)
    result = cursor.execute(query)
    print (result)
    cursor.close()
    con.close()

def listLocation(tID):

    return

def listLocalPokemon(tID):
    location = listLocation(tID)
    query = "SELECT * from wild_pokemon_found_in_towns where towns_townID like "+str(location)
    con = db.mySqlCon()
    cursor = con.cursor()
    result = cursor.execute(query)
    print(result)
    cursor.close()
    con.close()
    return

def catchPokemon(tID):
    pokeList = listLocalPokemon(tID)
    choice = pokeList[random.randrange(len(pokeList)-1)]
    return choice


def travel(location):

    return
