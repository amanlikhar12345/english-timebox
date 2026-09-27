import mysql.connector

class Database :
    def connect(self):
        connection=mysql.connector.connect(host="localhost",user="root",password="Aman@7999",database="english_timebox")
        return connection