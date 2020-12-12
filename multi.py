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

		# create the timestamp for the file name
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
			# Create a list, for sorting
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

# main menu and run program
Button(root, text="Audit Multi", command=generateMultiAudit).pack()

root.mainloop()
