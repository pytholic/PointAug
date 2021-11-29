import tkinter as tk
from utils import *
import os
from tkinter import filedialog


TITLE_FONT = ('Ubuntu', 18, 'bold')
INPUT_FONT = ('Ubuntu', 12, 'bold')
INPUT_LABEL_FONT = ('Ubuntu', 12, 'bold')

### UTILITY FUNCTIONS ###

# Rotation augmentation function and buttons
def augment_rotate_angle(data, case='Y'):
	for obj in data:
		rotation_augmentation_angle(obj)


def augment_rotate_random(data, case='Y'):
	for obj in data:
		rotation_augmentation_random(obj)

def augment_jitter(data, sigma=0.01, clip=0.05):
	for obj in data:
		jitter_augmentation(obj)


# Storing and deleting file nams	
obj_files =[]

def add_mesh(frame):

	for widget in frame.winfo_children():
		if isinstance(widget, tk.Label):
			widget.destroy()
	
	filename = filedialog.askopenfilename(initialdir='', title='Select File',
		filetypes=(('object files', '*.obj'), ('all files', '*.*')))

	obj_files.append(filename)

def show_files(frame, _list):
	for obj in _list:
		label = tk.Label(frame, text=obj, bg='gray')
		label.pack()

def del_mesh(frame):
	for widget in frame.winfo_children():
		if isinstance(widget, tk.Label):
			widget.destroy()

	obj_files.clear()


### APP INTERFACE ###

class SampleApp(tk.Tk):

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)

		self.winfo_toplevel().title("Point Cloud Augmentation Tool") # To change title from 'tk'

		# the container is where we'll stack a bunch of frames
		# on top of each other, then the one we want visible
		# will be raised above the others
		container = tk.Frame(self)
		#container.title("Point Cloud Augmentation Tool")
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}
		self.frames["StartPage"] = StartPage(parent=container, controller=self)
		self.frames["PageAug"] = PageAug(parent=container, controller=self)
		self.frames["PageRotAug"] = PageRotAug(parent=container, controller=self)
		self.frames["PageRotInputs"] = PageRotInputs(parent=container, controller=self)

		self.frames["StartPage"].grid(row=0, column=0, sticky="nsew")
		self.frames["PageAug"].grid(row=0, column=0, sticky="nsew")
		self.frames["PageRotAug"].grid(row=0, column=0, sticky="nsew")
		self.frames["PageRotInputs"].grid(row=0, column=0, sticky="nsew")

		self.show_frame("StartPage")


	def show_frame(self, page_name):
		'''Show a frame for the given page name'''
		frame = self.frames[page_name]
		frame.tkraise()


# Starting Page

class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		self.canvas = tk.Canvas(self, height=700, width=700, bg='#263D42')
		self.canvas.pack(fill="both", expand=True)

		self.frame_start = tk.Frame(self, bg='white')
		self.frame_start.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

		
		label_start = tk.Label(self.frame_start, text="Open files for augmentation!", bg='#E5E4E2', font=TITLE_FONT, borderwidth=2)
		label_start.pack(side="top", fill="x", pady=10)

		# Open file button
		open_file = tk.Button(self.frame_start, text='Open File', padx=10, width = 15,
					pady=5, fg='white', bg='#263D42', bd=3, relief='raised',
					command=lambda: [add_mesh(self.frame_start), show_files(self.frame_start, obj_files)])
		
		open_file.pack(side=tk.BOTTOM)
		#open_file.place(x=100, y=530) # Can also use relx and rely
		#open_file.pack(side=tk.BOTTOM)


		# Delete file button
		delete_file = tk.Button(self.frame_start, text='Delete Files', padx=10, width = 15,
					pady=5, fg='white', bg='#263D42', bd=3, relief='raised',
					command=lambda: del_mesh(self.frame_start))
		
		delete_file.pack(side=tk.BOTTOM)
		#delete_file.place(x=205, y=530)


		# Augmentation button
		augment_button = tk.Button(self.frame_start, text='Augmentation', padx=10, width = 15,
						pady=5, fg='white', bg='#263D42', bd=3, relief='raised',
						command=lambda: controller.show_frame("PageAug"))
		
		augment_button.pack(side=tk.BOTTOM)



class PageAug(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		self.canvas = tk.Canvas(self, height=700, width=700, bg='#263D42')
		self.canvas.pack(fill="both", expand=True)

		self.frame_aug = tk.Frame(self, bg='white')
		self.frame_aug.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

		label_aug = tk.Label(self.frame_aug, text="Choose augmentation type", bg='#E5E4E2', font=TITLE_FONT, borderwidth=2)
		label_aug.pack(side="top", fill="x", pady=10)
	

		# Show Files
		show_files = tk.Button(self.frame_aug, text='Show Files', padx=10, width = 15,
					pady=5, fg='white', bg='#263D42', bd=3, relief='raised',
					command=lambda: controller.show_frame("StartPage"))
		
		#show_files.place(x=200, y=530)
		show_files.pack(side=tk.BOTTOM)

		# Rotation Augmentation
		rotation_augmentation = tk.Button(self.frame_aug, text='Rotation', padx=10, width = 15,
					pady=5, fg='white', bg='#263D42', bd=3, relief='raised',
					command=lambda: controller.show_frame("PageRotAug"))
		
		rotation_augmentation.place(x=20, y=70)
		#rotation_augmentation.pack(side=tk.LEFT)

		# Jitter Augmentation
		jitter_augmentation = tk.Button(self.frame_aug, text='Jitter', padx=10, width = 15,
						pady=5, fg='white', bg='#263D42', bd=3, relief='raised',
						command=lambda: augment_jitter(obj_files, sigma=0.01, clip=0.05))
		
		jitter_augmentation.place(x=160, y=70)
		#jitter_augmentation.pack(side=tk.LEFT)



# Rotation Augmentation Page

class PageRotAug(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		self.controller = controller

		self.canvas = tk.Canvas(self, height=700, width=700, bg='#263D42')
		self.canvas.pack(fill="both", expand=True)

		self.frame_rot = tk.Frame(self, bg='white')
		self.frame_rot.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

		label_aug = tk.Label(self.frame_rot, text="Choose augmentation type", bg='#E5E4E2', font=TITLE_FONT, borderwidth=2)
		label_aug.pack(side="top", fill="x", pady=10)

		
		# Show Files
		show_files = tk.Button(self.frame_rot, text='Show Files', padx=10, width = 15,
					pady=5, fg='white', bg='#263D42', bd=3, relief='raised',
					command=lambda: controller.show_frame("StartPage"))
		
		show_files.pack(side=tk.BOTTOM)
		#show_files.place(x=200, y=530)

		
		# Angle rotation Augmentation
		angle_rotation = tk.Button(self.frame_rot, text='Angle Rotation', padx=10, width = 15,
					pady=5, fg='white', bg='#263D42', bd=3, relief='raised',
					command= lambda: controller.show_frame("PageRotInputs"))
					#command=lambda: augment_rotate_angle(obj_files, 'Y'))
		
		angle_rotation.place(x=20, y=70)
		#angle_rotation.pack(side=tk.BOTTOM)

		# Random Rotation Augmentation
		random_rotation = tk.Button(self.frame_rot, text='Random Rotation', padx=10, width = 15,
						pady=5, fg='white', bg='#263D42', bd=3, relief='raised',
						command=lambda: augment_rotate_random(obj_files, 'Y'))
		
		random_rotation.place(x=160, y=70)
		#random_rotation.pack(side=tk.BOTTOM)


# User Inputs for Rotation Augmentation

class PageRotInputs(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		self.controller = controller

		self.canvas = tk.Canvas(self, height=700, width=700, bg='#263D42')
		self.canvas.pack(fill="both", expand=True)

		self.frame_rot_inputs = tk.Frame(self, bg='white')
		self.frame_rot_inputs.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

		label_aug = tk.Label(self.frame_rot_inputs, text="Input the dersired parameters", 
							bg='#E5E4E2', font=TITLE_FONT, borderwidth=2)
		label_aug.pack(side="top", fill="x", pady=10)

		
		### Taking desired input from user ###

		# Input for angle augmentation

		# Number of augmentations
		self.num_angle_aug = tk.IntVar()
		self.num_angle_aug.set(1)
		tk.Entry(self.frame_rot_inputs, textvariable=self.num_angle_aug, 
				bg='#E5E4E2', justify='center').place(x=270, y=70, width=100, height=25)

		label_num_angle = tk.Label(self.frame_rot_inputs, text="Number:", 
							font=INPUT_LABEL_FONT, bg='white', borderwidth=2)
		label_num_angle.place(x=160, y=72)

		# Input angle
		self.angle = tk.IntVar()
		self.angle.set(90)
		tk.Entry(self.frame_rot_inputs, textvariable=self.angle, 
				bg='#E5E4E2', justify='center').place(x=270, y=100, width=100, height=25)

		label_angle = tk.Label(self.frame_rot_inputs, text="Angle:", 
							font=INPUT_LABEL_FONT, bg='white', borderwidth=2)
		label_angle.place(x=170, y=102)


		# Show Files
		show_files = tk.Button(self.frame_rot_inputs, text='Show Files', padx=10, width = 15,
					pady=5, fg='white', bg='#263D42', bd=3, relief='raised',
					command=lambda: controller.show_frame("StartPage"))
		
		show_files.pack(side=tk.BOTTOM)

		# # Angle rotation Augmentation
		# angle_rotation = tk.Button(self.frame_rot, text='Angle Rotation', padx=10, 
		# 			pady=5, fg='white', bg='#263D42', bd=3, relief='raised',
		# 			command=lambda: augment_rotate_angle(obj_files, 'Y'))
		
		# angle_rotation.pack(side=tk.BOTTOM)

		# # Random Rotation Augmentation
		# random_rotation = tk.Button(self.frame_rot, text='Random Rotation', padx=10, 
		# 				pady=5, fg='white', bg='#263D42', bd=3, relief='raised',
		# 				command=lambda: augment_rotate_random(obj_files, 'Y'))
		
		# random_rotation.pack(side=tk.BOTTOM)



# Run

if __name__ == "__main__":
	app = SampleApp()
	app.mainloop()