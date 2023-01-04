# W = Menubutton(master, options)   

# Option name	                      Description
# activebackground	        This option indicates the background color of the menubutton at the time when the mouse hovers the menubutton.
# bd	                    This option is used to represent the width of the border in pixels. The default value is 2 pixels.
# bitmap	                This option will be set to the graphical content which is to be displayed to the widget.
# bg	                    This option is used to represent the background color of the widget.
# cursor	                This option indicates the cursor when the mouse hovers the menubutton.
# activeforeground	        This option mainly represents the font color of the widget at the time when the widget is under the focus
# fg	                    This option represents the foreground color of the widget.
# direction	                With the help of this option, you can specify the direction so that menu can be displayed to the specified direction of the button. You can Use LEFT, RIGHT, or ABOVE to place the widget accordingly.
# disabledforeground	    This option indicates the text color of the widget when the widget is disabled
# height	                This option indicates the height of the menubutton. This height indicates the number of text lines in the case of text lines and it indicates the number of pixels in the case of images.
# image	                    This option indicates the image displayed on the menubutton.
# higlightcolor         	This option indicates the highlight color when there is a focus on the button
# justify	                This option is used to indicate the way by which the multiple text lines are represented. For left justification, it is set to LEFT and it is set to RIGHT for the right justification, and CENTER for the center justification.
# padx	                    This option indicates the additional padding of the widget in the horizontal direction.
# pady	                    This option indicates the additional padding of the widget in the vertical direction.
# menu	                    This option is used to indicate the menu associated with the menubutton
# width	                    This option specifies the width of the widget. For textual buttons, It exists as a number of letters or for image buttons it indicates the pixels
# Wraplength	            In this case, if this option's value is set to a positive number, the text lines will be wrapped in order to fit within this length.
# state	                    As the normal state of menubutton is enabled.It can be set to disable to make the menubutton unresponsive.
# text	                    This option is used to indicate the text on the widget.
# textvariable          	A control variable of class StringVar can be associated with this menubutton. If you will set that control variable then it will change the displayed text.
# underline	                This option is mainly used to represent the index of the character in the text of the widget which is to be underlined. The indexing generally starts with zero in the text.
# relief	                This option is used to specify the border type. Its default value is RAISED


from tkinter import *
import tkinter

win = Tk()

mbtn = Menubutton(win, text="Courses", relief=RAISED)
mbtn.grid()
mbtn.menu = Menu(mbtn, tearoff = 0)
mbtn["menu"] = mbtn.menu

pythonVar = IntVar()
javaVar = IntVar()
phpVar = IntVar()

mbtn.menu.add_checkbutton(label="Python", variable=pythonVar)
mbtn.menu.add_checkbutton(label="Java", variable=javaVar)
mbtn.menu.add_checkbutton(label="PHP", variable=phpVar)

mbtn.pack()
win.mainloop()