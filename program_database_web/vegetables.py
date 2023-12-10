'''
Name: Jordyn Kuhn
Date: 3/2/23
CRN: 23199
CIS 226: Advanced Python Programming
'''

import sqlite3

#Vegetables
class Vegetables:
    #initialize
    def __init__(self, conn):
        self.conn = conn
        self.c = self.conn.cursor()

    #Create the table
    def setup(self):
        self.c.execute("CREATE TABLE IF NOT EXISTS vegetables (name text, quantity)")
        self.conn.commit()
    
    #Show all values in the table
    def show_all(self):
        for row in self.c.execute("SELECT * FROM vegetables"):
            yield row

    #Add or update a vegetable value
    def add_vegetable(self, name, quantity):
        quantity = int(quantity)
        exists = self.find_vegetable(name)

        if exists:
            self.c.execute("UPDATE vegetables SET quantity=? WHERE name=?", [quantity, name])
        else:
            self.c.execute("INSERT INTO vegetables VALUES (?, ?)", [name, quantity])

        self.conn.commit()
        
    #Finds a vegetable
    def find_vegetable(self, name):
        self.c.execute("SELECT name, quantity FROM vegetables WHERE name = ?", [name])
        return self.c.fetchone()
    
    #Delete vegetable
    def del_vegetable(self, name):
        exists = self.find_vegetable(name)
        if exists:
            self.c.execute("DELETE FROM vegetables WHERE name = ?", [name])
            self.conn.commit()
            return "{} was successfully removed.".format(name)
        else:
            return("{} is not in table.".format(name))
        