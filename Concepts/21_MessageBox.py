# from tkinter import messagebox
# messagebox.function_name(title, message [, options])  

# Tkinter MessageBox - showwarning()
from tkinter import *  
  
from tkinter import messagebox  
  
win = Tk()  
win.geometry("200x200")  
messagebox.showwarning("warning","This is a Warning")  
  
win.mainloop()  


# Tkinter MessageBox - askquestion()
from tkinter import *  
from tkinter import messagebox  
  
win = Tk()  
win.geometry("100x100")  
messagebox.askquestion("Confirm","Are you sure about it?")  
win.mainloop()  


# Tkinter MessageBox - askretrycancel()
from tkinter import *  
from tkinter import messagebox  
  
win= Tk()  
win.geometry("100x100")  
messagebox.askretrycancel("Application"," wanna try again?")  
  
win.mainloop()  


# Tkinter MessageBox - showerror()
from tkinter import *  
from tkinter import messagebox  
  
top = Tk()  
top.geometry("100x100")  
messagebox.showerror("errorWindow","oops!!!Error")  
top.mainloop()  