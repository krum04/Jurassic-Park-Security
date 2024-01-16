import os
from time import sleep
from PIL import Image, ImageTk
import tkinter as tk
import pygame

# Initialize pygame mixer for audio
pygame.mixer.init()

# Load your MP3 file
pygame.mixer.music.load('magicword.mp3')

# Path to GIF file
gif_path = 'nedry.gif'

# Update the image for each frame of GIF
def update_gif(ind):
    if gif_displayed:
        try:
            gif.seek(ind)
            tk_gif.paste(gif)
            root.after(100, update_gif, ind+1)
        except EOFError:
            root.after(100, update_gif, 0)

# Clear the terminal
os.system("clear")

# Print the opening text
print("Jurassic Park, System Security Interface")
print("Version 4.0.5, Alpha E")
print("Ready", end="", flush=True)
sleep(1)
for i in range(3):
    print(".", end="", flush=True)
    sleep(1)
input("\n>")
print("access: PERMISSION DENIED.")
input(">")
print("access: PERMISSION DENIED.")
input(">")
print("access: PERMISSION DENIED...and...")

# Create a tkinter window without borders or title bar
root = tk.Tk()
root.overrideredirect(1)

# Set the initial position of the window (200 pixels from the left and top)
root.geometry('+200+200')

# Function to get the current mouse position on ButtonPress
def on_press(event):
    root.x = event.x
    root.y = event.y

# Function to move the window on ButtonMotion
def on_drag(event):
    x = root.winfo_pointerx() - root.x
    y = root.winfo_pointery() - root.y
    root.geometry(f'+{x}+{y}')

# Binding the mouse events to the root window
root.bind('<ButtonPress-1>', on_press)
root.bind('<B1-Motion>', on_drag)

# Load the GIF
gif = Image.open(gif_path)

# Convert the GIF to a format tkinter can use
tk_gif = ImageTk.PhotoImage(gif)

# Create a label for the image (but don't pack it yet)
label = tk.Label(root, image=tk_gif, borderwidth=0)

# Flag to control when the GIF is displayed
gif_displayed = False

# Now display the GIF
gif_displayed = True
label.pack()
update_gif(0)

# Function to print the magic word message
def print_magic_word():
    print("YOU DIDN'T SAY THE MAGIC WORD!")
    root.after(2250, print_magic_word)

# Start printing the magic word message
root.after(2250, print_magic_word)

# Start playing the MP3 file in a loop indefinitely
pygame.mixer.music.play(-1)  

# Start the tkinter main loop
root.mainloop()

# Stop the music when the window is closed
pygame.mixer.music.stop()