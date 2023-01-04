# w = Spinbox(master, option=value)

# Name of the Option	                    Description
# bg	                        This option is used for the background color of the widget.
# bd	                        This option is used for the border width of the widget
# command	                    This option is used to indicate the associated function with the widget which is called every time the state of the widget is changed.
# cursor	                    With the help of this option, your mouse pointer type can be changed to the cursor type that is assigned to this option.
# activebackground	            This option indicates the background color of the widget when it is under the focus
# disabledbackground	        This option is used to indicate the background color of the widget when it is disabled.
# disabledforeground	        This option is used to indicate the foreground color of the widget when it is disabled.
# font	                        This option specifies the font type of text inside the widget.
# fg	                        This option specifies the foreground color of the widget.
# format	                    This option is mainly used for the format string. There is no default value of this option.
# from_	                        This option is used to indicate the starting range of the widget
# justify	                    This option specifies the alignment of multiple lines in the label. The default value is LEFT. Other values are RIGHT and CENTER.
# relief	                    This option indicates the type of border. The default value of this option is SUNKEN.
# state	                        This option is used to represent the state of the widget. The default value of this option is NORMAL. Other values are "DISABLED", "read-only", etc.
# validate	                    This option is used to control how to validate the value of the widget
# to	                        This option represents the maximum limit of the widget value. The other value is specified by the from_ option
# repeatdelay	                This option is mainly used to control the autorepeat button. The value here is in milliseconds.
# repeatinterval	            This option is similar to repeatdelay option. The value here is also given in milliseconds.
# validatecommand	            This option is associated with the function callback that is used for the validation of the content of the widget.
# xscrollcommand	            This option is mainly used with the set() method of the scrollbar widget to make this widget horizontally scrollable
# wrap	                        This option is mainly used to wrap-up the up and down button of the Spinbox
# width	                        This option indicates the width of the widget.
# vcmd	                        This option is similar to validatecommand.
# values	                    This option represents the tuple which contains the values for the widget
# textvariable	                It is a control variable that is used to control the text of the widget

# Method Name	                        Description
# invoke(element)	            This method is used to invoke the callback that is associated with the widget.
# insert(index,string)	        We use this method mainly to insert the string at the given specified index
# index(index)	                To get the absolute value of the given index this method will be used
# identify(x,y)             	This method is used to identify the widget's element in the specified range
# get(startindex, endindex)	    This method is used to get the characters in the specified range
# delete(startindex, endindex)	This method is used to delete the characters in the specified range

from tkinter import *

win = Tk() 
win.geometry("300x200") 

w = Label(win, text ='StudyTonight', fg="navyblue",font = "50") 
w.pack() 

sp = Spinbox(win, from_= 0, to = 50) 
sp.pack() 

win.mainloop() 