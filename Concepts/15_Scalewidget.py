# W = Scale(master, options)   

# Name of the option	                        Description
# activebackground	            This option represents the background color of the widget when it is under focus.
# bg	                        This option represents the background color of the widget
# bd	                        This option represents the border size of the widget. The default value is 2 pixels.
# cursor	                    With the help of this option, the mouse pointer will be changed to a specific cursor type and it can be an arrow, dot, etc.
# command	                    This option will be set to the procedure which is called every time when we move the slider. If we move the slider rapidly, the callback to the procedure is done when it settles.
# digits	                    When the control variable which is used to control the scale data is of string type, then this option is mainly used to specify the number of digits when the numeric scale is converted to a string.
# fg	                        This option indicates the foreground color of the text
# font	                        This option indicates the font type of the text
# from_	                        This option is used to represent one end of the widget range.
# highlightcolor	            This option indicates the highlight color when the widget is under the focus
# highlightbackground	        This option indicates the highlight color when the widget is not under the focus
# label	                        This option can be set to some text which then can be shown as a label with the scale. If the scale is horizontal then it is shown in the top left corner or if the scale is vertical then it shown in the top right corner.
# length	                    This option indicates the length of the widget. It represents the X dimension if the scale is in the horizontal direction and it represents the Y dimension if the scale is in a vertical direction.
# relief	                    This option is used to specify the border type. Its default value is FLAT
# orient	                    This option can be set to either horizontal or vertical depending upon the type of the scale.
# resolution	                This option will be set to the smallest change which is made to the value of the scale
# repeatdelay	                This option is mainly used to tell the duration up to which the button is to be pressed before the slider starts moving in that direction repeatedly. its default value is 300 ms
# sliderlength	                This option represents the length of the slider window along the length of the scale. Its default value is 30 pixels. Also, you can change it to the appropriate value.
# showvalue	                    By default, the value of the scale is shown in the text form, also we can set this option to 0 in order to suppress the label.
# state	                        By default, the state of the scale widget is active. To make it unresponsive you can also set it to DISABLED
# width	                        This option is used to represent the width of the trough part of the widget
# variable	                    This option is used to represent the control variable for the scale
# to                        	This option is used represents a float or integer value that specifies the other end of the range represented by the scale
# takefocus	                    Generally, the focus will cycle through the scale widgets. If you don't want this behavior you can set this option to 0.
# tickinterval	                With the help of this option, scale values are displayed on the multiple of the specified tick interval. The default value of this option is 0.
# troughcolor	                This option is used to set the color for the trough


# Methods
# get():
# set(value):

from tkinter import *

win = Tk() 
win.geometry("400x300") 

v = DoubleVar() 

def show(): 	
	sel = "The Vertical Scale Value is = " + str(v.get()) 
    # adding scale value to label to show
	scale_val.config(text=sel, font=("Courier", 16)) 

scl = Scale(win, variable=v, from_=60, to=1, orient=VERTICAL) 

mainlabel = Label(win, text="The Vertical Slider") 

btn = Button(win, text ="Show Slider Value", 
			command = show, 
			bg = "darkblue", 
			fg = "white") 

# creating another label to show the scale value
scale_val = Label(win) 

scl.pack(anchor = CENTER) 
mainlabel.pack() 
btn.pack() 
scale_val.pack() 

win.mainloop() 