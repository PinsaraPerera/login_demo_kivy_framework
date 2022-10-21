import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="appdata"
)

Q1 = "CREATE TABLE if not exists Users(user_name VARCHAR(50) PRIMARY KEY NOT NULL," \
     " email VARCHAR(50) NOT NULL,password VARCHAR(8) NOT NULL, created datetime NOT NULL) "

mycursor = db.cursor()
mycursor.execute(Q1)
