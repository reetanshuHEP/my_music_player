from tkinter import *

root = Tk()

# Load the image
try:
    play_icon = PhotoImage(file="play.png").subsample(2, 2)
    # Create a button with the image
    play_button = Button(root, image=play_icon)
    play_button.pack()
except:
    print("Failed to load the image file.")

root.mainloop()
