import tkinter as tk
from tkinter import filedialog, Text
from utils import *
import os


# Reading file paths and storing them

obj_files =[]

def add_mesh():

	for widget in frame_main.winfo_children():
		if isinstance(widget, tk.Label):
			widget.destroy()
	
	filename = filedialog.askopenfilename(initialdir='', title='Select File',
		filetypes=(('object files', '*.obj'), ('all files', '*.*')))

	obj_files.append(filename)

	for obj in obj_files:
		label = tk.Label(frame_main, text=obj, bg='gray')
		label.pack()



# Preparing environment

root = tk.Tk() # Kind of like a frame where we will attach all things

canvas = tk.Canvas(root, height=700, width=700, bg='#263D42') # bg = background
canvas.pack() # Attach canvas to root

frame_main = tk.Frame(root, bg='white')
frame_main.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.065)


# Adding buttons and actions

# Open file button
open_file = tk.Button(root, text='Open File', padx=10, pady=5, fg='white', bg='#263D42', command=add_mesh)
open_file.pack()


# Rotation augmentation function and buttons
def augment_rotate_angle():
	for obj in obj_files:
		rotation_augmentation_angle(obj)


def augment_rotate_random():
	for obj in obj_files:
		rotation_augmentation_random(obj)


rotate_angle_button = tk.Button(root, text='Angle Rotation Augmentation', padx=10, pady=5, fg='white', bg='#263D42', command=augment_rotate_angle)
rotate_angle_button.pack()

rotate_random_button = tk.Button(root, text='Random Rotation Augmentation', padx=10, pady=5, fg='white', bg='#263D42', command=augment_rotate_random)
rotate_random_button.pack()

root.mainloop()