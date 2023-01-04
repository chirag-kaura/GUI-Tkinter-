# W = Scrollbar(master, options)   

# Name of the Option	                    Description
# activebackground              	This option represents the background color of the widget when it is under focus.
# bg	                            This option represents the background color of the widget
# bd	                            This option represents the border size of the widget. The default value is 2 pixels.
# cursor	                        With the help of this option, the mouse pointer will be changed to a specific cursor type and it can be an arrow, dot, etc.
# command	                        This option will be set to the procedure associated which is called every time the scrollbar is moved.
# elementborderwidth	            This option mainly represents the border width around the arrowheads and the slider. The default value of this option is -1.
# highlightthickness	            This option represents the thickness of the focus highlights
# highlightbackground	            This option indicates the highlight color when the widget is not under the focus
# highlightcolor	                This option indicates the highlight color when the widget is under the focus
# jump	                            This option is used to control the behavior of the scroll jump. If this option is set to 1, then the callback is called at the time when the user releases the mouse button.
# orient	                        This option can be set to either horizontal or vertical depending upon the orientation of the scrollbar.
# width	                            This option represents the width of the scrollbar.
# troughcolor                   	This option is used to set the color for the trough
# takefocus                     	By default, you can tab the focus through this widget. If you don't want this behavior you can set this option to 0.
# repeatdelay	                    This option is mainly used to tell the duration up to which the button is to be pressed before the slider starts moving in that direction repeatedly. its default value is 300 ms
# repeatinterval	                The default value of this option is 100

# Methods
# get():
# set(first, last):

from tkinter import *  
  
win= Tk()  
sbb = Scrollbar(win)  
sbb.pack(side = RIGHT, fill = Y)  
  
mylist = Listbox(win, yscrollcommand = sbb.set)  
  
for line in range(45):  
    mylist.insert(END, "Value " + str(line))  
  
mylist.pack(side = LEFT)
sbb.config(command = mylist.yview)
  
mainloop()