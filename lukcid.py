import random
import string
import tkinter.messagebox
from tkinter import *

# Returns a combination of letter & digits
def gen():
    return random.choice(string.ascii_letters + string.digits)

    #prints the first digits until %, and starts printing random generation from the gen function and converts to upper case
def printme():
        entryText.set('00000001008%s111%s1%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % (gen().upper(), gen().upper(), gen().upper(),
	                                                                         gen().upper(), gen().upper(), gen().upper(),
					                                    gen().upper(), gen().upper(), gen().upper(),
				                                            gen().upper(), gen().upper(), gen().upper(),
                                                                            gen().upper(), gen().upper(), gen().upper(),
									    gen().upper(), gen().upper()))


def printme2():
        entryText2.set('00000001008%s000%s1%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % (gen().upper(), gen().upper(), gen().upper(),
	                                                                         gen().upper(), gen().upper(), gen().upper(),
					                                    gen().upper(), gen().upper(), gen().upper(),
				                                            gen().upper(), gen().upper(), gen().upper(),
                                                                            gen().upper(), gen().upper(), gen().upper(),
									    gen().upper(), gen().upper()))
																																														     #Main Window
window = Tk()
#Size of the window
window.geometry("500x300")
#Tittle
window.title("Lukcid v1")
#Disable resizing
window.resizable(width=FALSE, height=FALSE)

# Entry Text
entryText = StringVar(window)
entryText2 = StringVar(window)

#Variable holding the image
photo = PhotoImage(file="pirate.png")
#Invoke the image and displays it on the main window
label= Label(window, image=photo)
label.pack()

#Prints an info warning before program loads and whishes you good luck :)
tkinter.messagebox.showinfo("Made by 0Katz", 'May the force be with you!')

#The Reason why I have 2 buttons is because I've seen valid console id's
#with three 1's  or three zero's at the 13's character up to the 15th character.
#So I made to buttons to enforce the Luck! Maybe the 1's and 0's is based on regions.

#Text Box Button which generates the console ids with 1's 
textbox = Entry(window, textvariable=entryText).place(x=260, y=100)
botton = Button(window, text="Generate", command=printme).place(x=290, y=126)

#Text Box and Button which generates console ids with 0's 
textbox2 = Entry(window, textvariable=entryText2).place(x=260, y=160)
botton = Button(window, text="Generate", command=printme2).place(x=290, y=186)

#Doesn't work yet, just there for an idea until
#We can figure a way to use .Net framework with python
tmApi = Radiobutton(window, text="TMAPI", value=1).place(x=17, y=140)
ccApi = Radiobutton(window, text="CCAPI", value=1).place(x=85, y=140)
apiButton = Button(window, text="Stablish Connection").place(x=26, y=180)
ipPs3 = Entry(window).place(x=20, y=100)
ipLabel = Label(window, text="IP ADDRESS").place(x=37, y=70)
genLabel = Label(window, text="CONSOLE ID").place(x=287, y=70)


window.mainloop()
