from tkinter import *
from PIL import Image, ImageTk
root=Tk()
root.geometry("500x500")

'''
photo=PhotoImage(file="03_01.jpg")
label=Label(image=photo)

it'll not work as jpg is not supported by tkinter only png
install  module
'''

image=Image.open("03_02.jpg")
photo=ImageTk.PhotoImage(image)

label=Label(image=photo)
label.pack()

root.mainloop()