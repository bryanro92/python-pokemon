import mysql.connector
from app import secrets as db
def mySqlCon():
    return mysql.connector.connect(user=db.getUserName(), database='pokemon')

def createUser(name, gen):
    con = mySqlCon()
    cursor = con.cursor()
    string = "INSERT INTO `trainers` (`tID`, `tName`, `tGender`, `towns_townID`, `numberOfPokemon`) VALUES (NULL,'"+name+"', '"+gen+"', '0','0')"
    cursor.execute(string)
    con.commit()
    message = "\nWelcome to the pokemon world "+name+"."
    print(message)
    cursor.close()
    con.close()
    message = "Your trainer identification number is:\n\t"+str(getNewtID())+"\nDon't forget this! It will be used to track your progress.\n"
    incrementTrainerCatchCount(getNewtID())
    return message

def getNewtID():
    con = mySqlCon()
    cursor = con.cursor()
    query = "select tID from trainers where tID=(select max(tID) from trainers)"
    cursor.execute(query)
    tList = cursor.fetchone()
    tID = tList[0]
    cursor.close()
    con.close()
    return tID

def currentUser(tID):
    con = mySqlCon()
    cursor = con.cursor()
    cursor.execute("select tName from trainers where tID like "+tID)
    nameList = cursor.fetchone()
    name = nameList[0]
    cursor.close()
    con.close()
    return name

def returnItemCount(tID):
    con = mySqlCon()
    cursor = con.cursor()
    query = "select itemNum from trainers_has_items where tID like "+str(tID)
    cursor.execute(query)
    count = cursor.fetchall()
    return len(count)

def returnTrainerCatchCount(tID):
    con = mySqlCon()
    cursor = con.cursor()
    cursor.execute("select numberOfPokemon from trainers where tID like "+str(tID))
    result = cursor.fetchone()
    cursor.close()
    con.close()
    return result[0]

def incrementTrainerCatchCount(tID):
    con = mySqlCon()
    cursor = con.cursor()
    count = returnTrainerCatchCount(tID)
    count = count+1
    query = "UPDATE trainers set numberOfPokemon = "+str(count)+" where tID = "+str(tID)
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()
    return count

def returnPokemonIDforTrainer(pID, tID):
    con = mySqlCon()
    cursor = con.cursor()
    query = "Select wild_pokemon_pID from wild_pokemon_caught_by_trainers where trainers_tID like "+tID+ " and pokemonID like "+pID

    cursor.execute(query)
    poke = cursor.fetchone()
    cursor.close()
    con.close()
    return poke[0]
