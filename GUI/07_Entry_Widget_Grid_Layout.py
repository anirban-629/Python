from tkinter import *
def printdetails():
    with open("07_Entry_Widget_Text.txt", 'a')as f:
        f.write(f"Email ID: {emailval.get()}\n")
        f.write(f"Password: {pasval.get()}\n")
root=Tk()
root.geometry("400x300")

email=Label(root,text="Email ID")
email.grid(row=0)

pas=Label(root,text="Password")
pas.grid(row=1)

# Variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar
emailval=StringVar()
pasval=StringVar()

emailentry=Entry(root,textvariable= emailval)
emailentry.grid(row=0,column=1)
pasentry=Entry(root,textvariable= pasval)
pasentry.grid(row=1,column=1)

Button(text="Submit",command=printdetails).grid()


root.mainloop()