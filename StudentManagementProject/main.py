from asyncio.windows_events import NULL
from pickle import FALSE
from turtle import goto
import SystemInitialize as si
import docs

class model:
    def dataModel(self):
        self.fName=input('First Name -> ') or NULL
        self.lName=input('Last Name -> ') or NULL
        self.dob=input('Date of Birth -> ') or NULL
        self.mob=input('Student Mobile -> ') or NULL
        self.email=input('Email id -> ') or NULL
        self.address=input('Address for Correspondence -> ') or NULL
        self.city=input('City/Town -> ') or NULL
        self.district=input('District -> ') or NULL
        self.state=input('State -> ') or NULL
        self.pin=input('Pin Code -> ') or NULL
        self.fatherName=input('Father Name -> ') or NULL
        self.fatherNo=input('Mobile No. -> ') or NULL
        self.motherName=input('Mother Name -> ') or NULL
        self.motherNo=input('Mobile No. -> ') or NULL
        self.gender=input('Gender -> ') or NULL
        self.bloodgroup=input('Blood Group -> ') or NULL
        self.LandlineNo=input('Landline No. -> ') or NULL
        data={
            'First Name':self.fName,
            'Last Name':self.lName,
            'DOB':self.dob,
            'Mobile No.':self.mob,
            'Email':self.email,
            'Address':self.address,
            'City':self.city,
            'District':self.district,
            'State':self.state,
            'Pin':self.pin,
            'Father Name':self.fatherName,
            'Mobile No.':self.fatherNo,
            'Mother Name':self.motherName,
            'Mother No.':self.motherNo,
            'Gender':self.gender,
            'Blood Group':self.bloodgroup,
            'Line Line No.':self.LandlineNo
        }

class depts:
    pass

def initDB():
    si.main()
    print('DATABASE CREATED SUCCESFULLY')

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

def main():
    try:
        initDB()
    except:
        print('\n\nDatabase is already there...!\n')

    # dept=chooseDept()

    

main()
