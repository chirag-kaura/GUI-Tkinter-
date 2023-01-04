# W = Listbox(master, options)   

# Name of Option	                    Description
# bg	                    This option indicates the background color of the widget.
# bd	                    This option is used to represent the size of the border. The default value is 2 pixels.
# cursor	                With the help of this option, the mouse pointer will look like the cursor type like dot, arrow, etc.
# font	                    This option indicates the font type of the Listbox items.
# fg	                    This option indicates the color of the text.
# height	                This option is used to represents the count of the lines shown in the Listbox. The default value of this option is 10.
# highlightcolor	        This option is used to indicate the color of the Listbox items when the widget is under focus.
# highlightthickness	    This option is used to indicate the thickness of the highlight.
# relief	                This option indicates the type of border. The default value is SUNKEN.
# selectbackground	        This option is used to indicate the background color that is used to display the selected text.
# selectmode	            This option is used to determine the number of items that can be selected from the list. It can set to BROWSE, SINGLE, MULTIPLE, EXTENDED.
# width	                    This option is used to represent the width of the widget in characters.
# xscrollcommand	        This option is used to let the user scroll the Listbox horizontally.
# yscrollcommand	        This option is used to let the user scroll the Listbox vertically.
# 
# 
# Method	                            Description
# activate(index)	            This method is mainly used to select the lines at the specified index.
# curselection()	            This method is used to return a tuple containing the line numbers of the selected element or elements, counting from 0. If nothing is selected, return an empty tuple.
# delete(first, last = None)	This method is used to delete the lines which exist in the given range.
# get(first, last = None)	    This method is used to get the list of items that exist in the given range.
# index(i)	                    This method is used to place the line with the specified index at the top of the widget.
# insert(index, *elements)	    This method is used to insert the new lines with the specified number of elements before the specified index.
# nearest(y)	                This method is used to return the index of the nearest line to the y coordinate of the Listbox widget.
# see(index)	                This method is used to adjust the position of the Listbox to make the lines specified by the index visible.
# size()	                    This method returns the number of lines that are present in the Listbox widget.
# xview()	                    This method is used to make the widget horizontally scrollable.
# xview_moveto(fraction)	    This method is used to make the Listbox horizontally scrollable by the fraction of the width of the longest line present in the Listbox.
# xview_scroll(number, what)	This method is used to make the listbox horizontally scrollable by the number of characters specified.
# yview()	                    This method allows the Listbox to be vertically scrollable.
# yview_moveto(fraction)	    This method is used to make the listbox vertically scrollable by the fraction of the width of the longest line present in the Listbox.
# yview_scroll (number, what)	This method is used to make the listbox vertically scrollable by the number of characters specified.

from tkinter import *

top = Tk()

top.geometry("200x250")

lbl = Label(top, text="List of Programming Languages")

listbox = Listbox(top)

listbox.insert(1,"Python")

listbox.insert(2, "Java")

listbox.insert(3, "C")

listbox.insert(4, "C++")

lbl.pack()
listbox.pack()
  
top.mainloop()
