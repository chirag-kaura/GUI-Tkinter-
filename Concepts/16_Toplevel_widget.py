# W = Toplevel(master,options) 

# Name of the option	                Description
# bd	                        To represent the border size of the window
# bg	                        To represent the background color of the window
# class_	                    Generally, the text selected in the text widget is simply exported to be selected to the window manager. You can also set the value of this option to 0 to make this kind of behavior false.
# cursor	                    This option will convert the mouse pointer to the specified cursor type and it can be set to an arrow, dot, etc.
# width	                        This option is used to represent the width of the window
# height	                    This option is used to represent the height of the window
# font	                        This option indicates the font type of the text to be inserted into the widget.
# fg	                        This option is used to indicate the foreground color of the widget.
# relief	                    This option indicates the type of the window.


# Method	                            Description
# title(string)	                This method is used to define the title for the window.
# withdraw()	                This method is used to delete the window but it would not destroy the window.
# positionfrom(who)	            This method is used to define the position controller
# sizefrom(who)	                This method is used to define the size controller.
# minsize(width,height)	        This method is used to declare the minimum size for the window
# maxsize(width,height)	        This method is used to declare the maximum size for the window
# resizable(width,height)	    This method is used to control whether the window can be resizable or not.
# transient([master])	        This method is used to convert the window into a temporary window
# iconify()	                    This method is used to convert the top-level window into an icon.
# deiconify()	                This method is mainly used to display the window.
# frame()	                    To indicate a system-dependent window identifier this method is used.
# group(window)	                This method is used to add a top-level window to a specified window group
# protocol(name,function)	    This method is used to indicate a function which will be called for the specific protocol
# state()	                    This method is used to get the current state of the window. Some Possible values of this option are normal, iconic, withdrawn, and icon.


from tkinter import *  
  
win = Tk()  
  
win.geometry("200x200")  
  
def open():  
    top = Toplevel(win)  
    top.mainloop()  
  
btn = Button(win, text="open", command=open)  
  
btn.place(x=75, y=50)  
  
win.mainloop()