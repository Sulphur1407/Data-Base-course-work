"""
Ось тут розписані функції на кнопках
"""
import datetime

import mysql.connector
import interface

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="abunaraze",
    database="db_sol"
)

mycursor = mydb.cursor()
"""
sqlFormula = "DELETE FROM type_of_defect WHERE id_type_of_defect = %s"
request1 = (4, "aboba")

mycursor.execute(sqlFormula, (4,))
mydb.commit()
"""


def get_sizes():
    mycursor.execute("SELECT DISTINCT size FROM Shoes_variant ORDER BY size")
    result = mycursor.fetchall()
    sizes = []
    for sequence in result:
        sizes.append(sequence[0])
    return sizes


def get_fashions():
    mycursor.execute("SELECT DISTINCT fashion FROM Shoes_variant ORDER BY fashion")
    result = mycursor.fetchall()
    fashions = []
    for sequence in result:
        fashions.append(sequence[0])
    return fashions


def get_data():
    if not interface.com_mount.get():
        pass # Error
    if not interface.com_year.get():
        pass # Error

    mount = interface.com_mount.get()
    year = interface.com_year.get()
    print(mount, year)