from datetime import datetime

from connect import mycursor, db


class Database:
    def __init__(self, name, password, email=None):
        self.name = name
        self.email = email
        self.password = password

    def add_user(self):
        if self.get_user(self.name):
            new_user = [(self.name, self.email, self.password, datetime.now())]
            mycursor.execute("INSERT INTO Users(user_name, email, password, created) VALUES(%s,%s,%s,%s)", new_user[0])
            db.commit()
            return True
        else:
            return self.get_user(self.name)

    def validate_user(self):
        mycursor.execute("SELECT password FROM Users WHERE user_name = %s", (self.name,))
        result = mycursor.fetchall()
        if len(result):
            if result[0][0] == self.password:
                return True
            return False
        return False

    def get_user(self, new_username):
        mycursor.execute("SELECT user_name FROM Users WHERE user_name = %s", (new_username,))
        result = mycursor.fetchall()
        if not len(result):
            return True
        else:
            return False

# mycursor.execute("INSERT INTO Users(user_name, email, password, created) VALUES(%s,%s,%s,%s)", ("pinsara","gtfwug@gmail.com","1234567a", datetime.now()))
# db.commit()
