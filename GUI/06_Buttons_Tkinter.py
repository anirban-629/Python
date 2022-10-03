from tkinter import *
root=Tk()
root.geometry("400x300")

def b1_command():
    print("HELLO")
def b2_command():
    print("HI")

f1=Frame(root,bg='Yellow',borderwidth=5,relief=GROOVE)
f1.pack(side=LEFT,anchor='nw')
b1=Button(f1,text="ANIRBAN",bg='blue',command=b1_command)
b1.pack(side=LEFT,anchor='nw')

f2=Frame(root,bg='blue',borderwidth=5,relief=GROOVE)
f2.pack(side=LEFT,anchor='nw')
b2=Button(f2,text="SUCHO",bg='RED',command=b2_command)
b2.pack(side=LEFT,anchor='nw')

root.mainloop()