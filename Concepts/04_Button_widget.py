# W = Button(master, options)  

# Option name	                        Description
# 
# activebackground	                This option indicates the background of the button at the time when the mouse hovers the button.
# bd	                            This option is used to represent the width of the border in pixels.
# bg	                            This option is used to represent the background color of the button.
# command	                        The command option is used to set the function call which is scheduled at the time when the function is called.
# activeforeground	                This option mainly represents the font color of the button when the mouse hovers the button.
# fg	                            This option represents the foreground color of the button.
# font	                            This option indicates the font of the button.
# height	                        This option indicates the height of the button. This height indicates the number of text lines in the case of text lines and it indicates the number of pixels in the case of images.
# image	                            This option indicates the image displayed on the button.
# higlightcolor	                    This option indicates the highlight color when there is a focus on the button
# justify	                        This option is used to indicate the way by which the multiple text lines are represented. For left justification, it is set to LEFT and it is set to RIGHT for the right justification, and CENTER for the center justification.
# padx	                            This option indicates the additional padding of the button in the horizontal direction.
# pady	                            This option indicates the additional padding of the button in the vertical direction.
# underline	                        This option is used to underline the text of the button.
# width	                            This option specifies the width of the button. For textual buttons, It exists as a number of letters or for image buttons it indicates the pixels.
# Wraplength	                    In the case, if this option's value is set to a positive number, the text lines will be wrapped in order to fit within this length.
# state	                            This option's value set to DISABLED to make the button unresponsive. The ACTIVE mainly represents the active state of the button.

import tkinter
from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("300x150")
def click():
    messagebox.showinfo("Hello", "Green Button clicked")
a = Button(top, text="yellow", activeforeground="yellow", activebackground="orange", pady=10)
b = Button(top, text="Blue", activeforeground="blue", activebackground="orange", pady=10)
# adding click function to the below button
c = Button(top, text="Green", command=click, activeforeground = "green", activebackground="orange", pady=10)
d = Button(top, text="red", activeforeground="yellow", activebackground="orange", pady=10)

a.pack(side = LEFT)
b.pack(side = RIGHT)
c.pack(side = TOP)
d.pack(side = BOTTOM)
top.mainloop()

