# W = PanedWindow(master, options) 

# Name of the Option	                  Description
# bd	                    This option is used to represent the 3D border size of the widget. The default value of this option indicates that the trough contains no border and the arrowheads and slider contain the 2-pixel border size.
# bg	                    This option represents the background color of the widget.
# cursor                	This option will convert the mouse pointer to the specified cursor type and it can be set to an arrow, dot, etc.
# borderwidth	            This option is used to indicate the border width of the widget. The default value of this option is 2 pixels.
# handlepad	                To represents the distance between the handle and the end of the sash we use this option. In horizontal orientation, it is the distance between the top of the sash and the handle. The default value of this option is 8 pixels
# height	                This option represents the height of the widget. If we do not specify the height then the height will be calculated by the height of the child widgets.
# handlesize	            This option represents the size of the handle and its default value is 8 pixels. Also, the handle will always be in square
# orient	                The value of this option will be set to HORIZONTAL if we want to place the child windows side by side. If we want to place the child windows from top to bottom then the value of this option will be set to VERTICAL.
# sashpad	                This option is used to represent the padding to be done around each sash. The default value of this option is 0.
# sashwidth	                This option indicates the width of the sash. The default value of this option is 2 pixels.
# sashrelief	            This option is used to represent the type of border around each of the sash. The default value of this option is FLAT
# showhandle	            To display the handles, the value of this option should be set to true. The default value of this option is false.
# width	                    This option represents the width of the widget. If we do not specify the height then the height will be calculated by the height of the child widgets.
# relief	                This option indicates the type of border. The default value of this option is FLAT.


# Method Name	                        Description
# config(options)	        This method is mainly used to configure any widget with some specified options.
# get(startindex,endindex)	This method is used to get the text at the specified given range.
# add(child,options)	    This method is used to add a window to a parent window.

from tkinter import * 

win = Tk() 

pw = PanedWindow(orient ='vertical') 
#creating Button widget 
top = Button(pw, text ="Just Click Me!!!\nI am a Button") 
top.pack(side=TOP) 

#Adding button widget to the panedwindow 
pw.add(top) 

#Creating Checkbutton Widget 
bot = Checkbutton(pw, text="I am Checkbutton Choose Me!") 
bot.pack(side=TOP) 
pw.add(bot) 

label = Label(pw, text="I am a Label") 
label.pack(side=TOP) 

pw.add(label) 

string = StringVar() 

entry = Entry(pw, textvariable=string, font=('arial', 15, 'bold')) 
entry.pack() 

# This is used to force focus on particular widget 
# that means widget is already selected for some operations 
entry.focus_force() 

pw.add(entry) 
pw.pack(fill = BOTH, expand = True) 

# To show sash 
pw.configure(sashrelief = RAISED) 

mainloop() 