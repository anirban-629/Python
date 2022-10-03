# 1
# from tkinter import *
# from PIL import Image,ImageTk
# root=Tk()
# root.geometry("500x500")
# root.minsize(300,300)
# root.maxsize(1000,1000)
# label=Label(text="Anirban")
# label.pack()
#
# photo1=PhotoImage(file="03_01.png")
# label2=Label(image=photo1)
# label2.pack()
#
# image=Image.open("03_02.jpg")
# photo2=ImageTk.PhotoImage(image)
# label3=Label(image=photo2)
# label3.pack()
#
# root.mainloop()

# 2
# from tkinter import *
# from PIL import Image,ImageTk
# root=Tk()
# root.geometry("500x500")
# # image=Image.open("03_02.jpg")
# # photo1=ImageTk.PhotoImage(image)
# # label1=Label(image=photo1)
# # label1.pack()
# label3=Label(text="HI THIS IS ANIRBAN")
# label3.pack()
#
# photo2=PhotoImage(file="03_01.png")
# label2=Label(image=photo2)
# label2.pack()
#
# root.mainloop()

# 3
# from tkinter import *
# root=Tk()
# root.title("ANIRBAN")
# root.geometry("500x500")
# label=Label(text="ANIRBAN IS A GOOD BOY"
#                  "HE STUDIES B.TECH CSE"
#                  "IN GMIT BARUIPUR KOLKATA",
#             bg="Black",fg="white",padx=30,pady=30)
# label.pack(side=BOTTOM,anchor="nw",fill=X)
# root.mainloop()

# 4
# from tkinter import *
# root=Tk()
# root.title="ANIRBAN"
# root.geometry("500x300")
# l2=Label(text="ANUP MISHRA",bg="red")
# l2.pack(side=LEFT,anchor='nw',padx=10)
#
# l3=Label(text="ANIRBAN MISHRA",bg="blue")
# l3.pack(side=TOP,anchor="w",padx=10)
# root.mainloop()

#
# 5
# from tkinter import *
# def c():
#     print("HELLO THIS IS PRACTICE FILE")
# root=Tk()
# root.geometry("400x300")
# f1=Frame(root,bg="yellow",borderwidth=6,relief=GROOVE)
# f1.pack(side=LEFT,anchor="nw")
# b1=Button(f1,text="A",bg="red",command=c)
# b1.pack()
# root.mainloop()

# from tkinter import *
# def g1():
#     print("Hello This is Button one")
# def g2():
#     print("Hello This is Button two")
# def g3():
#     print("Hello This is Button three")
# def g4():
#     print("Hello This is Button four")
# root=Tk()
# root.geometry("400x300")
# f1=Frame(root,bg="yellow")
# f1.pack(side=LEFT,anchor='nw',padx=5)
# b1=Button(f1,text="BUTTON-1",bg="Red",command=g1)
# b1.pack()
# f2=Frame(root,bg="green")
# f2.pack(side=LEFT,anchor='nw',padx=5)
# b2=Button(f2,text="BUTTON-2",bg="pink",command=g2)
# b2.pack()
# b3=Button(f1,text="BUTTON-3",bg="lightGreen",command=g3)
# b3.pack(side=TOP)
# b4=Button(f2,text="BUTTON-3",bg="lightblue",command=g4)
# b4.pack(side=TOP)
#
# root.mainloop()

# from tkinter import *
#
# root=Tk()
# root.geometry("400x300")
#
# name=Label(root,text="NAME:- ")
# name.grid(row=0)
#
# email=Label(root,text="Emial Id:- ")
# email.grid(row=1)
#
# # ph_no=Label(root,text="Phone Number:- ")
# # ph_no.grid(row=2)
#
# nameval=StringVar()
# emailval=StringVar()
# # phval=IntVar()
#
# name_entry=Entry(root,textvariable=nameval)
# name_entry.grid(row=0,column=1)
# email_entry=Entry(root,textvariable=emailval)
# email_entry.grid(row=1,column=1)
# # ph_entry=Entry(root,textvariable=phval)
# # ph_entry.grid(row=2,column=1)
#
# Button(text="Submit").grid()
# def printdetail():
#     with open("prctc.txt","a")as f:
#         f.write(nameval.get())
#         f.write(emailval.get())
#         # f.write(phval.get())
# root.mainloop()














