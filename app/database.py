import mysql.connector
import secrets as db
def mySqlCon():
    return mysql.connector.connect(user=db.getUserName(), database='pokemon')
def createUser(name, gen):
    con = mySqlCon()
    cursor = con.cursor()
    #insertString = "INSERT INTO `trainers` (`tID`, `tName, `tGender`, `towns_townID`) VALUES (25,'bill','m','0');"
    string = "INSERT INTO `trainers` (`tID`, `tName`, `tGender`, `towns_townID`) VALUES (NULL,'"+name+"', '"+gen+"', '0')"
    cursor.execute(string)
    con.commit()
    message = "Great! \nWelcome to the pokemon world "+name+"."
    cursor.close()
    con.close()
    return message

def currentUser(tID):
    con = mySqlCon()
    cursor = con.cursor()
    cursor.execute("select tName from trainers where tID like "+tID)
    nameList = cursor.fetchone()
    name = nameList[0]
    return name
