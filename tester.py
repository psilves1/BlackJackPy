from tkinter import *
from PIL import ImageTk, Image

master = Tk()


print("Ran")

canvas = Canvas(master, width=300, height=300)
canvas.pack()

img = ImageTk.PhotoImage(Image.open("C:\\Users\\psilv\\PycharmProjects\\BlackJackPy\\JPEG\\" + "12S" + ".jpg").resize((250, 250)))  # The resize method takes width and height in pixels
canvas.create_image(2, 2, anchor=NW, image=img)

#getImage(10, 10, "12S")

master.mainloop()

