'''
Name: Jordyn Kuhn
Date: 2/25/23
CRN: 23199
CIS 226: Advanced Python Programming
'''

import sqlite3

#Vegetables
class Vegetables:
    #initialize
    def __init__(self):
        self.conn = sqlite3.connect('my_data.db')
        self.c = self.conn.cursor()

    #Create the table
    def setup(self):
        self.c.execute("CREATE TABLE IF NOT EXISTS vegetables (name text, quantity)")
    
    #Show all values in the table
    def show_all(self):
        for row in self.c.execute("SELECT * FROM vegetables"):
            print(row)

    #Add or update a vegetable value
    def add_vegetable(self, name, quantity):
        quantity = int(quantity.strip() or "0")
        exists = self.find_vegetable(name)

        if exists:
            self.c.execute("UPDATE vegetables SET quantity=? WHERE name=?", [quantity, name])
        else:
            self.c.execute("INSERT INTO vegetables VALUES (?, ?)", [name, quantity])

        print('Successfully added {} {} to the table.'.format(quantity, name))

    #Finds a vegetable
    def find_vegetable(self, name):
        self.c.execute("SELECT name, quantity FROM vegetables WHERE name = ?", [name])
        return self.c.fetchone()
    
    #Delete vegetable
    def del_vegetable(self, name):
        exists = self.find_vegetable(name)
        if exists:
            self.c.execute("DELETE FROM vegetables WHERE name = ?", [name])
            print("{} was successfully removed.".format(name))
            return "{} was successfully removed.".format(name)
        else:
            print("{} is not in table.".format(name))

    def menu(self):
        run = True

        while run:
            print('''
                \n    1) Show all Vegetables
                \n    2) Add or Change the Quantity of a Vegetable
                \n    3) Get the Quantity of a Vegetable
                \n    4) Delete a Vegetable
                \n    69) Quit
                ''')
            
            choice = input("\n:")

            if choice == '1':
                self.show_all()

            if choice == '2':
                name = input("\nWhat is the name of the vegetable? ")
                quantity = input("\nWhat is the quantity of the vegetable? ")
                self.add_vegetable(name, quantity)
                self.conn.commit()

            if choice == '3':
                name = input("\nWhat is the name of the vegetable? ")
                print(self.find_vegetable(name))

            if choice == '4':
                name = input("\n What is the name of the vegetable? ")
                self.del_vegetable(name)
                self.conn.commit()

            if choice == '69':
                self.conn.close()
                print("Goodbye")
                run = False

