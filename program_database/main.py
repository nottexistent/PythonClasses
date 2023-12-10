'''
-----DESIGN-----
I will solve the problem by learning about SQL and using it to make
a table with vegetables.
I solved the problem by creating a program that makes a table, allows
users to add to, remove from, find, and show all of the table.
I tested by making sure that the functions worked correctly and
displayed correctly.
My code creates a table and then allows a user to show all,
add or change a vegetable in the table, get the quantity of a vegetable.
'''
'''
-----USER DOCUMENTATION-----
Type in the corresponding number from the menu to do that action.
1 shows all of the values in the table.
2 allows you to add a value (if not already in table), and change
a value (if it is already in the table).
3 gets the quantity of an inputted vegetable.
4 deletes a given vegetable.
0 quits the progrma.

'''
'''
Name: Jordyn Kuhn
Date: 2/25/23
CRN: 23199
CIS 226: Advanced Python Programming
Time Estimate: 2 hours
'''

import sqlite3
from vegetables import Vegetables

#runs the vegetables
def main():
    veg = Vegetables()
    veg.setup()
    veg.menu()


if __name__ == '__main__':
    main()