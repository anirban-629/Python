from tkinter import *
root=Tk()
root.title="ANIRBAN"
root.geometry("500x300")

f1=Frame(root,bg="Yellow",borderwidth=7,pady=60,padx=30,relief=GROOVE)
f1.pack(side=LEFT,anchor="nw")
l1=Label(f1,text="ANIRBAN MISHRA")
l1.pack()

f2=Frame(root,bg="Blue",borderwidth=7,pady=30,padx=100)
f2.pack(side=LEFT)

l2=Label(text="ANUP MISHRA",bg="red")
l2.pack(side=LEFT,anchor='nw',padx=10)

root.mainloop()
