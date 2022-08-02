'''
All code was assembled by myself, Samuel Sidzyik.
I pulled bits and pieces from various sources but this code is my own.

sources referenced
https://www.askpython.com/python/examples/find-all-methods-of-class#:~:text=Method%201%20%E2%80%93%20Using%20the%20dir%20%28%29%20function,it%20for%20MyClass.%20print%28dir%28MyClass%29%29%20Output%20%5B%27__class__%27%2C%20%27__delattr__%27%2C%20%27__dict__%27%2C
'''
from functionality import *

'''
CLI Program Navigation
'''
def comlinenav():
    monthy = 'May'
    yeary = '1999'
    print('\nWelcome to Sam\'s Pet Insurance!!')
    while True:
        match input('\nYou are in {} of {}\nWhere would you like to go?\n[1] Login\n[2] Purchase A Policy\n[3] Forgot Password\n[4] Quote\n[5] Time Travel\n[6] Goodbye\n'.format(monthy,yeary)):
            case '1':
                print('Login Prompt')
                user = login()
                access = 'table login column access'
                # method_list = [method for method in dir(Customer) if method.startswith('__') is False]
                # print(method_list)
            case '2':
                print('Buy Policy')
                signup(userlist)
            case '3':
                print('Forgot Password')
            case '4':
                quote = insurability()
                if quote > 10:
                    print('To insure you doggo the annual premium would be ${:,.2f}'.format(quote))
                else:
                    print('It isn\'t worth it for us to insure your doggo')
            case '5':
                print('Made it to the Time Machine')
                pass
            case '6':
                print('Thank you, Goodbye.')
                break
            case _:
                print('You did not enter a valid path')
                pass

# -- -- Runs CLI for project -- --
# comlinenav()

method_list = [method for method in dir(ttest) if method.startswith('__') is False]
print(method_list)