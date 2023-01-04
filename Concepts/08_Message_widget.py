# W = Message(master,options)  

# Name of the option	            Description
# anchor	                It is mainly used to decide the exact position of the text within the provided space. The default value of this option is CENTER.
# bg	                    This option denotes the background color of the widget.
# bd	                    This option is used to indicate the border width of the widget. The default value of this is 2 pixels.
# bitmap	                In order to display graphics on the widget, this option will be used. You can set it to any graphical or image object.
# cursor	                With the help of this option, the mouse pointer will be changed to a specific cursor type like an arrow, dot, etc.
# fg	                    This option is used to indicate the font color of the widget text.
# font	                    This option is used to indicate the font type of the widget text.
# height	                This option is used to indicate the vertical dimension of the message widget.
# image	                    This option is used to indicate the image on the widget.
# justify	                This option is used for the justification of the text on the widget. It can be CENTER, LEFT, RIGHT
# padx	                    This option is used for the horizontal padding of the widget.
# pady	                    This option is used for the vertical padding of the widget.
# relief	                This option is used to specify the border type. Its default value is FLAT
# underline	                This option can be set to an existing number in order to specify that nth letter of the string will be underlined. Its default value is -1 which indicates no underline.
# text	                    If you want to display one or more lines of text in a label widget you need to set this option to a string containing the text. You can use "\n" just in order to enter multiple lines
# textvariable	            This option is used to control the text represented by the widget. The textvariable can be set to the text that is needed to be shown on the widget.
# width	                    This option is used to indicate the horizontal dimension of the widget in the number of characters and not in pixels.
# wraplength	            This option is used to wrap the text to the number of lines just by setting this option to the desired number so that each line contains only that number of characters.

from tkinter import *

win = Tk() 
win.geometry("300x200") 

w = Label(win, text ='StudyTonight', font = "90",fg="Navyblue") 
w.pack() 
	
msg = Message(win, text = "Best place to learn coding online") 
	
msg.pack() 

win.mainloop() 