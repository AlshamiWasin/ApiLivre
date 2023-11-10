import mysql.connector
import Conf.confDB as conf

mydb = mysql.connector.connect(
    host=conf.host,
    user=conf.user,
    password=conf.password,
    database=conf.database
)


mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM client")

# Fetch the result
result = mycursor.fetchall()

for row in result:
    print(row)



mydb.close()