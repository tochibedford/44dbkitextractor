import os
import zipfile
import tqdm
import sys
from tkinter import *
import tkinter.font as tkFont
root = Tk(className="44DB Kit Extractor")

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class FFDB(object):
	def __init__(self, master, **kwargs):
		def acceptance(event):
			master.destroy();
		def declined(event):
			sys.exit();
		with open("word.txt") as li:
			l = li.read()
		master.focus_force()

		topFrame = Frame(master)
		topFrame.pack(side=TOP)

		fontStyle = tkFont.Font(family="Lucida Grande", size=17)
		fontStyleText = tkFont.Font(family="Lucida Grande", size=10)
		titleLabel = Label(topFrame, font=fontStyle, text="44DB LICENSE AGREEMENT")
		titleLabel.pack(side=TOP)

		bottomFrame = Frame(master)
		bottomFrame.pack(side=TOP)
		w = Frame(bottomFrame, width="20px")
		w.pack(side=LEFT)
		T = Text(bottomFrame, height=25, width=70, font=fontStyleText, wrap=WORD, bg="black", fg="white")
		T.pack(side=LEFT)
		T.insert(END, l)
		buttonFrame = Frame(bottomFrame)
		buttonFrame.pack(side=LEFT)

		acceptbutton = Button(buttonFrame, text="ACCEPT", fg="green", bg="black", width=20)
		acceptbutton.pack()

		declinebutton = Button(buttonFrame, text="DECLINE", fg="red", bg="black", width=20)
		declinebutton.pack()

		acceptbutton.bind("<Button-1>", acceptance)
		declinebutton.bind("<Button-1>", declined)

		scrollV = Scrollbar(bottomFrame, orient=VERTICAL)
		scrollV.config(command=T.yview)
		T.configure(yscrollcommand=scrollV.set)
		scrollV.pack(side=RIGHT, fill=Y)

def extract44():
	
	with zipfile.ZipFile("44DBpk.zip") as zf:
		for member in tqdm.tqdm(zf.infolist(), desc='Extracting'):
			try:
				zf.extract(member, pathExtract)
			except zipfile.error as e:
				pass

def clearScreen(): 
  
    # for windows 
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = os.system('clear') 


if __name__ == '__main__':
	if os.name == 'nt':
		usr = os.environ['USERPROFILE']
	else:
		usr = os.environ['HOME']
	pathExtract = usr + os.path.normpath("\\Documents\\44dbKits")
	if not os.path.isdir(pathExtract):
		os.mkdir(pathExtract)

	os.chdir(resource_path("."))
	app=FFDB(root)
	root.attributes('-alpha', 0.97)
	root.resizable(False, False)
	root.geometry("800x500")
	root.protocol("WM_DELETE_WINDOW", sys.exit)
	root.iconbitmap('iconWhite.ico')
	root.mainloop()
	clearScreen()

	sys.stdout.write("\x1b]2;44 Kit Extractor\x07")
	print("\n\n Extracting Your Kit")
	extract44();
	os.startfile(pathExtract);
