import mysql.connector
import random

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="abunaraze",
    database="db_sol"
    )

mycursor = mydb.cursor()

mycursor.execute("SELECT DISTINCT size FROM Shoes_variant ORDER BY size")
result = mycursor.fetchall()
sizes = []
for sequence in result:
    sizes.append(sequence[0])

mycursor.execute("SELECT DISTINCT fashion FROM Shoes_variant ORDER BY fashion")
result = mycursor.fetchall()
fashions = []
for sequence in result:
    fashions.append(sequence[0])

"""
for year in (2020, 2021, 2022):
    for month in range(1, 13):
        for fashion in fashions:
            for size in sizes:

                date = str(year) + "-" + str(month) + "-1"

                GetIdFormula = "SELECT id_shoes_variant FROM shoes_variant WHERE fashion = %s and size = %s"

                mycursor.execute(GetIdFormula, (fashion, size))

                id_shoes_variant = mycursor.fetchone()[0]

                InsertNumber = "INSERT INTO plan_db VALUES(DEFAULT, %s, %s, %s)"
                # print((random.randint(200, 999), date, id_shoes_variant))
                mycursor.execute(InsertNumber, (random.randint(200, 999), date, id_shoes_variant))
"""

for fashion in fashions:
    for size in sizes:
        GetIdFormula = """SELECT id_Plan_DB
                          FROM plan_db
                          JOIN shoes_variant sv
                            USING (id_shoes_variant)
                          WHERE sv.fashion = %s and sv.size = %s
                            and MONTH(data) = %s and YEAR(data) = %s
                            """

        mycursor.execute(GetIdFormula, (fashion, size, 12, 2022))
        id_Plan_DB = mycursor.fetchone()[0]
        InsertDefective = """INSERT INTO accounting_for_defective_products
                             VALUES(DEFAULT, %s, 1, %s)
                             """

        mycursor.execute(InsertDefective, (random.randint(0, 188), id_Plan_DB))

mydb.commit()
