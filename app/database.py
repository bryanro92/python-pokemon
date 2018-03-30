import mysql.connector
from app import secrets as db
def mySqlCon():
    return mysql.connector.connect(user=db.getUserName(), database='pokemon')
def createUser(name, gen):
    con = mySqlCon()
    cursor = con.cursor()
    string = "INSERT INTO `trainers` (`tID`, `tName`, `tGender`, `towns_townID`) VALUES (NULL,'"+name+"', '"+gen+"', '0')"
    cursor.execute(string)
    con.commit()
    message = "Great! \nWelcome to the pokemon world "+name+"."
    cursor.close()
    con.close()
    message += message +"\n Your trainer identification number is:\n\t"+str(getNewtID())+"\nDon't forget this! It will be used to track your progress.\n"
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
