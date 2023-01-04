# w = LabelFrame(master, option=value)

# Name of the Option	                Description
# height	                    This option is used to represent the height of the widget.
# width	                        This option is used to represent the width of the frame.
# text	                        This option represents the string containing the text of the Label.
# relief	                    This option represents the style of the border.The default value of this option is GROOVE
# padx	                        This option represents the horizontal padding of the widget
# pady	                        This option represents the vertical padding of the widget
# font	                        This option represents the font type of the text of the widget
# highlighthickness	            This option represents the width of the focus highlight border
# highlightbackground       	This option indicates the color of the focus highlight border at the time when the widget doesn't have the focus
# highlightcolor	            This option indicates the color of the focus highlight when the widget is under the focus
# bg	                        This option indicates the background color of the widget
# bd	                        This option is used to represent the size of the border around the indicator.The default value of this option is 2 pixels.
# Class	                        The default value of this option is LabelFrame.
# colormap	                    This option is mainly used to specify which colomap to be used for this widget.With the help of this option, we can reuse the colormap of another window on this widget.The colormap means 256 colors that are used to form the graphics
# container	                    The LabelFrame becomes the container widget if we will set the value of this option to true.The default value of this option is false
# cursor	                    This option will convert the mouse pointer to the specified cursor type and it can be set to an arrow, dot, etc
# fg	                        This option is used to indicate the foreground color of the widget
# labelAnchor                  	This option represents the exact position of the text inside the widget. The default value of this option is NW(north-west)
# labelwidget	                This option indicates the widget to be used for the label. Also,the frame uses the text for the label if no value specified

from tkinter import *  
  
win = Tk()  
win.geometry("300x200")  
  
labelframe1 = LabelFrame(win, text="Happy Thoughts!!!")  
labelframe1.pack(fill="both", expand="yes")  
  
toplabel = Label(labelframe1, text="You can put your happy thoughts here")  
toplabel.pack()  
  
labelframe2 = LabelFrame(win, text = "Changes You want!!")  
labelframe2.pack(fill="both", expand = "yes")  
  
bottomlabel = Label(labelframe2, text = "You can put here the changes you want,If any!")  
bottomlabel.pack()  
  
win.mainloop()  