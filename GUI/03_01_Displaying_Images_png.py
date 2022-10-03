from tkinter import *
root=Tk()
root.geometry("500x500")
photo=PhotoImage(file="03_01.png")
label=Label(image=photo)
label.pack()
root.mainloop()