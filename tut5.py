from tkinter import *
from PIL import Image, ImageTk

mahmudul_root = Tk()

mahmudul_root.geometry("755x544")
# photo = PhotoImage(file="1.png")

# For Jpg images

image = Image.open("photo.jpg")
photo = ImageTk.PhotoImage(image)


varun_label = Label(image=photo)
varun_label.pack()


mahmudul_root.mainloop()

