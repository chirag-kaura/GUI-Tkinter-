# W = Menu(master, options)   

# Name of the Option	                Description
# activebackground	            This option is used to indicate the background color of the widget when the widget is under the focus.
# activeforeground	            This option indicates the font color of text of the widget when the widget has the focus.
# activeborderwidth	            This option is used to indicate the width of the border of the widget when it is under the mouse(when it is active). The default value of this option is 1 pixel.
# bd	                        This option is used to indicate the border width of the widget
# bg	                        This option indicates the background color of the widget.
# cursor	                    This option indicates the cursor when the mouse hovers the menu.
# disabledforeground	        This option indicates the text color of the widget when the widget is disabled
# font	                        This option is used to indicate the font type of the text of widget
# fg	                        This option specifies the foreground color of the widget.
# relief	                    This option is used to specify the border type. Its default value is RAISED.
# image	                        This option is used to display an image on the menu
# postcommand	                This option can be set to any of the function which is called when the mouse hovers the menu.
# tearoff	                    The choices in the menu start from position 1 by default. But If we set the tearoff=1, then choices will start taking place from 0th position.
# selectcolor	                This option indicates the color used to display the checkbutton or radiobutton when they are selected.
# title	                        This option is set to the title of the window if you want to change the title of the window.

#Name of method	                        Description
# add_command()	                This method is used to add menu items to the menu.
# add_radiobutton()	            This method is used to add the radiobutton to the menu.
# add_checkbutton()	            This method is mainly used to add checkbuttons to the menu.
# add_cascade()	                This method is used to create a hierarchical menu to the parent menu by associating the given menu to the parent menu.
# add_seperator()	            This method is used to add the separator line to the menu items.
# add(type, options)	        This method is used to add the specific menu item to the menu.
# delete(startindex, endindex)	This method is used to delete the menu items that exist in the specified range.
# entryconfig(index, options)	This method is used to configure a menu item that is identified by the given index.
# index(item)	                This method is used to get the index of the specified menu item.
# insert_seperator(index)	    This method is used to insert a separator at the specified index.
# invoke(index)	                This method is used to invoke the associated operation with the choice given at the specified index.
# type(index)	                This method is used to get the type of choice specified by the index.


from tkinter import *

root = Tk()

def hello():
    print("hello!")

menubar = Menu(root)
menubar.add_command(label="Hello StudyTonight!", command=hello)
menubar.add_command(label="Quit!", command=root.quit)

root.config(menu=menubar)

root.mainloop()