# import library
from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox
import os, datetime, shutil
from os import path
from datetime import datetime
import tkinter as tk

# main menu tile and size
root = tk.Tk()
root.title("Document Manager")
root.geometry("400x200")

def replaceText():
	# get old text and check if chosen
	oldText = simpledialog.askstring(title="Enter Old Text", prompt="Please type in old text")
	if (oldText is None):
		return

	# get new text and check if chosen
	newText = simpledialog.askstring(title="Enter New Text", prompt="Please type in new text")
	if (newText is None):
		return

	# select output directory and check if chosen
	dstDir = filedialog.askdirectory(initialdir="/", title="Select Directory")
	if (len(dstDir) == 0):
		return

	# iterate through directory files
	for root, dirs, files in os.walk(dstDir, topdown=True):
		for name in files:
			# replace old with new text
			newName = name.replace(oldText, newText)

			# join the old file with root
			oldFileName = os.path.join(root, name)

			# join the new file with root
			newFileName = os.path.join(root, newName)

			# to rename the file, FINAL
			os.rename(oldFileName, newFileName)

	# display finish message
	messagebox.showinfo("Document Manager", "Completed Renaming File(s)")

# main menu and run program
Button(root, text="Rename file", command=replaceText).pack()

root.mainloop()
