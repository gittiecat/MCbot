import sqlite3 as sl

class DatabaseClass:
    def __init__(self):
        self.con = sl.connect('discord-server.db')
        self.cursor = self.con.cursor()
        DatabaseClass.createDatabase(self)

    def createDatabase(self):
        # CREATE DATABASE IF DOESN'T EXIST
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS accounts
                (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                user TEXT,
                account TEXT
                );""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS bad_words
                (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                word TEXT,
                count INTEGER
                );""")