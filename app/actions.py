from app import database as db
from app import settings
import random


def listCaughtPokemon(tID):
    con = db.mySqlCon()
    cursor = con.cursor()
    query = "select pokemonID from wild_pokemon_caught_by_trainers where trainers_tID like "+str(tID)
    cursor.execute(query)
    result = cursor.fetchall()
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
    query = "select personalName from wild_pokemon_caught_by_trainers where trainers_tID like "+str(settings.trainerID)+" and pokemonID like "+str(pID)
    cursor.execute(query)
    result = cursor.fetchone()
    return result[0]

def catchPokemon(tID):
    pokeList = listLocalPokemon(tID)

    choice = pokeList[random.randrange(len(pokeList)-1)]
    print("A wild "+wildPokeID2Name(choice[0])+" has appeared!")
    ans = input("Press 1 to battle or 2 to run away: ")
    if ans == "1":
        print("//TODO implement: battle")
        wildPokemon(choice[0])
    if ans == "2":
        print("run away")

    return

def listInventory():
    con = db.mySqlCon()
    cursor = con.cursor()
    query = "select items_itemID from trainers_has_items where tID like "+str(settings.trainerID)
    cursor.execute(query)
    results = cursor.fetchall()
    if len(results) < 1:
        print("Your inventory is empty!")
    else:
        print("Inventory: ")
        i = 1
        for item in results:
            print("\t"+str(i)+") "+ itemID2Name(item[0]))
            i=i+1

    return 0

def addItem2Inventory(itemID):
    inventorySize = db.returnItemCount(settings.trainerID)
    con = db.mySqlCon()
    cursor = con.cursor()
    query = "INSERT INTO `pokemon`.`trainers_has_items` (`itemNum`, `tID`, `items_itemID`) VALUES ('"+str(inventorySize+1)+"',"+str(settings.trainerID)+", '"+str(itemID)+"');"
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()
    return


def itemID2Name(iID):
    con = db.mySqlCon()
    cursor = con.cursor()
    query = "select itemName from items where itemID like "+str(iID)
    cursor.execute(query)
    result = cursor.fetchone()
    return result[0]

def trainerItemID2Name(iID):
    con = db.mySqlCon()
    cursor = con.cursor()
    query = "select items_itemID from trainers_has_items where itemNum like "+str(iID)
    cursor.execute(query)
    result = cursor.fetchone()
    return itemID2Name(result[0])

def giveItemToPoke():
    selection = pokeDetails()
    listInventory()
    item = input("Please select an item you'd like to give to "+trainerPokeID2Name(selection)+": ")
    print(trainerItemID2Name(item))
    query = "UPDATE wild_pokemon_caught_by_trainers SET `trainers_itemNum`='"+str(item)+"' WHERE `pokemonID`='"+str(selection)+"' and`trainers_tID`='"+str(settings.trainerID)+"';"
    con = db.mySqlCon()
    cursor = con.cursor()
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

    return

def returnPokesItem(pID):
    query = "select trainers_itemNum from wild_pokemon_caught_by_trainers where trainers_tID like "+str(settings.trainerID)+" and pokemonID like "+str(pID)
    con = db.mySqlCon()
    cursor = con.cursor()
    cursor.execute(query)
    results = cursor.fetchone()
    cursor.close()
    con.close()
    if results[0] == "None":
        return "No item"
    item = trainerItemID2Name(results[0])
    return item

def pokeUseItem(pID):
    print (returnPokesItem(str(pID)))
    return

def pokeDetails():
    listCaughtPokemon(settings.trainerID)
    selection = input("Select a pokemon to display its detailed information: ")
    con = db.mySqlCon()
    cursor = con.cursor()
    query = "select * from wild_pokemon_caught_by_trainers where pokemonID like "+str(selection)+" and trainers_tID like "+str(settings.trainerID)
    cursor.execute(query)
    results = cursor.fetchone()
    cursor.close()
    con.close()
    print("Pokemon, NickName, Level, current HP, MAX HP, item")
    if str(results[8]) == "None":
        print(str(wildPokeID2Name(results[1]))+", "+str(results[5])+", "+str(results[4])+", "+str(results[6])+", "+str(results[7]) + ", "+"none")
    else:
        print(str(wildPokeID2Name(results[1]))+", "+str(results[5])+", "+str(results[4])+", "+str(results[6])+", "+str(results[7]) + ", "+str(trainerItemID2Name(results[8])))
    return selection

def chooseStartingPokemon(tID):
    choice = input("Please select one of the following starting pokemon:\n\t1) Bulbasaur\n\t2) Charmander\n\t3) Squirtle\n\tchoice: ")
    name = input("Please enter a name for your Pokemon: ")
    if choice == "1":
        trainerCatchesPokemon(1,name)
        print("Bulbasaur! Great choice")
        return
    if choice == "2":
        trainerCatchesPokemon(4, name)
        print("Charmander! Fire up!")
        return
    if choice == "3":
        trainerCatchesPokemon(7,name)
        print("Squirtle squirt!")
        return
    return 0

def wildPokemon(pID):
    wildPokemon = wildPokeID2Name(pID)
    inBattle = True
    wildHP = 100
    listCaughtPokemon(settings.trainerID)
    ans = input("Select a Pokemon to send out: ")
    print(""+trainerPokeID2Name(ans)+"! I choose you!")

    while inBattle:
        ans = input("Press 1 to attempt to catch "+wildPokemon+", or 2 to attack: ")
        if ans == "1":
            print(wildPokemon+"'s health is "+str(wildHP))
            if wildHP > 50:
                rng = random.randrange(100)
            elif wildHP > 25:
                rng = random.randrange(50)
            else:
                rng = random.randrange(30)
            print("Your rng is: ", rng)
            if rng < 25:
                print(wildPokemon+" was captured!")
                if str(input("Press 1 to give your "+wildPokemon+" a nickname: ")) == "1":
                        name = input("Please enter a nickname for your "+wildPokemon+": ")
                else:
                    name = wildPokemon
                trainerCatchesPokemon(pID, name)
                inBattle = False
                return
        if ans == "2":
            print(wildPokemon+"'s health is "+str(wildHP))
            dmg = random.randrange(20)
            print("You do "+str(dmg)+" damage to "+wildPokemon)
            wildHP = wildHP - dmg
            if wildHP < 1:
                print(wildPokemon+" fainted!")
                inBattle = False
                return
    return 0

def trainerCatchesPokemon(pID, name):
    con = db.mySqlCon()
    cursor = con.cursor()
    if random.randrange(10) < 5:
        gender = "M"
    else:
        gender = "F"
    count = db.returnTrainerCatchCount(settings.trainerID)
    print("current count: "+str(count))
    query = "INSERT INTO `wild_pokemon_caught_by_trainers` (`pokemonID`, `wild_pokemon_pID`, `trainers_tID`, `pGender`, `pLevel`, `personalName`, `pokeHP`, `pokeHPMAX`) VALUES ("+str(count)+","+str(pID)+","+str(settings.trainerID)+", '"+gender+"', 1, '"+name+"',100,100)"
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()
    db.incrementTrainerCatchCount(settings.trainerID)
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
