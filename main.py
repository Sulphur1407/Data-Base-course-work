import datetime

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="abunaraze",
    database="db_sol"
)

mycursor = mydb.cursor()

sqlFormula = "DELETE FROM type_of_defect WHERE id_type_of_defect = %s"
request1 = (4, "aboba")

mycursor.execute(sqlFormula, (4,))

mydb.commit()
