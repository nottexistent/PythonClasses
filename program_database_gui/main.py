'''
-----DESIGN-----
I will solve the problem by creating a GUI for the vegetable database.
I solved the problem by creating a GUI for the vegetable database.
I tested by making sure it added, saved, and showed the vegtables and worked appropriately.
My code creates a vegetable database and allows users to add and show all vegetables in the database 
through a GUI.
'''
'''
-----USER DOCUMENTATION-----
To add a vegetable to the database type in a vegetable and a quantity into the boxes.
Then hit add, it will then update the status to tell you whether it was successfully added
and what it added.
To delete a vegetable type in the vegetable name and then hit delete.
To show all vegetables hit show all, a popup will open showing all the vegetables and 
quantities currently in the database. 
To quit hit quit.
'''
'''
Name: Jordyn Kuhn
Date: 3/2/23
CRN: 23199
CIS 226: Advanced Python Programming
Time Estimate: 3 hours
'''
from gui import Gui

#runs the vegetables
def main():
    gui = Gui()
    gui.window()


if __name__ == '__main__':
    main()