import mysql.connector

class Db_con:
    def __init__(self):
        pass

    def connect_to_db():
        try:
            my_db = mysql.connector.connect(
                host = "localhost",
                user = "hello",
                password = "Hello@123"
            )
            return my_db

        except:
            print("Unable to connect to DB")
            exit(0)
