import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("System Controls")
root.geometry("550x680")
img = Image.open("bg.png")
bg_img = ImageTk.PhotoImage(img)
bg_label = tk.Label(root, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


root.mainloop()
