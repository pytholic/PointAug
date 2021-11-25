import tkinter as tk
from tkinter import filedialog, Text
from utils import *
import os

root = tk.Tk() # Kind of like a frame where we will attach all things
obj_files =[]

def add_mesh():

	for widget in frame.winfo_children():
		widget.destroy()

	filename = filedialog.askopenfilename(initialdir='', title='Select File',
		filetypes=(('object files', '*.obj'), ('all files', '*.*')))

	obj_files.append(filename)
	print(filename)
	for obj in obj_files:
		label = tk.Label(frame, text=obj, bg='gray')
		label.pack()


def augment():

	for obj in obj_files:
		mesh = load_mesh(obj)




# Preparing environment

canvas = tk.Canvas(root, height=700, width=700, bg='#263D42') # bg = background
canvas.pack() # Attach canvas to root

frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.065)

# Adding buttons

open_file = tk.Button(root, text='Open File', padx=10, pady=5, fg='white', bg='#263D42', command=add_mesh)
open_file.pack()

run_augmentation = tk.Button(root, text='Run Augmentation', padx=10, pady=5, fg='white', bg='#263D42')
run_augmentation.pack()

root.mainloop()

