import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)


mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM client")

# Fetch the result
result = mycursor.fetchall()

for row in result:
    print(row)



mydb.close()