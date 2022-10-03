from asyncio.windows_events import NULL
from pickle import TRUE
from sys import flags


# a=input('A: ') or NULL
# b=input('B: ') or NULL
# print(a,b)

def chooseDept():
    flag=True
    print('Departments (Codes)->\n(CSE|ECE|EE|CE|ME)')
    while(flag):
        dept=input('Enter Department-> ').lower()
        if(dept=='cse'):
            flag=False
            return 'cse'
        elif(dept=='ece'):
            flag=False
            return 'ece'
        elif(dept=='ee'):
            flag=False
            return 'ee'
        elif(dept=='ce'):
            flag=False
            return 'ce'
        elif(dept=='me'):
            flag=False
            return 'me'
        else:
            print('Invalid input Try again ..!')

print(chooseDept())