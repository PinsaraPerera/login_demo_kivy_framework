import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="appdata"
)

mycursor = db.cursor()
# mycursor.execute("CREATE TABLE Users(user_name VARCHAR(50) PRIMARY KEY NOT NULL, email VARCHAR(50) NOT NULL,password VARCHAR(8) NOT NULL, created datetime NOT NULL) ")
