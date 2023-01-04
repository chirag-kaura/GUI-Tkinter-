# W = Frame(master, options)  

# Name of the option	                  Description
# bd	                    This option is used to represent the width of the border. Its default value is 2 pixels.
# bg	                    This option is used to indicate the normal background color of a widget.
# cursor                	With the help of this option, the mouse pointer can be changed to the cursor type which is set to different values like an arrow, dot, etc.
# height	                This option is used to indicate the height of the frame.
# width	                    This option is used to indicate the width of the frame.
# highlightbackground   	This option denotes the color of the background color when it is under focus.
# highlightthickness    	This option is used to specify the thickness around the border when the widget is under the focus.
# relief	                This option specifies the type of the border of the frame. Its default value is FLAT
# highlightcolor        	This option is mainly used to represent the color of the focus highlight when the frame has the focus.

from tkinter import *
 
root = Tk() 
root.geometry("300x150") 

w = Label(root, text ='StudyTonight', font = "80") 
w.pack() 

frame = Frame(root) 
frame.pack() 

bottomframe = Frame(root) 
bottomframe.pack(side = BOTTOM) 

button1 = Button(frame, text ="Block1", fg ="red") 
button1.pack(side = LEFT) 

button2 = Button(frame, text ="Block2", fg ="brown") 
button2.pack(side = LEFT) 

button3 = Button(frame, text ="Block3", fg ="blue") 
button3.pack(side = LEFT) 

button4 = Button(bottomframe, text ="Block4", fg ="orange") 
button4.pack(side = BOTTOM) 

button5 = Button(bottomframe, text ="Block5", fg ="orange") 
button5.pack(side = BOTTOM) 

button6 = Button(bottomframe, text ="Block6", fg ="orange") 
button6.pack(side = BOTTOM) 

root.mainloop()