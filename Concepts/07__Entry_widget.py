# w = Entry(master, option=value)

# Option Name	            Description
# bg	                This option is used for the background color of the widget.
# bd	                This option is used for the width of the border in pixels. Its default value is 2 pixels.
# cursor                This option helps in changing the mouse pointer to the cursor type and set it to the arrow, dot, etc.
# exportselection	    It is important to note that By Default, the text that is written inside the entry box will get automatically copied to the clipboard. If you do not want to copy the text then set the value of exportselection to 0.
# fg	                This option is used to indicate the color of the text.
# font	                This option is used to represent the font type of the text
# highlightbackground	This option is used to represent the color to display in the traversal highlight region when the widget does not have the input focus.
# highlightcolor	    This option is used to represent the color to use for the traversal highlight rectangle which is drawn around the widget when the widget has an input focus.
# relief	            This option is used to indicate the type of border. The default value of this option is FLAT. It has more values like GROOVE, RAISED,RIGID.
# justify	            This option is used to specify how the text is organized in the case if the text contains multiple lines.
# selectbackground	    This option is used to indicate the background color of the selected text.
# selectforeground	    It is used to set the font of the selected task.
# selectborderwidth	    This option indicates the width of the border to display around the selected task
# width	                This option indicates the width of the image or width of text to display.
# textvariable	        With the help of this option, you will be able to retrieve the current text from your entry widget, you need to set this option to an instance of the StringVar class.
# show	                This option is used to show the entry text of some other type instead of the string. For example, we type the password using stars (*).
# xscrollcommand	    You can link the entry widget to the horizontal scrollbar if you want the user to enter more text rather then the actual width of the widget.
# insertbackground	    This option mainly represents the color to use as a background in the area covered by the insertion cursor. and thus this color will normally override the normal background for the widget.

# Method Name	                    Description
# delete(first, last=None)	    This method is used to delete the specified characters inside the widget.
# get()	                        This method is used to get the entry widget's current text as a string.
# icursor(index)                This method is used to set the insertion cursor just before the character at the specified index.
# index(index)              	This method is used to place the cursor to the left of the character written at the specified index.
# select_clear()	            This method is used to clear the selection in the case if some selection has been done.
# select_present()	            If there is a presence of some selection then this method will return true otherwise, it will return false.
# insert(index, s)	            This method is mainly used to insert the specified string(s) before the character placed at the specified index
# select_adjust(index)	        This method mainly includes the selection of the character present at the specified index
# select_form(index)	        This method mainly sets the anchor index position to the character specified by the index.
# select_range(start, end)	    This method is used to select the characters to exist between the specified range
# select_to(index)	            This method mainly selects all the characters from the beginning to the specified index
# xview(index)	                This method is used to link the entry widget to a horizontal scrollbar
# xview_scroll(number, what)	This method is mainly used to make the entry widget scrollable horizontally


from tkinter import * 
   
win = Tk()  
  
win.geometry("400x250")  
  
name = Label(win, text = "Name").place(x = 30,y = 50)  
  
email = Label(win, text = "Email").place(x = 30, y = 90)  
  
password = Label(win, text = "Password").place(x = 30, y = 130)  
  
submitbtn = Button(win, text = "Submit",activebackground = "red", activeforeground = "blue").place(x = 30, y = 170)  
  
entry1 = Entry(win).place(x = 80, y = 50)  

entry2 = Entry(win).place(x = 80, y = 90)  
 
entry3 = Entry(win).place(x = 95, y = 130)  
  
win.mainloop()