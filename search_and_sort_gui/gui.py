'''
Name: Jordyn Kuhn
Date: 1/29/23
CRN: 23199
CIS 226: Advanced Python Programming
'''
import PySimpleGUI as sg
from list import List
 
#Class to handle the GUI
class Gui:
    #starts the menu and layout
    def __init__(self):
        self.list_str = ''
        self.list = List()
        #menu
        self.menu = [
            ['&File', ['&Quit']],
            ['&Help', ['&About...',]]
        ]

        #layout
        self.layout = [
            [sg.Menu(self.menu)],
            [sg.Text("Hello there!", key = 'greet')],
            [sg.Text("Enter a list to sort through it (ex: 1,2,3,4): ", key = 'inst')],
            [sg.Input(key = 'list')],
            [sg.Text("Enter a number to search for it:", key = 'search')],
            [sg.Input(key = 'num')],
            [sg.Text('Output: ')],
            [sg.Text(size = (40,1), key = 'output1')],
            [sg.Text(size = (40,1), key = 'output2')],
            [sg.Text(size = (40,1), key = 'output3')],
            [sg.Text(size = (40,1), key = 'output4')],
            [sg.Button('Sort and Search!', key = 'button')],
            [sg.Button('Quit')],
            [sg.StatusBar('Waiting for input', key = 'status', size = (10,1))]
        ]

    #Update and change the screen
    def next_screen(self, window):
            self.list.reset_counts()
            window['output1'].update(("Your list unsorted is: {}").format(self.list.create_list(self.list_str)))
            window['output2'].update(("Your sorted list is: {}").format(self.list.sort_list()))
            window['output3'].update(("Searching for: {}").format(self.num))
            window['output4'].update(('Found: {}').format(self.list.search_list(self.num)))
            self.list.print_swap()

    #Keeps the window open and interacts with input
    def window(self):
        #creates the window
        window = sg.Window('Search and Sort', self.layout)

        #keeps the window open
        while True:
            event, values = window.read()
            print((event, values))

            if event ==  sg.WINDOW_CLOSED or event =='Quit':
                break

            elif event == 'About...':
                sg.popup("About Search and sort:", 
                '''Sorts a user provided list and searches through it 
                \nType in the box to set the list separating 
                \nthe numbers with commas, then type in the number
                \nyou're looking for in the list and then hit the button.
                \nThe program will then sort and search your list printing
                \nthe unsorted list, the sorted list, the number, and the 
                \nposition of the number''')

            else:
                if values['list'] != '' and values['num'] != '':

                    self.list_str = str(values['list'])

                    self.num = int(values['num'])

                    self.next_screen(window)
                else:
                    window['status'].update('Make sure to fill in both boxes')
            #updates the window