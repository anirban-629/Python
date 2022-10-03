from tkinter import *
root=Tk()
root.title("Anirban")

# Important Label Options
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"

# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

label=Label(text='''# Important Label Options
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"

# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE''',
            bg='pink',fg="blue",font="pristina 20 bold",padx=50,pady=50,borderwidth=10,relief=GROOVE)

# Important Pack options
# anchor = nw
# side = top, bottom, left, right
# fill
# padx
# pady
label.pack(side=BOTTOM,anchor="nw",fill=Y,padx=10,pady=20)
root.mainloop()







