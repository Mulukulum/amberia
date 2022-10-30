import sqlite3

from os.path import dirname
FilePath=dirname(__file__)+"\Data\Amber.db"     #Gets the path of the database
del dirname

Con=sqlite3.connect(FilePath)       #Creates the database file if it doesn't exist already and makes a connection
Cursor=Con.cursor()

Con.commit()
Con.close()