'''
All code was assembled by myself, Samuel Sidzyik.
I pulled bits and pieces from various sources but this code is my own.

sources referenced
https://www.pysimplegui.org/en/latest/cookbook/
https://github.com/PySimpleGUI/PySimpleGUI/issues/2298
https://github.com/PySimpleGUI/PySimpleGUI/issues/721
https://stackoverflow.com/questions/56261629/how-can-i-create-radio-buttons-from-a-list-using-pysimplegui
https://pysimplegui.trinket.io/demo-programs#/layouts/push-and-vpush-elements

I wanted to use this but didn't have time to fully implement it
https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Keyboard_ENTER_Presses_Button.py
https://adambaskerville.github.io/posts/PythonGUIPlotter/
'''
# -- -- imports for GUI, and functions from 'connected.py' -- --
import PySimpleGUI as sg
from functionality import *
# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd


# -- -- Visual Theme to GUI -- --
# https://icon-icons.com/download/89239/ICO/32/
# sns.set_style("darkgrid")
sg.theme('DarkTeal9')
sg.set_options(icon=r"C:\Users\Owner.P200219L\Desktop\C2C\Final\pawprint.ico",text_color='silver')


#-- -- Functions to Initiate each window -- --
#Home screen (done)
def startwindow():
    # -- -- Lays out the Home window -- --
    # -- -- creates placeholder window to be removed after the launch of the next window

    layout = [[sg.Text('''Sam\'s Doggo
    Life Insurance''',font='Lucinda 20',size=(20,2),justification='c')],
            [sg.Button('Login',key='login',size=(15,1),font='Lucinda 12'),sg.Button('Get a Quote',key='quote',size=(15,1),font='Lucinda 12')],
            [sg.Button('Exit',font='Lucinda 12')]]
    window = sg.Window('Home',layout)

    # -- -- opens the window and reads output -- --
    while True:
        event,values = window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            window.Close()
            quit()
        elif event == 'quote':
            window.Close()
            return 'quote'
        elif event == 'login':
            window.Close()
            return 'login'

#Quote Screen (done)
def quote():
    # -- -- Lays out the Home window -- --
    layoutquote = [[sg.Text('Doggo Name',key='dname',size=(11,1),font='Lucinda 12'),sg.Input(key='dogname',font='Lucinda 12',size=(20,1))],
    [sg.Text('Doggo Breed',key='pass',size=(11,1),font='Lucinda 12'),sg.Combo(['Mixed Breed under 15 lbs.','Mixed Breed under 30 lbs.','Mixed Breed under 65 lbs.','Mixed Breed under 110 lbs.','Mixed Breed over 110 lbs.'],key='kind',font='Lucinda 12',size=(20,1))],
    [sg.Text('Doggo Age',key='age',size=(11,1),font='Lucinda 12'),sg.Input(key='ageinput',font='Lucinda 12',size=(20,1))],
    [sg.Text('',key='space',size=(30,2),font='Lucinda 11',visible=False)],
    [sg.Button('Quote me',key='quote',font='Lucinda 12'),sg.Button('Back',key='back',font='Lucinda 12'),sg.Button('Apply for this policy!',key='approved',font='Lucinda 12',visible=False)],
    [sg.Button('Exit',font='Lucinda 12')]]
    window = sg.Window('Quote',layoutquote)
    
    while True:
        event,values = window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            window.Close()
            quit()
        # -- -- Actual Functionality -- --
        elif event == 'quote':
            window['space'].update(visible=True)
            cost = guiinsurability(values['kind'],int(values['ageinput']))
            if cost == 0:
                window['space'].update('Your dog is inelligble for life insurance',visible=True)
            else:
                window['space'].update('Your Doggo is eligible for life insurance!\nA policy is available for ${:.2f} per year!'.format(cost),visible=True)
                window['approved'].update(visible=True)
        elif event == 'back':
            window.Close()
            return 'start','pass','pass','pass'
        elif event == 'approved':
            window.Close()
            return 'signup',values['dogname'],values['kind'],values['ageinput']

#Signup after approved quote (done)
def signup(name,breed,age):
    layoutsignup = [[sg.Text('First Name',size=(15,1),font='Lucinda 12'),sg.Input(key='fname',font='Lucinda 12',size=(15,1))],
    [sg.Text(key='fnameerr',size=(35,1),font='Lucinda 10',visible=False,justification='r',text_color='red')],
    [sg.Text('Last Name',size=(15,1),font='Lucinda 12'),sg.Input(key='lname',font='Lucinda 12',size=(15,1))],
    [sg.Text(key='lnameerr',size=(35,1),font='Lucinda 10',visible=False,justification='r',text_color='red')],
    [sg.Text('Address1',size=(15,1),font='Lucinda 12'),sg.Input(key='add1',font='Lucinda 12',size=(15,1))],
    [sg.Text(key='add1err',size=(35,1),font='Lucinda 10',visible=False,justification='r',text_color='red')],
    [sg.Text('Address2',size=(15,1),font='Lucinda 12'),sg.Input(key='add2',font='Lucinda 12',size=(15,1))],
    [sg.Text('Address3',size=(15,1),font='Lucinda 12'),sg.Input(key='add3',font='Lucinda 12',size=(15,1))],
    [sg.Text('City',size=(15,1),font='Lucinda 12'),sg.Input(key='city',font='Lucinda 12',size=(15,1))],
    [sg.Text(key='cityerr',size=(35,1),font='Lucinda 10',visible=False,justification='r',text_color='red')],
    [sg.Text('State',size=(15,1),font='Lucinda 12'),sg.Input(key='state',font='Lucinda 12',size=(15,1))],
    [sg.Text(key='stateerr',size=(35,1),font='Lucinda 10',visible=False,justification='r',text_color='red')],
    [sg.Text('Zip',size=(15,1),font='Lucinda 12'),sg.Input(key='zip',font='Lucinda 12',size=(15,1))],
    [sg.Text(key='ziperr',size=(35,1),font='Lucinda 10',visible=False,justification='r',text_color='red')],
    [sg.Text('Username',size=(15,1),font='Lucinda 12'),sg.Input(key='userinput',font='Lucinda 12',size=(15,1))],
    [sg.Text(key='usererr',size=(35,1),font='Lucinda 10',visible=False,justification='r',text_color='red')],
    [sg.Text('Password',key='pass1',size=(15,1),font='Lucinda 12'),sg.Input(key='passinput',font='Lucinda 12',size=(15,1),password_char='*')],
    [sg.Text(key='pass1err',size=(35,1),font='Lucinda 10',justification='r',visible=False,text_color='red')],
    [sg.Text('''Must be: 8-16 characters
and contain alpha, numeric, and special key(s)''',key='passreq',size=(30,3),font='Lucinda 12')],
    [sg.Text('ReEnter Password',key='pass2',size=(15,1),font='Lucinda 12'),sg.Input(key='pass2input',font='Lucinda 12',size=(15,1),password_char='*')],
    [sg.Text(key='pass2err',size=(35,1),font='Lucinda 10',justification='r',visible=False,text_color='red')],
    [sg.Button('Create Policy',key='create',font='Lucinda 12'),sg.Button('Main Menu',key='back',font='Lucinda 12')],
    [sg.Button('Exit',font='Lucinda 12')]]
    
    window = sg.Window('Log in',layoutsignup)

    while True:
        event,values = window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            window.Close()
            quit()
        elif event == 'create':
            window['fnameerr'].update(visible=False)
            window['lnameerr'].update(visible=False)
            window['add1err'].update(visible=False)
            window['cityerr'].update(visible=False)
            window['stateerr'].update(visible=False)
            window['ziperr'].update(visible=False)
            window['usererr'].update(visible=False)
            window['pass1err'].update(visible=False)
            window['pass2err'].update(visible=False)
            sent,fname,lname,add1,city,state,zipp,username,pass1,pass2 = guisignup(name,breed,age,values['fname'],values['lname'],values['add1'],values['add2'],values['add3'],values['city'],values['state'],values['zip'],values['userinput'],values['passinput'],values['pass2input'])
            #Success
            if sent==True:
                sg.popup_timed("Thank you for trusting us with your pet's final cost.\nYour policy has been created and can be viewed by logging in.",auto_close_duration=5)
                window.Close()
                return 'login'
            #Failure
            else:
                if fname != values['fname']:
                    window['fnameerr'].update(fname)
                    window['fnameerr'].update(visible=True)
                if lname != values['lname']:
                    window['lnameerr'].update(lname)
                    window['lnameerr'].update(visible=True)
                if add1 != values['add1']:
                    window['add1err'].update(add1)
                    window['add1err'].update(visible=True)
                if city != values['city']:
                    window['cityerr'].update(city)
                    window['cityerr'].update(visible=True)
                if state != values['state']:
                    window['stateerr'].update(state)
                    window['stateerr'].update(visible=True)
                if zipp != values['zip']:
                    window['ziperr'].update(zipp)
                    window['ziperr'].update(visible=True)
                if username != values['userinput']:
                    window['usererr'].update(username)
                    window['usererr'].update(visible=True)
                if pass1 != values['passinput']:
                    window['pass1err'].update(pass1)
                    window['pass1err'].update(visible=True)
                if pass2 != values['pass2input']:
                    window['pass2err'].update(pass2)
                    window['pass2err'].update(visible=True)

        elif event == 'back':
            window.Close()
            return 'start'

#Login Screen (done - removed forgot pass)
def login():
    # -- -- Lays out and initiates new Window to Login -- --
    layoutlogin = [[sg.Text('Username',key='user',size=(15,1),font='Lucinda 12'),sg.Input(key='userinput',font='Lucinda 12',size=(15,1))],
    [sg.Text('Password',key='pass',size=(15,1),font='Lucinda 12'),sg.Input(key='passinput',font='Lucinda 12',size=(15,1),password_char='*')],
    [sg.Button('Login',key='login',font='Lucinda 12'),sg.Button('Back',key='back',font='Lucinda 12'),sg.Push(),sg.Text(key='error',font='Lucinda 12',size=(15,2))],
    [sg.Button('Exit',font='Lucinda 12')]]
    window = sg.Window('Log in',layoutlogin)

    while True:
        event,values = window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            window.Close()
            quit()
        elif event == 'login':
            user,access = guilogin(values['userinput'],values['passinput'])
            if user == values['userinput']:
                window.Close()
                return 'start',user,access
            else:
                window['error'].update('Incorrect username or password')
        elif event == 'back':
            window.Close()
            return 'start','pass','pass'
        elif event == 'forgot':
            return 'start','pass','pass'

#Home screen for Customers (done)
def customerscreen(user):
    customer = getcustomer(user)
    doglist = customer.dogs #! Get Doggos
    dogs = [[sg.Push(),sg.Text(text,font='Lucinda 12'),sg.Push()] for text in doglist]
    layoutcustomer = [[sg.Text('Welcome, {}'.format(customer.fname),key='user',size=(30,1),font='Lucinda 12',justification='c')],
    [sg.Text('Annual Premium',key='premium',size=(15,1),font='Lucinda 12'),sg.Text('${:,.2f}'.format(customer.premium),key='amount',size=(15,1),font='Lucinda 12')],
    #for loop for each dog!!!
    [sg.Text('Your covered pets:',key='pets',size=(15,1),font='Lucinda 12')]] + dogs + [[sg.Button('Add Doggo',key='add',font='Lucinda 12'),sg.Push(),sg.Button('File a Claim',key='claim',font='Lucinda 12')],
    [sg.Button('Remove Doggo',key='remove',font='Lucinda 12'),sg.Push(),sg.Button('Print Policy',key='print',font='Lucinda 12')],
    [sg.Push(),sg.Button('Logout',key='logout',font='Lucinda 12'),sg.Button('Exit',font='Lucinda 12'),sg.Push()]]
    window = sg.Window(customer.fname,layoutcustomer)

    while True:
        event,values = window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            window.Close()
            quit()
        else:
            if event == 'print':
                sg.popup_timed('A copy of your Policy has been created. Check your downloads folder.')
            window.Close()
            return event,customer

#Add pet screen for Customers (done)
def add(user,customer):
    layoutadd = [[sg.Text('Doggo Name',key='dname',size=(15,1),font='Lucinda 12'),sg.Input(key='userinput',font='Lucinda 12',size=(15,1))],
    [sg.Text('Doggo Breed',key='pass',size=(15,1),font='Lucinda 12'),sg.Combo(['Mixed Breed under 15 lbs.','Mixed Breed under 30 lbs.','Mixed Breed under 65 lbs.','Mixed Breed under 110 lbs.','Mixed Breed over 110 lbs.'],key='kind',font='Lucinda 12',size=(15,1))],
    [sg.Text('Doggo Age',key='age',size=(15,1),font='Lucinda 12'),sg.Input(key='ageinput',font='Lucinda 12',size=(15,1))],
    [sg.Text('',key='space',size=(30,2),font='Lucinda 11',visible=False)],
    [sg.Button('Quote me',key='quote',font='Lucinda 12'),sg.Button('Back',key='back',font='Lucinda 12'),sg.Button('Add your doggo',key='approved',font='Lucinda 12',visible=False)],
    [sg.Button('Exit',font='Lucinda 12')]]
    window = sg.Window('Add to your Pack',layoutadd)
    
    while True:
        event,values = window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            window.Close()
            quit()
        # -- -- Actual Functionality -- --
        elif event == 'quote':
            cost = guiinsurability(values['kind'],int(values['ageinput']))
            if cost == 0:
                window['space'].update('Your dog is inelligble for life insurance',visible=True)
            else:
                window['space'].update('Your Doggo is eligible for life insurance!\nA policy is available for ${:.2f} per year!'.format(cost),visible=True)
                window['approved'].update(visible=True)
        elif event == 'back':
            window.Close()
            return 'start', customer
        elif event == 'approved':
            customer = adddog(user,customer.policyno,values['userinput'],values['kind'],int(values['ageinput']))
            sg.popup_timed('Your pet {} has been added to your policy no.{}.'.format(values['userinput'],customer.policyno))
            window.Close()
            return 'start', customer

#Remove pet screen for Customers (done)
def remove(user,customer):
    radio_choices = customer.dogs
    radio = [[sg.Radio(text, 1,key=text),] for text in radio_choices]
    layoutrem = [[sg.Text('Select which doggo to remove from your policy.',key='condolence',size=(15,1),font='Lucinda 12')]] + radio +[[sg.Button('Remove',key='submit',font='Lucinda 12')],
    [sg.Button('Back',key='back',font='Lucinda 12')]]
    window = sg.Window('Remove Pet',layoutrem)

    while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED:
            window.Close()
            quit()
        elif event == 'back':
            window.Close()
            return 'start',customer
        elif event == 'submit':
            window.Close
            for i in radio_choices:
                if values[i] == True:
                    window.Close()
                    customer = removedog(user,customer.policyno,i)
                    sg.popup_timed('Your pet {} has been removed from your policy no.{}.'.format(i,customer.policyno))
                    return 'start',customer

#Claim pet screen for Customers (done)
def claim(user,customer):
    radio_choices = customer.dogs
    radio = [[sg.Radio(text, 1,key=text,font='Lucinda 12'),] for text in radio_choices]
    layoutclaim = [[sg.Text('We\'re sorry to have you file a claim\non your beloved pet.',key='condolence',size=(30,2),font='Lucinda 11')]] + radio +[[sg.Button('Submit Claim',key='submit',font='Lucinda 12')],
    [sg.Button('Back',key='back',font='Lucinda 12')]]
    window = sg.Window('File a Claim',layoutclaim)

    while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED:
            window.Close()
            quit()
        elif event == 'back':
            window.Close()
            return 'start',customer
        elif event == 'submit':
            window.Close
            for i in radio_choices:
                if values[i] == True:
                    window.Close()
                    customer = claimdog(user,customer.policyno,i)
                    sg.popup_timed('Our deepest condolences for your {}.'.format(i))
                    return 'start',customer

#Agent home screen (done)
def agent(user):
    agents=getagent(user)
    layoutagent = [[sg.Text(agents.fname,key='user',size=(20,1),font='Lucinda 20')],
    [sg.Text('Customer',key='user',size=(30,1),font='Lucinda 12')],
    [sg.Button('Quote',key='quote',font='Lucinda 12'),sg.Button('New Policy',key='new',font='Lucinda 12'),sg.Button('File a Claim',key='claim',font='Lucinda 12')],
    [sg.Text('Agent',key='user',size=(30,1),font='Lucinda 12')],
    [sg.Button('Income',key='income',font='Lucinda 12'),sg.Button('Policy Holders',key='policies',font='Lucinda 12')],
    [sg.Push(),sg.Button('Logout',key='logout',font='Lucinda 12'),sg.Button('Exit',font='Lucinda 12')]]
    window = sg.Window('{}'.format(user),layoutagent)

    while True:
        event,values = window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            window.Close()
            quit()
        else:
            window.Close()
            return event,agents

#Agent quote pet for customer (done)
def agentadd(user):
    layoutadd = [[sg.Text('Doggo Name',key='dname',size=(15,1),font='Lucinda 12'),sg.Input(key='userinput',font='Lucinda 12',size=(15,1))],
    [sg.Text('Doggo Breed',key='pass',size=(15,1),font='Lucinda 12'),sg.Combo(['Mixed Breed under 15 lbs.','Mixed Breed under 30 lbs.','Mixed Breed under 65 lbs.','Mixed Breed under 110 lbs.','Mixed Breed over 110 lbs.'],key='kind',font='Lucinda 12',size=(15,1))],
    [sg.Text('Doggo Age',key='age',size=(15,1),font='Lucinda 12'),sg.Input(key='ageinput',font='Lucinda 12',size=(15,1))],
    [sg.Text('',key='space',size=(30,2),font='Lucinda 11',visible=False)],
    [sg.Button('Quote me',key='quote',font='Lucinda 12'),sg.Button('Back',key='back',font='Lucinda 12'),sg.Button('Add your doggo',key='approved',font='Lucinda 12',visible=False)],
    [sg.Button('Exit',font='Lucinda 12')]]
    window = sg.Window('Add to your Pack',layoutadd)
    
    while True:
        event,values = window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            window.Close()
            quit()
        # -- -- Actual Functionality -- --
        elif event == 'quote':
            cost = guiinsurability(values['kind'],int(values['ageinput']))
            if cost == 0:
                window['space'].update('Your dog is inelligble for life insurance',visible=True)
            else:
                window['space'].update('Your Doggo is eligible for life insurance!\nA policy is available for ${:.2f} per year!'.format(cost),visible=True)
                window['approved'].update(visible=True)
        elif event == 'back':
            window.Close()
            return 'start'
        elif event == 'approved':
            agentsend(user,values['userinput'],values['kind'],values['ageinput'])

#Agent create policy for customer based on approved quote (done)
def agentsend(user,name,breed,age):
    layoutsignup = [[sg.Text('Agent Name',key='aname',size=(15,1),font='Lucinda 12'),sg.Text(user,key='agent',font='Lucinda 12',size=(15,1))],
    [sg.Text('First Name',size=(15,1),font='Lucinda 12'),sg.Input(key='fname',font='Lucinda 12',size=(15,1))],
    [sg.Text(key='fnameerr',size=(30,1),font='Lucinda 12',visible=False,justification='r',text_color='red')],
    [sg.Text('Last Name',size=(15,1),font='Lucinda 12'),sg.Input(key='lname',font='Lucinda 12',size=(15,1))],
    [sg.Text(key='lnameerr',size=(30,1),font='Lucinda 12',visible=False,justification='r',text_color='red')],
    [sg.Text('Address1',size=(15,1),font='Lucinda 12'),sg.Input(key='add1',font='Lucinda 12',size=(15,1))],
    [sg.Text(key='add1err',size=(30,1),font='Lucinda 12',visible=False,justification='r',text_color='red')],
    [sg.Text('Address2',size=(15,1),font='Lucinda 12'),sg.Input(key='add2',font='Lucinda 12',size=(15,1))],
    [sg.Text('Address3',size=(15,1),font='Lucinda 12'),sg.Input(key='add3',font='Lucinda 12',size=(15,1))],
    [sg.Text('City',size=(15,1),font='Lucinda 12'),sg.Input(key='city',font='Lucinda 12',size=(15,1))],
    [sg.Text(key='cityerr',size=(30,1),font='Lucinda 12',visible=False,justification='r',text_color='red')],
    [sg.Text('State',size=(15,1),font='Lucinda 12'),sg.Input(key='state',font='Lucinda 12',size=(15,1))],
    [sg.Text(key='stateerr',size=(30,1),font='Lucinda 12',visible=False,justification='r',text_color='red')],
    [sg.Text('Zip',size=(15,1),font='Lucinda 12'),sg.Input(key='zip',font='Lucinda 12',size=(15,1))],
    [sg.Text(key='ziperr',size=(30,1),font='Lucinda 12',visible=False,justification='r',text_color='red')],
    [sg.Button('Create Policy',key='create',font='Lucinda 12'),sg.Button('Main Menu',key='back',font='Lucinda 12')],
    [sg.Button('Exit',font='Lucinda 12')]]
    window = sg.Window('Create Policy for {}'.format(name),layoutsignup)
    
    while True:
        event,values = window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            window.Close()
            quit()
        elif event == 'back':
            window.Close()
            return 'start'
        elif event == 'create':
            window['fnameerr'].update(visible=False)
            window['lnameerr'].update(visible=False)
            window['add1err'].update(visible=False)
            window['cityerr'].update(visible=False)
            window['stateerr'].update(visible=False)
            window['ziperr'].update(visible=False)
            sent,fname,lname,add1,city,state,zipp = guiagentsignup(values['fname'],values['lname'],values['add1'],values['add2'],values['add3'],values['city'],values['state'],values['zip'],11,name,breed,age)
            if sent==True:
                sg.popup_timed("Thank you for trusting us with your pet's final cost.\nYour policy has been created and can be viewed by logging in.",auto_close_duration=5)
                window.Close()
                return 'login'
            else:
                if fname != values['fname']:
                    window['fnameerr'].update(fname)
                    window['fnameerr'].update(visible=True)
                if lname != values['lname']:
                    window['lnameerr'].update(lname)
                    window['lnameerr'].update(visible=True)
                if add1 != values['add1']:
                    window['add1err'].update(add1)
                    window['add1err'].update(visible=True)
                if city != values['city']:
                    window['cityerr'].update(city)
                    window['cityerr'].update(visible=True)
                if state != values['state']:
                    window['stateerr'].update(state)
                    window['stateerr'].update(visible=True)
                if zipp != values['zip']:
                    window['ziperr'].update(zipp)
                    window['ziperr'].update(visible=True)

#Agent create policy with no pets (done)            
def agentsignup(user):
    layoutsignup = [[sg.Text('Agent Name',key='aname',size=(15,1),font='Lucinda 12'),sg.Text(user,key='agent',font='Lucinda 12',size=(15,1))],
    [sg.Text('First Name',size=(15,1),font='Lucinda 12'),sg.Input(key='fname',font='Lucinda 12',size=(15,1))],
    [sg.Text(key='fnameerr',size=(30,1),font='Lucinda 12',visible=False,justification='r',text_color='red')],
    [sg.Text('Last Name',size=(15,1),font='Lucinda 12'),sg.Input(key='lname',font='Lucinda 12',size=(15,1))],
    [sg.Text(key='lnameerr',size=(30,1),font='Lucinda 12',visible=False,justification='r',text_color='red')],
    [sg.Text('Address1',size=(15,1),font='Lucinda 12'),sg.Input(key='add1',font='Lucinda 12',size=(15,1))],
    [sg.Text(key='add1err',size=(30,1),font='Lucinda 12',visible=False,justification='r',text_color='red')],
    [sg.Text('Address2',size=(15,1),font='Lucinda 12'),sg.Input(key='add2',font='Lucinda 12',size=(15,1))],
    [sg.Text('Address3',size=(15,1),font='Lucinda 12'),sg.Input(key='add3',font='Lucinda 12',size=(15,1))],
    [sg.Text('City',size=(15,1),font='Lucinda 12'),sg.Input(key='city',font='Lucinda 12',size=(15,1))],
    [sg.Text(key='cityerr',size=(30,1),font='Lucinda 12',visible=False,justification='r',text_color='red')],
    [sg.Text('State',size=(15,1),font='Lucinda 12'),sg.Input(key='state',font='Lucinda 12',size=(15,1))],
    [sg.Text(key='stateerr',size=(30,1),font='Lucinda 12',visible=False,justification='r',text_color='red')],
    [sg.Text('Zip',size=(15,1),font='Lucinda 12'),sg.Input(key='zip',font='Lucinda 12',size=(15,1))],
    [sg.Text(key='ziperr',size=(30,1),font='Lucinda 12',visible=False,justification='r',text_color='red')],
    [sg.Button('Create Policy',key='create',font='Lucinda 12'),sg.Button('Main Menu',key='back',font='Lucinda 12')],
    [sg.Button('Exit',font='Lucinda 12')]]
    window = sg.Window('Creat Policy',layoutsignup)

    while True:
        event,values = window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            window.Close()
            quit()
        elif event == 'back':
            window.Close()
            return 'start'
        elif event == 'create':
            window['fnameerr'].update(visible=False)
            window['lnameerr'].update(visible=False)
            window['add1err'].update(visible=False)
            window['cityerr'].update(visible=False)
            window['stateerr'].update(visible=False)
            window['ziperr'].update(visible=False)
            sent,fname,lname,add1,city,state,zipp = guiagentsignup(values['fname'],values['lname'],values['add1'],values['add2'],values['add3'],values['city'],values['state'],values['zip'],user)
            if sent==True:
                sg.popup_timed("Thank you for trusting us with your pet's final cost.\nYour policy has been created and can be viewed by logging in.",auto_close_duration=5)
                window.Close()
                return 'login'
            else:
                if fname != values['fname']:
                    window['fnameerr'].update(fname)
                    window['fnameerr'].update(visible=True)
                if lname != values['lname']:
                    window['lnameerr'].update(lname)
                    window['lnameerr'].update(visible=True)
                if add1 != values['add1']:
                    window['add1err'].update(add1)
                    window['add1err'].update(visible=True)
                if city != values['city']:
                    window['cityerr'].update(city)
                    window['cityerr'].update(visible=True)
                if state != values['state']:
                    window['stateerr'].update(state)
                    window['stateerr'].update(visible=True)
                if zipp != values['zip']:
                    window['ziperr'].update(zipp)
                    window['ziperr'].update(visible=True)

#Agent files claim on user (done)
def agentclaim(user):
   
    layoutagentclaim = [[sg.Text('Enter policy number',size=(15,1),font='Lucinda 12'),sg.Input(key ='policyno',size=(15,1),font='Lucinda 12')],
                        [sg.Button('Find policy',key='find',font='Lucinda 12')],
                        [sg.Text('',key='err',font='Lucinda 12',justification='r',text_color='red')],
                        [sg.Button('Back',key='back',font='Lucinda 12')]]
    window = sg.Window('File a Claim',layoutagentclaim)

    while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED:
            window.Close()
            quit()
        elif event == 'back':
            window.Close
            return 'start'
        elif event == 'find':
            dogs = polcheck(values['policyno'])
            if dogs != False:
                radio = [[sg.Radio(text, 1,font='Lucinda 12',key='that'),] for text in dogs]
                layoutclaim = [[sg.Text('Select the pet to file a claim on.',key='condolence',size=(30,2),font='Lucinda 11')]] + radio +[[sg.Button('Submit Claim',key='submit',font='Lucinda 12')],
                [sg.Button('Back',key='back',font='Lucinda 12')]]
                window2 = sg.Window('File a Claim',layoutclaim)
                window2.Close
                while True:
                    event2,values2 = window2.read()
                    if event2 == sg.WIN_CLOSED:
                        window.Close()
                        window2.Close()
                        quit()
                    elif event2 == 'back':
                        window.Close()
                        window2.Close()
                        return 'start'
                    elif event2 == 'submit':
                        claimdog('user1',values['policyno'],values2['that'])
                        sg.popup_timed('Claim has been filed for {}.'.format(values2['that']))
                        window.Close()
                        window2.Close()
                        return 'start'
            else:
                window['err'].update('Incorrect policy number.')

#Queries all policies associated with the agent (done)
def agentpolicies(user,agents):
    plist = policylist(agents.agentno)
    pollist = [[sg.Text(text,font='Lucinda 12',size=(30,1),justification='c'),] for text in plist]
    layoutagentpolicies = [[sg.Text('Policies associated with you.',font='Lucinda 12',size=(30,1),justification='c')]] + pollist + [[sg.Button('Back',key='back',font='Lucinda 12')]]
    window = sg.Window('Policies',layoutagentpolicies)

    while True:
        event,values = window.read()
        print('again')
        if event == sg.WIN_CLOSED:
            window.Close()
            quit()
        elif event == 'back':
            window.Close()
            return 'start'

#Queries policies and total compensation (done)
def agentincome(user,agents):
    premiums,policies = premiumtotal(agents.agentno)

    layoutagentincome = [[sg.Text('You are the acting agent over {} policies'.format(policies),font='Lucinda 12',size=(32,1))],
                        [sg.Text('Your commission is 3 percent \nfor a yearly total of ${:,.2f}.'.format(int(premiums)*.03),font='Lucinda 12',size=(32,2))],
                        [sg.Button('Back',key='back',font='Lucinda 12')]]
    window = sg.Window('Your cut',layoutagentincome)

    while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED:
            window.Close()
            quit()
        elif event == 'back':
            window.Close()
            return 'start'

#actuary home screen (done)
def actuary(user):
    actuaries = getactuary(user)
    income = getincome()
    layoutactuary = [[sg.Text('Welcome, {}'.format(actuaries.fname),key='user',size=(20,1),font='Lucinda 20')],
    [sg.Text('Yearly Revenue',key='user',size=(15,1),font='Lucinda 12'),sg.Text('${:,.2f}'.format(income),key='revenue',size=(15,1),font='Lucinda 12')],
    [sg.Text('Edit Values',key='user',size=(30,1),font='Lucinda 12')],
    [sg.Button('Age Pets',key='age',font='Lucinda 12')],
    # sg.Button('Payout Table',key='pays',font='Lucinda 12'),
    # [sg.Text('Visualize',key='user',size=(30,1),font='Lucinda 12')],
    # [sg.Button('Profit by Dog Size',key='sizeprofit',font='Lucinda 12')],
    [sg.Button('Logout',key='logout',font='Lucinda 12'),sg.Button('Exit',font='Lucinda 12')]]
    window = sg.Window('Confidential',layoutactuary)

    while True:
        event,values = window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            window.Close()
            quit()
        elif event == 'age':
            gboys = agepets()
            income = getincome()
            window['revenue'].update('${:,.2f}'.format(income))
            sg.popup('The dogs have been aged 1 year.\n{} good boys are waiting on rainbow road.'.format(gboys),font='Lucinda 12')
        else:
            window.Close()
            return event, actuaries

#Creates a graph to visualize cost of running company 
def actuaryvisual():
        # -- -- Lays out the Home window -- --
    # -- -- creates placeholder window to be removed after the launch of the next window

    layout = [[],
            [sg.Button('Back',key='back',font='Lucinda 12'),sg.Button('Exit',font='Lucinda 12')]]
    window = sg.Window('Visual',layout)

    # -- -- opens the window and reads output -- --
    while True:
        event,values = window.read()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            window.Close()
            quit()
        elif event == 'quote':
            window.Close()
            return 'quote'
        elif event == 'login':
            window.Close()
            return 'login'

#Program Navigation
navkey = 'start'
while True:
    match navkey:
        case 'start':
            navkey = startwindow()
        case 'quote':
            navkey,dog_name,dog_breed,dog_age = quote()
            if navkey == 'signup':
                navkey = signup(dog_name,dog_breed,dog_age)
        case 'login':
            navkey,user,access = login()

            if access == 'Customer':
                while True:
                    navkey,customer = customerscreen(user)
                    if navkey == 'logout':
                        navkey = 'login'
                        user=''
                        break
                    elif navkey == 'add':
                        navkey, customer = add(user,customer)
                    elif navkey == 'remove':
                        navkey, customer = remove(user,customer)
                    elif navkey == 'claim':
                        navkey,customer = claim(user,customer)
                    elif navkey == 'print':
                        policy(customer)

            elif access == 'Agent':
                while True:
                    navkey,agents = agent(user)
                    if navkey == 'logout':
                        user=''
                        navkey = 'login'
                        break
                    elif navkey == 'claim':
                        navkey = agentclaim(user)
                    elif navkey == 'new':
                        navkey = agentsignup(user)
                    elif navkey == 'quote':
                        navkey = agentadd(user)
                    elif navkey == 'income':
                        navkey = agentincome(user,agents)
                    elif navkey == 'policies':
                        navkey = agentpolicies(user,agents)                                            
            elif access == 'Actuary':
                while True:
                    navkey,actuaries = actuary(user)
                    if navkey == 'logout':
                        user=''
                        navkey = 'start'
                    elif navkey == 'sizeprofit':
                        navkey = actuaryvisual()
