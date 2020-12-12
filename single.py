#import library
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os, datetime, shutil
from os import path
from datetime import datetime

# main menu title and size
root = Tk()
root.title("Document Manager")
root.geometry("400x200")

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

# main menu and run program
Button(root, text="Audit Single", command=generateSingleAudit).pack()

root.mainloop()
