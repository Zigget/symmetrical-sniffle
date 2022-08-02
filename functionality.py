'''
All code was assembled by myself, Samuel Sidzyik.
I pulled bits and pieces from various sources but this code is my own.

sources referenced
https://stackoverflow.com/questions/8370943/how-to-print-name-of-class-in-python
'''
from connected import *
import datetime
import hashlib as hash
import os

#Initialize Database fn names are self explanitory

# clearall() #Erases and recreates database
# sequencecreate() #Creates a sequence for policy numbers
# tablescreate() #Creates all the tables in the database
# dataset() #Fills database with necess
# population() #Auto fills database with customers
'''
Objects
'''
class Customer():
    def __init__(self,fname,lname,dogs,premium,policyno):
        self.fname = fname
        self.lname = lname
        self.dogs = dogs
        self.premium = premium
        self.policyno = policyno

class Agent():
    def __init__(self,fname,agentno):
        self.fname = fname
        self.agentno = agentno

class Actuary():
    def __init__(self,fname):
        self.fname = fname



'''
Functions
'''
#Creates customer object (done)
def getcustomer(username):
    fname,lname,dogs,premium,policy = customerdata(username)

    this1 = Customer(fname,lname,dogs,premium,policy)
    return this1

#Creates Agent object
def getagent(username):
    fname,agentno = agentdata(username)

    this1 = Agent(fname,agentno)
    return this1

#Creates Actuary object
def getactuary(username):
    fname = actuarydata(username)

    this1 = Actuary(fname)
    return this1

#Quotes if a policy would be issued (done)
def guiinsurability(dog,age):
    lifespan = breedsdict[dog]['lifespan']
    lifeleft = lifespan - age
    if lifeleft < 1:
        return 0
    else:
        quote = claimdict[breedsdict[dog]['size']]/lifeleft
        return round(quote,2)

#Adds dog to customer object and queries addition to table (done)
def adddog(username,policyno,dog_name,dog_breed,dog_age):
    adddoggo(policyno,dog_name,dog_breed,dog_age)
    fname,lname,dogs,premium,policy = customerdata(username)

    this1 = Customer(fname,lname,dogs,premium,policy)
    return this1

#Removes dog from customer object and queries deletion to table (done)
def removedog(username,policyno,dog_name):
    removedoggo(policyno,dog_name)
    fname,lname,dogs,premium,policy = customerdata(username)

    this1 = Customer(fname,lname,dogs,premium,policy)
    return this1

#Removes dog from customer object and queries deletion to table (done)
def claimdog(username,policyno,dog_name):
    claimdoggo(policyno,dog_name)
    fname,lname,dogs,premium,policy = customerdata(username)

    this1 = Customer(fname,lname,dogs,premium,policy)
    return this1

#Creates a hashed and salted password (done)
def passsecure(password):
    salt = os.urandom(64)
    securepass = b''
    securepass = hash.pbkdf2_hmac('sha256',password.encode('utf-8'),salt,20000)
    return securepass,salt

#Checks to make sure that the policy exists
def polcheck(pol):
    if polquery(pol) == True:
        return doglist(pol)
    else:
        return False

#Prints policy (done for now...)
def policy(customer):
        policyno = customer.policyno
        premium = customer.premium
        doggos = customer.dogs
        file_name = 'Policy_{}.docx'.format(policyno)
        file_data = "\t\t\t\t\t{}\n\n\t\tSAM's Dogg Life Insurance\n\n\t\tMy Policy {}\n\n\n\tOwner: \t{} {}\n\n\tYearly Premium: ${:,.2f}\n\n\tCovered Pets\t{}".format(datetime.datetime.now(),policyno,customer.fname,customer.lname,premium,'\n\t\t\t\t'.join(doggos))
        os.path.join(os.path.dirname(__file__),file_name)
        with open(file_name,'w') as write_file:
            write_file.write(file_data)

#Trys loging in (done)
def guilogin(username,password):
    return checkpass(username,password)

#Tests signup values and requests query to insert values to tables(done)
def guisignup(name,breed,age,fname,lname,add1,add2,add3,city,state,zip,user='pass',pass1='pass',pass2='pass'):
    sent = True
    userlist = users()
    if pass1 != pass2:
        pass2 = 'Passwords didn\'t match.'
        sent = False
    if str(fname).strip() == '':
        fname = 'Name cannot be blank'
        sent = False
    elif str(fname).isnumeric() == True:
        fname = 'Name cannot be a number'
        sent = False
    if str(lname).strip() == '':
        lname = 'Name cannot be blank'
        sent = False
    elif str(lname).isnumeric() == True:
        lname = 'Name cannot be a number'
        sent = False
    if str(add1).strip() == '':
        add1 = 'Address cannot be blank'
        sent = False
    elif str(add1).isnumeric() == True:
        add1 = 'Address cannot only be a number'
        sent = False
    if str(city).strip() == '':
        city = 'City cannot be blank'
        sent = False
    elif str(city).isnumeric() == True:
        city = 'City cannot be a number'
        sent = False
    if str(state).strip() == '':
        state = 'State cannot be blank'
        sent = False
    elif str(state).isnumeric() == True:
        state = 'State cannot be a number'
        sent = False
    if str(zip).strip() == '':
        zip = 'Zip cannot be blank'
        sent = False
    elif str(zip).isnumeric() != True:
        zip = 'Zip must be a number'
        sent = False
    elif len(str(zip)) != 5:
        zip = 'Zip must be 5 digits'
        sent = False
    if user == 'pass':
        pass
    elif str(user).strip() == '':
        user = 'Username cannot be blank'
        sent = False
    elif str(user).isnumeric() == True:
        user = 'Username cannot be a number'
        sent = False
    elif str(user) in str(userlist):
        user = '!Username has already been taken'
        sent = False
    special = '[]!@?#$%-&*=_'
    check1 = False
    check2 = False
    for i in pass1:
        if i in special:
            check1 = True
        if i.isdigit():
            check2 = True
    if len(pass1) > 16 or len(pass1) < 8 or str(pass1).lower() == pass1 or str(pass1).upper() == pass1 or check1 != True or check2 != True:
        pass1 = 'Password did not meet requirements'
        sent = False
    if sent==True:
        hashpass,salt = passsecure(pass1)
        agent = 0
        createpol(fname,lname,add1,add2,add3,city,state,zip,name,breed,age,agent,user,hashpass,salt)
        return sent,fname,lname,add1,city,state,zip,user,pass1,pass2
    else:
        return sent,fname,lname,add1,city,state,zip,user,pass1,pass2

#Tests signup values from agent and requests query to insert values to tables(done albeit redundant)
def guiagentsignup(fname,lname,add1,add2,add3,city,state,zip,agent,name = 'pass',breed = '',age = ''):
    sent = True
    if str(fname).strip() == '':
        fname = 'Name cannot be blank'
        sent = False
    elif str(fname).isnumeric() == True:
        fname = 'Name cannot be a number'
        sent = False
    if str(lname).strip() == '':
        lname = 'Name cannot be blank'
        sent = False
    elif str(lname).isnumeric() == True:
        lname = 'Name cannot be a number'
        sent = False
    if str(add1).strip() == '':
        add1 = 'Address cannot be blank'
        sent = False
    elif str(add1).isnumeric() == True:
        add1 = 'Address cannot only be a number'
        sent = False
    if str(city).strip() == '':
        city = 'City cannot be blank'
        sent = False
    elif str(city).isnumeric() == True:
        city = 'City cannot be a number'
        sent = False
    if str(state).strip() == '':
        state = 'State cannot be blank'
        sent = False
    elif str(state).isnumeric() == True:
        state = 'State cannot be a number'
        sent = False
    if str(zip).strip() == '':
        zip = 'Zip cannot be blank'
        sent = False
    elif str(zip).isnumeric() != True:
        zip = 'Zip must be a number'
        sent = False
    elif len(str(zip)) != 5:
        zip = 'Zip must be 5 digits'
        sent = False
    if sent == True:
        createpol(fname,lname,add1,add2,add3,city,state,zip,name,breed,age,agent)
        return sent,fname,lname,add1,city,state,zip
    else:
        return sent,fname,lname,add1,city,state,zip

#Lists policies associated with the agent (done)
def policylist(agentnum):
    list = querypollist(agentnum)
    return list

#total number of policies and premium cost for all policies with this agent (done)
def premiumtotal(agentnum):
    plist = querypollist(agentnum)
    policies = len(plist)
    premium = getpremsquery(plist)

    return premium,policies

#Get total premium brought in per year (done)
def getincome():
    income = queryincome()
    return income

def agepets():
    bois = agedogs(1)
    return bois
#CLI (obsolete)
'''
# def insurability():
#     dog = input('What is the breed of your pal?\nIf mixed or unkown type 0: ')
#     if dog in breedsdict:
#         #elif breed in Dog API weight
#         size = breedsdict[dog]['size'] #or API weight
#         lifespan = breedsdict[dog]['lifespan']
#     else:
#         weight = int(input('\nEnter your doggo\'s weight or guesstimate adult weight if a puppy: '))
#         if weight < 15:
#             size = 'XS'
#             lifespan = 18
#         elif weight < 30:
#             size = 'S'
#             lifespan = 15
#         elif weight < 65:
#             size = 'M'
#             lifespan = 12
#         elif weight < 110:
#             size = 'L'
#             lifespan = 9
#         else:
#             size = 'XL'
#             lifespan = 7
#     age = int(input('\nHow many years young is your doggo?: '))
#     lifeleft = lifespan - age
#     quote = claimdict[size]/lifeleft
#     return quote
# def login():
#     while True:
#         usr = input('Enter your username: ')
#         if usr == '1':
#             return ''
#         pwd = getpass.getpass('Enter your password: ')
#         if usr in userlist:
#             for i,k in customers.items():
#                 if pwd == i.password and k['Tries'] > 0:
#                     return i
#                 elif k['Tries'] == 0:
#                     print('You have reached max tries and this account is locked.')
#                 else:
#                     k['Tries'] -=1
#         print('\nUsername password combination incorrect.\n[1] Back')
# def signup(userlist):
#     while True:
#         #Names
#         try:
#             newfname = input('Enter your first name:').strip()
#             newlname = input('Enter your last name: ').strip()
#             if len(newfname) < 3 or len(newlname) < 3:
#                 print('Your first and last name must each be at least 3 letters.',end=' ')
#                 raise ValueError()
#             elif newfname.isnumeric() or newlname.isnumeric():
#                 print('Your name cannot be a number.',end=' ')
#                 raise ValueError()
#         except ValueError:
#             print('Invalid Entry.')
#         else:
#             while True:
#                 try:
#                     #Username
#                     newusername = input('Enter your username: ').strip()
#                     if newusername in userlist:
#                         print('This username has already been taken.',end=' ')
#                         raise ValueError()
#                     elif len(newusername) < 3:
#                         print('Your username must be at least 3 characters.',end=' ')
#                         raise ValueError()
#                     elif newusername.isnumeric():
#                         print('You username cannot be a number.',end=' ')
#                         raise ValueError()
#                 except ValueError:
#                     print('Invalid Entry.')
#                 else:
#                     while True:
#                         try:
#                             #Password
#                             pass1 = getpass.getpass('A password must be between 6 and 12 characters and contai a minimum of 1 lowercase 1 uppercase and 1 special character.\nEnter your password: ')
#                             if len(pass1) < 6 or len(pass1) > 12:
#                                 print('Your password must be between 6 and 12 characters.',end=' ')
#                                 raise ValueError()
#                             elif pass1.upper() == pass1:
#                                 print('Your password must contain a lowercase letter.',end=' ')
#                                 raise ValueError()
#                             elif pass1.lower() == pass1:
#                                 print('Your password must contain a uppercase letter.',end=' ')
#                                 raise ValueError()
#                             else:
#                                 special = '[]!@?#$%-&*=_'
#                                 check1 = False
#                                 check2 = False
#                                 for i in pass1:
#                                     if i in special:
#                                         check1 = True
#                                     if i.isdigit():
#                                         check2 = True
#                                 if check1 != True or check2 != True:
#                                     print('Your password must contain a special character.',end=' ')
#                                     raise ValueError()
#                         except ValueError:
#                             print('Invalid Entry.')
#                         else:
#                             try:
#                                 pass2 = getpass.getpass('ReEnter your password: ')
#                                 if pass1 != pass2:
#                                     print('Your password must match.',end=' ')
#                                     raise ValueError()
#                             except ValueError:
#                                 print('Invalid Entry.')
                            # else:
                            #     #Saves user
                            #     username = Customer(newfname,newusername,pass1)
                            #     customers[username] = newacc
                            #     userlist.append(username.username)
                            #     return
'''
