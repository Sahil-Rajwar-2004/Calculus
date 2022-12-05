from tkinter import Tk
from tkinter import Frame
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Menu
from tkinter import Scrollbar
from tkinter import messagebox
from tkinter import Text
from tkinter import StringVar
from tkinter import ttk
from tkinter import BOTH
from tkinter import END
from tkinter import DISABLED
from tkinter import NORMAL
from tkinter import INSERT
from tkinter import RIGHT
from tkinter import Y
import webbrowser
import homepage
import sympy
import about

def integration():
    try:
        getArg = displayEntry.get()
        arg = box.get()
        if arg == "dx":
            wrt = sympy.Symbol("x")
        elif arg == "dy":
            wrt = sympy.Symbol("y")
        else:
            messagebox.showerror("Error","It's a Bug, check the source code!")
        res = sympy.integrate(getArg,wrt)
        text.config(state = NORMAL)
        text.insert(INSERT,res)
        text.insert(INSERT,"\n")
        text.insert(INSERT,"-----------------------\n")
        text.config(state = DISABLED)
    except Exception as e:
        messagebox.showerror("Error",e)

def differentiation():
    try:
        getArg = displayEntry.get()
        arg = box.get()
        if arg == "dx":
            wrt = sympy.Symbol("x")
        elif arg == "dy":
            wrt = sympy.Symbol("y")
        else:
            messagebox.showerror("Error","It's a Bug, check the source code!")
        res = sympy.diff(getArg,wrt)
        text.config(state = NORMAL)
        text.insert(INSERT,res)
        text.insert(INSERT,"\n")
        text.insert(INSERT,"-----------------------\n")
        text.config(state = DISABLED)
    except Exception as e:
        messagebox.showerror("Error",e)

def aboutme():
    messagebox.showinfo("About Me",f"Author: {about.author}\nVerion: {about.version}")

def homePage():
    webbrowser.open(homepage.url)

def reset():
    displayEntry.delete(0,END)
    box.current(0)

app = Tk()
app.geometry("600x500")
app.title("Calculus Calculator")
app.resizable(False,False)

mainMenu = Menu(app)
app.config(menu = mainMenu)
mainMenu.add_command(label = "About",command = aboutme)
mainMenu.add_command(label = "HomePage",command = homePage)

displayFrame = Frame(app)
displayFrame.pack(fill = BOTH,padx = 5,pady = 5)
var1 = StringVar()
displayEntry = Entry(displayFrame,textvariable = var1,font = ("ubuntu",16),width = 30,border = 0)
displayEntry.grid(row = 0,column = 0,padx = 5,pady = 5)
var2 = StringVar()
box = ttk.Combobox(displayFrame,values = ["dx","dy"],textvariable = var2,font = ("ubuntu",13),state = "readonly",width=10)
box.grid(row = 0,column = 1,padx = 0,pady = 5)
box.current(0)

buttonFrame = Frame(app)
buttonFrame.pack(fill = BOTH,padx = 5,pady = 5)
integrateBtn = Button(buttonFrame,text = "Integrate",font = ("ubuntu",12),command = integration,border = 0)
integrateBtn.grid(row = 0,column = 0,padx = 5,pady = 5)
derivativeBtn = Button(buttonFrame,text = "Differentiate",font = ("ubuntu",12),command = differentiation,border = 0)
derivativeBtn.grid(row = 0,column = 1,padx = 5,pady = 5)
resetBtn = Button(buttonFrame,text = "Clear",font = ("ubuntu",12),command = reset,border = 0)
resetBtn.grid(row = 0,column = 2)

mainFrame = Frame(app)
mainFrame.pack(fill = BOTH,padx = 5,pady = 5)
label = Label(mainFrame,text = "Result",font = ("ubuntu",12))
label.pack(fill = BOTH,padx = 5,pady = 5)
scrollBar = Scrollbar(mainFrame)
scrollBar.pack(side = RIGHT,fill = Y)
text = Text(mainFrame,font = ("ubuntu",13),state = DISABLED,yscrollcommand = scrollBar.set)
text.pack(fill = BOTH,padx = 5,pady = 5)
scrollBar.config(command = text.yview)

app.mainloop()
