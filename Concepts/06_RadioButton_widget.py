# W = Radiobutton(master, options)   

# Name of the option	                Description
# 
# anchor	            This option is used to represent the exact position of the text within the widget, in the case of the widget contains more space than the requirement of the text. The default value of this option is CENTER.
# bg	                This option represents the background color of the widget.
# activebackground	This option represents the background color of the widget when it is under focus.
# activeforeground	This option represents the font color of the widget when it is under focus.
# borderwidth     	This option is used to represent the size of the border.
# bitmap	            If you want to display graphics on the widget then you can set this widget to any graphical or image object.
# command	            This option is used to set the procedure which must be called every time when the state of the radiobutton is changed.
# cursor	            This option will convert the mouse pointer to the specified cursor type and it can be set to an arrow, dot, etc.
# font	            This option is used to represent the font type of the text of the widget.
# fg	                This option is used to represent the foreground color of the text of the widget.
# height	            This option indicates the vertical dimension of the widget
# width	            This option indicates the horizontal dimension of the widget and it is represented as the number of characters.
# padx	            This option represents the horizontal padding of the widget.
# pady	            This option represents the vertical padding of the widget
# highlightcolor	    This option is used to represent the color of the focus highlight when the widget is under the focus
# highlightbackground	This option is used to represent the color of the focus highlight when the widget is not under the focus.
# image	            If you want to display an image on the widget then this option will be set to an image rather than the text
# justify	            This option is used to represent the justification of the multiline text. The default value is CENTER. Other values are LEFT, RIGHT.
# relief	            This option is used to represent the type of border. The default value is FLAT.
# selectcolor     	This option indicates the color of the radiobutton when it is selected
# selectimage	        This option indicates the image to be displayed on the radiobutton when it is selected
# state	            This option is used to represent the state of the radio button. The default state of the Radiobutton is NORMAL. You can also set the state to DISABLED in order to make the radiobutton unresponsive.
# text	            This option indicates the text to be displayed on the radiobutton.
# textvariable	    This option is used to control the text represented by the widget. The textvariable can be set to the text that is needed to be shown on the widget.
# underline	        This option can be set to an existing number in order to specify that nth letter of the string will be underlined. Its default value is -1 which indicates no underline
# variable	        This option is also known as the control variable which is used to keep the track of user's choices. Thus this variable is shared among all radiobuttons.
# value	            This option of each radiobutton is assigned to the control variable when it is turned on by the user.
# wraplength      	This option is used to wrap the text to the number of lines just by setting this option to the desired number so that each line contains only that number of characters.

# Method Name	            Description
# 
# deselect()	        This method is used to deselect or turns off the radio button
# select()	            This method is used to select the radio button
# invoke()	            This method is generally used to call a function when the state of radio button gets changed.
# flash()	            This method is generally used to flash the radio button between its normal and active colors many times.

from tkinter import * 
from tkinter.ttk import *

win= Tk() 
win.geometry('200x200') 
v = StringVar(win, "1") 

# we will add Style class to add style to Radiobutton  
style = Style(win) 
style.configure("TRadiobutton", background = "light blue", 
				foreground = "orange", font = ("arial", 14, "bold")) 

# Dictionary to create multiple buttons 
values = {"RadioButton 1" : "1", 
		"RadioButton 2" : "2", 
		"RadioButton 3" : "3" 
		} 

for (text, value) in values.items(): 
	Radiobutton(win, text = text, variable = v, 
				value = value).pack(side = TOP, ipady = 3) 
mainloop() 