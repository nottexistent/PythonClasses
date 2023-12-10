'''
-----DESIGN-----
I will solve the problem by creating a random number generator 
with different gui elements.
I solved the problem by creating a random number generator
with different gui elemets, text box, buttons, and dialog.
I tested by making sure that each individual element worked
and that the output was as expected.
My code randomly generates a number based on user input and 
has a nice gui.

'''
'''
-----USER DOCUMENTATION-----
It creates a random number and displays it at the top. 
Type in the box to set a range, and it'll pick any 
number between 0 and the inputted number.
If no number is inputted it will pick between
0 and 100.
Click "Random Number!" to get a random number.

'''
'''
Name: Jordyn Kuhn
Date: 1/29/23
CRN: 23199
CIS 226: Advanced Python Programming
Time Estimate: 4 hours
'''
import PySimpleGUI as sg
from gui import Gui

#runs the gui
def main():
    newgui = Gui()
    newgui.window()

if __name__ == '__main__':
    main()