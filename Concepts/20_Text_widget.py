# W = Text(master, options)   

# Name of the option	                    Description
# bd	                            This option represents the border width of the widget.
# bg	                            This option indicates the background color of the widget.
# exportselection	                This option is used to export the selected text in the selection of the window manager. If you do not want to export the text then you can set the value of this option to 0.
# cursor	                        This option will convert the mouse pointer to the specified cursor type and it can be set to an arrow, dot, etc.
# font	                            This option is used to indicate the font type of the text.
# fg	                            This option indicates the text color of the widget
# height	                        This option indicates the vertical dimension of the widget and it is mainly in the number of lines.
# highlightbackground	            This option indicates the highlightcolor at the time when the widget isn't under the focus.
# higlightthickness	                This option is used to indicate the thickness of the highlight. The default value of this option is 1.
# highlightcolor	                This option indicates the color of the focus highlight when the widget is under the focus.
# insertbackground	                This option is used to represent the color of the insertion cursor.
# padx	                            This option indicates the horizontal padding of the widget.
# pady	                            This option indicates the vertical padding of the widget.
# relief	                        This option indicates the type of the border of the widget. The default value of this option is SUNKEN.
# state	                            If the value of this option is set to DISABLED then the widget becomes unresponsive to mouse and keyboard
# tabs	                            This option is used to control how the tab character is used for the positioning of the text
# width                         	This option represents the width of the widget and this is in characters.
# wrap	                            To wrap wider lines into multiple lines this option is used. The default value of this option is CHAR which breaks the line which gets too wider at any character
# xscrollcommand	                If you want to make the Text widget horizontally scrollable, then you can set this option to the set() method of Scrollbar widget
# yscrollcommand                	If you want to make the Text widget vertically scrollable, then you can set this option to the set() method of Scrollbar widget
# spacing1	                        This option indicates the vertical space to insert above each line of the text.
# spacing2	                        This option is used to specify how much extra vertical space to add between displayed lines of text when a logical line wraps. The default value of this option is 0
# spacing3	                        This option indicates the vertical space to insert below each line of the text.
# selectbackground              	This option indicates the background color of the selected text.
# selectborderwidth	                This option indicates the width of the border around the selected text.
# insertofftime                 	This option represents the time amount in Milliseconds and during this time the insertion cursor is off in the blink cycle
# insertontime	                    This option represents the time amount in Milliseconds and during this time the insertion cursor is on in the blink cycle
# insertborderwidth             	In order to represent the width of the border around the cursor, we use this option. The default value of this option is 0.

# Method	                            Description
# index(index)	                    This method is used to get the specified index.
# see(index)	                    This method returns true or false on the basis that if the string is visible or not at the specified index.
# insert(index,string)	            This method is used to insert a string at the specified index.
# get(startindex,endindex)	        This method returns the characters in the specified range
# delete(startindex,endindex)	    This method deletes the characters in the specified range

# Methods for Tag Handling
# tag_config()
# tag_add(tagname, startindex, endindex)
# tag_delete(tagname)
# tag_remove(tagname, startindex, endindex)

# Methods for Mark Handling
# index(mark)
# mark_names()
# mark_gravity(mark, gravity)
# mark_set(mark, index)
# mark_unset(mark)

import tkinter as tk 
from tkinter import *

win = Tk() 

#to specify size of window. 
win.geometry("250x170") 

# To Create a text widget and specify size. 
T = Text(win, height = 6, width = 53) 

# TO Create label 
l = Label(win, text = "Quote for the Day") 
l.config(font =("Courier", 14)) 

Quote = """Success usually comes to those who are too busy to be looking for it"""

# Create a button for the next text. 
b1 = Button(win, text = "Next", ) 

# Create an Exit button. 
b2 = Button(win, text = "Exit", 
			command = win.destroy) 

l.pack() 
T.pack() 
b1.pack() 
b2.pack() 

# Insert the Quote 
T.insert(tk.END, Quote) 

tk.mainloop() 