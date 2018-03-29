import mysql.connector
import secrets as db
def mySqlCon():
    return mysql.connector.connect(user=db.getUserName(), database='pokemon')
def createUser(name, gen):
    cursor = mySqlCon().cursor(buffered=True)
    insertString = "INSERT INTO `trainers` (`tID`, `tName, `tGender, `towns_townID`) VALUES (NULL, %s, %s, '0')"
    cursor.execute(insertString, (name, gen))
    return 0
