import sqlite3
Connector=sqlite3.connect("Amber.db")       #Creates the database file if it doesn't exist already
Cursor=Connector.cursor()