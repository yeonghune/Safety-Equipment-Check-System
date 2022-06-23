from tkinter_and_openCV import VideoOpen
from tkinter import *

root =Tk()
root.title("YeongHun GUI")

label1 = Label(root, text="Hello")
label1.pack()

photo =PhotoImage(file="GUI_EXAMPLE\image.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text = "bye")

    global photo2
    photo2 = PhotoImage(file="GUI_EXAMPLE\image2.png")
    label2.config(image=photo2)


btn = Button(root, text="클릭", command=VideoOpen)
btn.pack()

root.mainloop()