'''
-----DESIGN-----
I will solve the problem by creating a search and sort program
with different gui elements.
I solved the problem by creating a search and sort program
with different gui elemets, text box, buttons, and dialog.
I tested by making sure that each individual element worked
and that the output was as expected.
My code takes a user inputted list and sorts it then finds the 
number and then prints the position in the sorted list.

'''
'''
-----USER DOCUMENTATION-----
Type in the list you want sorted and searched through
in the first box, separating each number with commas. 
Then type in the number you want to find in the second 
box. 
The program will then print out your list, your list sorted,
the number you were searching for, and whether it found it or
not and where it found it.

'''
'''
Name: Jordyn Kuhn
Date: 2/16/23
CRN: 23199
CIS 226: Advanced Python Programming
Time Estimate: 4 hours
'''
from gui import Gui

#Main
def main():
    newgui = Gui()
    newgui.window()

if __name__ == '__main__':
    main()