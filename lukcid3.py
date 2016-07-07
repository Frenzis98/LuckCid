import random
import string
import tkinter.messagebox
from tkinter import *


# Returns a combination of letter & digits
def gen():
    return random.choice(list('abcdef' + string.digits))


# prints the first digits until %, and starts printing random generation from the gen function and converts to upper case
# and then opens up a file and appends every click as a new line.
def printme():
    combo1 = '00000001008%s111%s1%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % (gen().upper(), gen().upper(), gen().upper(),
                                                                         gen().upper(), gen().upper(), gen().upper(),
                                                                         gen().upper(), gen().upper(), gen().upper(),
                                                                         gen().upper(), gen().upper(), gen().upper(),
                                                                         gen().upper(), gen().upper(), gen().upper(),
                                                                         gen().upper(), gen().upper())
    with open("cid_file1.txt", 'a') as outfile:
        outfile.write(combo1 + '\n')
    entryText.set(combo1)


def printme2():
    combo2 = '00000001008%s000%s1%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % (gen().upper(), gen().upper(), gen().upper(),
                                                                          gen().upper(), gen().upper(), gen().upper(),
                                                                          gen().upper(), gen().upper(), gen().upper(),
                                                                          gen().upper(), gen().upper(), gen().upper(),
                                                                          gen().upper(), gen().upper(), gen().upper(),
                                                                          gen().upper(), gen().upper())
    with open("cid_file2.txt", 'a') as outfile:
        outfile.write(combo2 + '\n')
    entryText2.set(combo2)
    # Main Window

window = Tk()
# Size of the window
window.geometry("500x300")
# Tittle
window.title("Lukcid v2")
# Disable resizing
window.resizable(width=FALSE, height=FALSE)
# *** Status Bar ***
status = Label(window, text="Twitter: 0Katz   Youtube: Simple Dev ", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM)
# Variable holding the image
photo = PhotoImage(file="pirate.png")
# Invoke the image and displays it on the main window
label = Label(window, image=photo)
label.pack()

# Prints an info warning before program loads and whishes you good luck :)
tkinter.messagebox.showinfo("Made by 0Katz", 'May the force be with you!')

# Entry Text
entryText = StringVar(window)
entryText2 = StringVar(window)

# Text Box Button which generates the console ids with 1's
textbox = Entry(window, textvariable=entryText).place(x=260, y=100, width=227)
botton = Button(window, text="Generate", command=printme).place(x=356, y=126)

# Text Box and Button which generates console ids with 0's
textbox2 = Entry(window, textvariable=entryText2).place(x=260, y=160, width=227)
botton = Button(window, text="Generate", command=printme2).place(x=356, y=186)

# Doesn't work yet, just there for an idea until
# We can figure a way to use .Net framework with python
tmApi = Radiobutton(window, text="TMAPI", value=1).place(x=17, y=140)
ccApi = Radiobutton(window, text="CCAPI", value=1).place(x=85, y=140)
apiButton = Button(window, text="Stablish Connection").place(x=26, y=180)
ipPs3 = Entry(window).place(x=20, y=100)
ipLabel = Label(window, text="IP ADDRESS").place(x=37, y=70)
genLabel = Label(window, text="CONSOLE ID").place(x=350, y=70)

window.mainloop()
