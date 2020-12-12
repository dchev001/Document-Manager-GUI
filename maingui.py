# import library
from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox
import os, datetime, shutil
from os import path
from datetime import datetime
import tkinter.font as font

# main menu configuration
root = Tk()
root.title("Document Manager")
root.geometry("300x200")
root.resizable(width=0, height=0)

# to generate single audit report
def generateSingleAudit():
	# select input directory and check if chosen
	srcDir = filedialog.askdirectory(initialdir="/", title="Select Directory")
	if (len(srcDir) == 0):
		return

	# select output directory and check if chosen
	dstDir = filedialog.askdirectory(initialdir="/", title="Save File To")
	if (len(dstDir) == 0):
		return

	# initialize date, create timestamp for file
	currTime = datetime.now()
	shortDate = currTime.strftime("%Y%m%d")
	longDate = currTime.strftime("%b %m %Y %I:%M:%S%p")

	# change directory to selected one
	os.chdir(srcDir)

	# to name the directory file
	dirname = os.path.basename(srcDir)

	# create file
	fileName = shortDate+"_"+dirname+"_Audit Report (gen. "+longDate+").xlsx"
	f = open(fileName, "w+")

	# move file to destination
	shutil.move(fileName, dstDir)

	# iterate through current directory
	for root, dirs, files in os.walk(srcDir, topdown=True):
		# create list for sorting
		tempList = []

		for name in files:
			# join file name to root
			filePath = os.path.join(root, name)
			fpath = filePath[len(srcDir):]

			# append file name to list
			tempList.append(fpath)

		# sort the list
		tempList.sort()

		# write the list to file
		for b in tempList:
			f.write("\"" + b + '\"\n')

	# close file
	f.close()

	# display finish message
	messagebox.showinfo("Document Manager", "Completed Audit Report.")

# to generate multiple audit report
def generateMultiAudit():
	# select input directory and check if chosen
	srcDir = filedialog.askdirectory(initialdir="/", title="Select Directory")
	if (len(srcDir) == 0):
		return

	# select output directory and check if chosen
	dstDir = filedialog.askdirectory(initialdir="/", title="Save File(s) To")
	if (len(dstDir) == 0):
		return

	# change directory to selected one
	os.chdir(srcDir)

	# list the input folders directory
	lst = os.listdir(os.getcwd())

	# iterate through the input folders directory
	for x in lst:
		# join the input folder to the path
		currDir = os.path.join(os.getcwd(), x)

		# initialize date, create timestamp for file
		currTime = datetime.now()
		shortDate = currTime.strftime("%Y%m%d")
		longDate = currTime.strftime("%b %d %Y %I:%M:%S%p")

		# create the file name for the current folder
		fileName = shortDate+"_"+x+"_Audit Report (gen. "+longDate+").xlsx"
		f = open(fileName, "w+")

		# move file to destination
		shutil.move(fileName, dstDir)

		# iterate the current directory of the input folder
		for root, dirs, files in os.walk(currDir, topdown=True):
			# create list for sorting
			tempList = []

			# iterate through the files
			for name in files:
				# join file name to root
				filePath = os.path.join(root, name)
				fpath = filePath[len(currDir):]

				# append file name to list
				tempList.append(fpath)

			# sort the list
			tempList.sort()

			# write the list to file
			for b in tempList:
				f.write("\"" + b + "\"\n")

		# close file
		f.close()

	# display finish message
	messagebox.showinfo("Document Manager", "Completed Audit Report(s).")

# to replace the text in a directory
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
	messagebox.showinfo("Document Manager", "Completed Renaming File(s).")

# main menu and run program
Button(root, text="Audit Single", width=300, padx=40, pady=20, font="Arial", command=generateSingleAudit).pack()
Button(root, text="Audit Multiple", width=300, padx=40, pady=20, font="Arial", command=generateMultiAudit).pack()
Button(root, text="Rename File(s)", width=300, padx=40, pady=20, font="Arial", command=replaceText).pack()

root.mainloop()
