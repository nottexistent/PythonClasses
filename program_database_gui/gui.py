'''
Name: Jordyn Kuhn
Date: 3/2/23
CRN: 23199
CIS 226: Advanced Python Programming
'''
import PySimpleGUI as sg
from vegetables import Vegetables
 
#creates the gui
class Gui:
    #starts the menu and layout
    def __init__(self):

        #menu
        self.menu = [
            ['&File', ['&Quit']],
            ['&Help', ['&About...',]]
        ]

        #layout
        self.layout = [
            [sg.Menu(self.menu)],
            [sg.Text("Vegetable Database", key = 'title', border_width=3)],
            [sg.Text("  Type in a vegetable and an amount to add or change a vegetable:", key = 'inst')],
            [sg.Text('      Vegetable Name:   '), sg.Input(key = 'vegetable')],
            [sg.Text('      Vegetable Amount:'), sg.Input(key = 'quantity')],
            [sg.Text('   '), sg.Button('Add'), sg.Text('   '), sg.Button('Delete')],
            [sg.Text('  Or Press the button to see all vegetable values:')],
            [sg.Text('   '), sg.Button('See All Values')],
            [sg.Text()],
            [sg.Text('   '), sg.Button('Quit')],
            [sg.StatusBar('Waiting for input', key = 'status', size = (10,1))]
        ]

        self.veg = Vegetables()

    #Keeps the window open and interacts with input
    def window(self):
        #creates the window
        window = sg.Window('Vegetable Database', self.layout)

        #keeps the window open
        while True:
            event, values = window.read()
            print((event, values))

            if event ==  sg.WINDOW_CLOSED or event =='Quit':
                break

            elif event == 'About...':
                sg.popup("About Vegetable Database:", 
                '''
                \nTo add a vegetable to the database type in a vegetable and a quantity into the boxes.
                \nThen hit add, it will then update the status to tell you whether it was successfully added
                \nand what it added.
                \nTo delete a vegetable type in the vegetable name and then hit delete.
                \nTo show all vegetables hit show all, a popup will open showing all the vegetables and 
                \nquantities currently in the database. 
                \nTo quit hit quit.
                ''')

            elif event == 'See All Values':
                window['status'].update('Showing all values')
                sg.popup(str(self.veg.show_all()))

            elif values["vegetable"] != '' and values['quantity'] != '':
                    if event == "Add":
                        out = self.veg.add_vegetable(values['vegetable'], values['quantity'])
                        window['status'].update(out)

            elif event == "Delete" and values['vegetable'] != '':
                        out = self.veg.del_vegetable(values['vegetable'])
                        window['status'].update(out)

            else:
                window['status'].update('Please enter vegetable name and quantity or press Show All Values')

            #updates the window