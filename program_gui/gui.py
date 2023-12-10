'''
Name: Jordyn Kuhn
Date: 1/29/23
CRN: 23199
CIS 226: Advanced Python Programming
'''
import PySimpleGUI as sg
import random
 
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
            [sg.Text("Hello there!", key = 1)],
            [sg.Text("Click the button for a random number.", key = 2)],
            [sg.Text("Range (Default is 100):", key = 3)],
            [sg.Input(key = 'Range')],
            [sg.Text(size = (40,1), key = 'Output')],
            [sg.Button('Random Number!', key = 'button')],
            [sg.Button('Quit')],
            [sg.StatusBar('Waiting for input', key = 'status', size = (10,1))]
        ]

        #default range
        self.range = 100

    #Update and change the screen
    def next_screen(self, window):
            window[1].update(("Your number is {}").format(self.randnum()))
            window[2].update("Click the button again for another random number.")
            window[3].update(("Range (Set at {}):").format(self.range))
            window['status'].update("Generated Number, waiting for input.")

    #Keeps the window open and interacts with input
    def window(self):
        #creates the window
        window = sg.Window('Random Number Generator', self.layout)

        #keeps the window open
        while True:
            event, values = window.read()
            print((event, values))

            if event ==  sg.WINDOW_CLOSED or event =='Quit':
                break

            elif event == 'About...':
                sg.popup("About Random Number Generator:", 
                '''It creates a random number and displays it at the top. 
                \nType in the box to set a range, and it'll pick any 
                \n number between 0 and the inputted number.
                \n If no number is inputted it will pick between
                \n 0 and 100.
                \nClick "Random Number!" to get a random number.''')

            else:
                if values['Range'] != '':
                    self.range = values['Range']
                    print (values['Range'])
                self.next_screen(window)

            #updates the window
            

    #creates the random number
    def randnum(self):
        return random.randint(0, int(self.range))

    def about_window(self):
        about_layout = [
            [sg.Text('''About Random Number Generator:
            \nIt creates a random number and displays it at the top. 
            \nType in the box to set a range, and it'll pick any 
            \n number between 0 and the inputted number.
            \n If no number is inputted it will pick between
            \n 0 and 100.
            \nClick "Random Number!" to get a random number.''')]
        ]

        about_window = sg.Window('About Random Number Generator', about_layout)

        while True:
            event, values = about_window.read()

            if event == sg.WINDOW_CLOSED or event =='Quit':
                break