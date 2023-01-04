# w = CheckButton(master, option=value)

# Option name	                Description

# activebackground      	This option indicates the background color of the checkbutton at the time when the checkbutton is under the cursor.
# bd	                    This option indicates the size of the border around the corner. The default size is 2 pixels.
# bg	                    This option is used to represent the background color of the checkbutton.
# bitmap	                This option is mainly used to display the image on the button.
# command	                The command option is used to set the function call which is scheduled at the time when the state of checkbutton is changed.
# activeforeground	        This option mainly represents the foreground color of the button when the checkbutton is under the cursor.
# fg                    	This option represents the text color of the checkbutton.
# font                  	This option indicates the font of the checkbutton.
# height                	This option indicates the height of the button. This height indicates the number of text lines in the case of text lines and it indicates the number of pixels in the case of images. the default value is 1.
# image	                    This option indicates the image representing the checkbutton.
# cursor	                This option helps in changing the mouse pointer to the cursor name when it is over the checkbutton.
# disableforeground	        This option is the color which is used to indicate the text of a disabled checkbutton.
# higlightcolor         	This option indicates the highlight color when there is a focus on the checkbutton
# justify	                This option is used to indicate the way by which the multiple text lines are represented. For left justification, it is set to LEFT and it is set to RIGHT for the right justification, and CENTER for the center justification.
# padx	                    This option indicates the padding of the checkbutton in the horizontal direction.
# pady	                    This option indicates the padding of the checkbutton in the vertical direction.
# underline	                This option is used to underline the text of the checkbutton.
# width	                    This option specifies the width of the checkbutton. For textual buttons, It exists as a number of letters or for image buttons it indicates the pixels.
# Wraplength	            In the case If this option is set to an integer number, then the text will be broken into the number of pieces.
# variable	                This option is mainly used to represents the associated variable that is used to track the state of the checkbutton
# offvalue	                The associated control variable of checkbutton is set to 0 by default if the button is (off). you can also change the state of an unchecked variable to some other one.
# onvalue	                The associated control variable of checkbutton will be set to 1 when it is set (on). Any alternate value will be supplied for the on state by setting onvalue to that value.
# text	                    This option is used to indicate the label just next to the checkbutton. For multiple lines use "\n".
# state	                    This option mainly used to represent the state of the checkbutton. Its default value= normal. It can be changed to DISABLED to make the checkbutton unresponsive. The value of this button is ACTIVE when checkbutton is under focus
# selectcolor	            This option indicates the color of the checkbutton when it is set. Its default value is Red.
# selectimage	            This option indicates the image on the checkbutton when it is set.

# Method Name	                Description
# 
# invoke()	                This method in checkbutton widget is used to invoke the method associated with the checkbutton.
# select()	                This method in the checkbutton widget is called to turn on the checkbutton.
# deselect()	            This method in the checkbutton widget is called to turn off the checkbutton.
# toggle()	                This method in the checkbutton widget is used to toggle between the different Checkbuttons.
# flash()	                This method in the checkbutton widget is used to flashed between active and normal colors.

from tkinter import *

root = Tk() 
root.geometry("300x300") 

w = Label(root, text ='StudyTonight', fg="Blue",font = "100") 
w.pack() 

Checkbutton1 = IntVar() 
Checkbutton2 = IntVar() 
Checkbutton3 = IntVar() 

Button1 = Checkbutton(root, text = "Homepage", 
					variable = Checkbutton1, 
					onvalue = 1, 
					offvalue = 0, 
					height = 2, 
					width = 10) 

Button2 = Checkbutton(root, text = "Tutorials", 
					variable = Checkbutton2, 
					onvalue = 1, 
					offvalue = 0, 
					height = 2, 
					width = 10) 

Button3 = Checkbutton(root, text = "Contact us", 
					variable = Checkbutton3, 
					onvalue = 1, 
					offvalue = 0, 
					height = 2, 
					width = 10) 
	
Button1.pack() 
Button2.pack() 
Button3.pack() 

mainloop() 