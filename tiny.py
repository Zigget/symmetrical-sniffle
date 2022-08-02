import PySimpleGUI as sg
# from functionality import *
import hashlib as hash
import random
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sys
import os
import itertools

if len(sys.argv) == 1:
    event, fnames = sg.Window('Select File(s) you wish to plot.').Layout([[sg.Text('Note, select multiple files by holding ctrl and clicking the number required.')],
                                                                          [sg.Input(key='_FILES_'), sg.FilesBrowse()], 
                                                                          [sg.OK(), sg.Cancel()]]).Read(close=True) # Add Ok and Cancel buttons
    # Close the window if cancel is pressed
    if event in (sg.WIN_CLOSED, 'Cancel'):
        exit()
else:
    # Check to see if any files were provided on the command line
    fnames = sys.argv[1]

# If no file names are selected, exit the program as these are required
if not fnames['_FILES_']:
    sg.popup("Cancel", "No filename supplied")
    raise SystemExit("Cancelling: no filename supplied")

fnames = fnames['_FILES_'].split(';')
# Count the number of files provided
no_files = len(fnames)
# List the available colours for the plots. More can be added to this list
matplotlib_colours = ["dodgerblue", "indianred", "gold", "steelblue", "tomato", "slategray", "plum", "seagreen", "gray"]
# List the line-styles you want. More can be added to this list
matplotlib_linestyles = ["solid", "dashed", "dashdot", "dotted"]
# The text of the headings for the drop-down menus
headings = ['X,Y INDICES', '  TYPE', 'COLOUR','LINE', '  LEGEND']

layout = [  [sg.Text('You can use LaTeX math code for axis labels and legend entries, e.g. $\mathbf{r}$', font=('Courier', 10))],
            [sg.Text('To use regular text in math mode use $\mathrm{Text}$\n')],
            [sg.Text('_'  * 100, size=(100, 1))], # Add horizontal spacer  
            [sg.Text('X-axis label:'), 
              sg.InputText('')],
            [sg.Text('Y-axis label:'), 
              sg.InputText('')],
            [sg.Text('_'  * 100, size=(100, 1))], # Add horizontal spacer  
            [sg.Text('                                        ')] + [sg.Text(h, size=(11,1)) for h in headings],  # build header layout
            *[[sg.Text('File: {}'.format(os.path.basename(os.path.normpath(i))), size=(40, 1)), 
               sg.InputText('X', size=(5, 1)),
               sg.InputText('Y', size=(5, 1)),
               sg.InputCombo(values=('point', 'line')),
               sg.InputCombo(values=(matplotlib_colours)),
               sg.InputCombo(values=(matplotlib_linestyles)),
               sg.InputText('Enter Legend Label', size=(20, 1)),
              ] for i in fnames
             ],
            [sg.Text('_'  * 100, size=(100, 1))], # Add horizontal spacer
            [sg.Button('Plot'), sg.Button('Cancel')],
         ]

window = sg.Window('Plot v1-01', layout)
# Read in the events and values       
event, values = window.read()
# If cancel is pressed then close the window and exit
if event in (sg.WIN_CLOSED, 'Cancel'):
    exit()

window.close()
# def claim():
#     radio_choices = ['Hershey','Twix']
#     radio = [[sg.Radio(text, 1,key=text,font='Lucinda 12'),] for text in radio_choices]
#     layoutclaim = [[sg.Text('We\'re sorry to have you file a claim\non your beloved pet.',key='condolence',size=(30,2),font='Lucinda 11')]] + radio +[[sg.Button('Submit Claim',key='submit',font='Lucinda 12')],
#     [sg.Button('Back',key='back',font='Lucinda 12')]]
#     window = sg.Window('File a Claim',layoutclaim)

#     while True:
#         event,values = window.read()
#         if event == sg.WIN_CLOSED:
#             window.Close()
#             quit()
#         elif event == 'back':
#             window.Close()
#             print('back')
#         elif event == 'submit':
#             window.Close
#             for i in radio_choices:
#                 if values[i] == True:
#                     print(i)
#                     sg.popup_timed('Our deepest condolences for your {}.'.format(i))
            
# claim()

# dognames = ['Stax','Pringle','Twizzler','Crush','Hershey','Twix','Crunch','Fruit Loop','Skippy']
# for i in range(random.randrange(1,4)):
#     dog_name = random.choice(dognames)
#     dognames.remove(dog_name)
#     print(dog_name)

# def this():
#     username = 'ssidzyik'
#     password = 'MayFourth2019!'
#     conn = psycopg2.connect(conn_string) 
#     cursor = conn.cursor()

#     #Queries to Database
#     cursor.execute("SELECT username from login ;")
#     usernames = cursor.fetchall()
#     if str(username) in str(usernames):
#         cursor.execute("SELECT * from login where username = %s",(username,))
#         user = cursor.fetchone()
#         securepass = hash.pbkdf2_hmac('sha256',password.encode('utf-8'),bytes(user[3]),20000)
#         print(user[0],user[1])
#         if securepass == bytes(user[2]):
#             print('yay')
#         else:
#             print('boo')
#     else:
#         user = False
#     #Close connection to Database
#     conn.commit()
#     cursor.close()
#     conn.close()
# this()
# fname='Tom'
# lname='Test'
# add1='404 T st'
# add2=''
# add3=''
# city='Omaha'
# state='NE'
# zip=68404
# name='Tex'
# kind='Mixed Breed under 30 lbs.'
# age=3
# agent='1'
# user='ssidzyik'
# hashpass=b'\xb5\xaa\xe7\xa1x\x10/#\xa4\xfbu\x9e5n\x8a\x14\x9f)p\x1fJP8\x8fK\x1e\x16\xfe)\xd1\xc8\xd4'
# salt=b' z\xaa\xa1\x035\xea\x04\xc1W\xd2\xd2\x9e\xf6>\xcb\xf2\xc1\x0f\xd7\xf9D\xac\x10\x87\xa9@\xe3\x16\x83\xb1\xa5!V!\x81i\xd3\xd1^\x12\x0c\xe0\xa8\xd21\xe9r\x9cbbH\xb2\x82\xe7b\x19\xed\xbd\xc1\xd1\xed\x97P'

# this()
# population()


# createpol(fname,lname,add1,add2,add3,city,state,zip,name,kind,age,agent,user,hashpass,salt)
# city = random.choice(['Omaha','Lincoln','Grand Island','Bellevue','Ralston'])
# # print(city)


# password = 'MayFourth2019!'
# securepass = hash.pbkdf2_hmac('sha256',password.encode('utf-8'),salt,20000)
# if securepass == hashpass:
    # print(securepass)

# this = (1,)
# print(this[0])
# def passsecure(password):
#     salt = os.urandom(64)
#     securepass = hash.pbkdf2_hmac('sha256',password.encode('utf-8'),salt,20000)
#     return securepass,salt
# print(passsecure('this'))
# doggos = ['! Get Doggos','Get Doggos2']
# doggosstr =['{}'.format(dog) for dog in doggos]
# print(doggosstr)
# print('\n\n\n'.join(doggos))
# this = 68404
# print((str(this).isnumeric()))
# QT_ENTER_KEY1 = 'special 16777220'
# QT_ENTER_KEY2 = 'special 16777221'

# layout = [[sg.Text('Test of Enter Key use')],
#           [sg.Input(key='-IN-')],
#           [sg.Button('Button 1', key='-1-')],
#           [sg.Button('Button 2', key='-2-')],
#           [sg.Button('Button 3', key='-3-')]]

# window = sg.Window('My new window', layout, return_keyboard_events=True)
# while True:             # Event Loop
#     event, values = window.read()
#     if event == sg.WIN_CLOSED:
#         break
#     if event in ('\r', QT_ENTER_KEY1, QT_ENTER_KEY2):         # Check for ENTER key
#         # go find element with Focus
#         elem = window.find_element_with_focus()
#         if elem is not None and elem.Type == sg.ELEM_TYPE_BUTTON:       # if it's a button element, click it
#             elem.Click()
#         # check for buttons that have been clicked
#     elif event == '-1-':
#         print('Button 1 clicked')
#     elif event == '-2-':
#         print('Button 2 clicked')
#     elif event == '-3-':
#         print('Button 3 clicked')

# window.close()
# # -- -- Lays out the Home window -- --
# layout = [[sg.Text('''window 1''',font='Lucinda 20',size=(20,2),justification='c')],
#         [sg.Button('Login',key='login',size=(15,1),font='Lucinda 12')],
#         [sg.Button('Exit',font='Lucinda 12')]]
# window = sg.Window('Home',layout)

# # -- -- intiates the window -- --
# event,values = window.read()
# if event == 'Exit' or event == sg.WIN_CLOSED:
#     test = 'close'
# elif event == 'login':
#     test = 'login'

# def window1():
#     # -- -- Lays out the Home window -- --
#     layout1 = [[sg.Text('''window 1''',font='Lucinda 20',size=(20,2),justification='c')]]
#     layout = [[sg.Text('''window 1''',font='Lucinda 20',size=(20,2),justification='c')],
#             [sg.Button('Login',key='login',size=(15,1),font='Lucinda 12')],
#             [sg.Button('Exit',font='Lucinda 12')]]
#     window = sg.Window('Log in',layout1,alpha_channel=0)
#     window2 = sg.Window('Log in',layout,alpha_channel=0).finalize()
#     window2.SetAlpha(1)
#     window.Close()
#     window = window2

#     # -- -- intiates the window -- --
#     while True:
#         event,values = window.read()
#         if event == 'Exit' or event == sg.WIN_CLOSED:
#             window.Close()
#             return 'close'
#         elif event == 'login':
#             window.Close()
#             return 'login'

# def login():
#     # -- -- Lays out the Home window -- --
#     layout1 = [[sg.Text('''window 1''',font='Lucinda 20',size=(20,2),justification='c')]]
#     window = sg.Window('Log in',layout1,alpha_channel=0)
#     layout = [[sg.Text('''window 2''',font='Lucinda 20',size=(20,2),justification='c')],
#             [sg.Button('home',key='home',size=(15,1),font='Lucinda 12')],
#             [sg.Button('Exit',font='Lucinda 12')]]
#     window2 = sg.Window('Log in',layout,alpha_channel=0).finalize()
#     window2.SetAlpha(1)
#     window.Close()
#     window = window2

#     # -- -- intiates the window -- --
#     while True:
#         event,values = window.read()
#         if event == 'Exit' or event == sg.WIN_CLOSED:
#             window.Close()
#             return 'close'
#         elif event == 'home':
#             window.Close()
#             return 'home'

# while True:
#     match test:
#         case 'login':
#             test = login()
#         case 'home':
#             test = window1()
#         case 'close':
#             break
    