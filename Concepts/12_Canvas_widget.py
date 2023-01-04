# w = Canvas(master, option=value)

# Option name	                Description
# bd	                This option is mainly used to set the width of the border in pixels.The default value of 0px means no border, 1px means thin line border and you can increase the width of the border.
# # bg	                This option is used to set the background color.
# cursor	            Whether to use an arrow, dot, or circle on the canvas for the cursor, this option can be used.
# confine	            This option is set to make the canvas non-scrollable outside the scroll region.
# height	            This option is used for controlling the height of the canvas.
# width	                This option is used to set the width of the widget.
# highlightcolor	    This option indicates the highlight color when there is a focus on the button
# xscrollcommand	    In the case, if the canvas is of scrollable type, then this attribute should act as the set() method of the horizontal scrollbar
# yscrollcommand	    In the case, if the canvas is of scrollable type, then this attribute should act as the set() method of the vertical scrollbar
# scrollregion	        This is option is mainly used to represent the coordinates that are specified as the tuple containing the area of the canvas
# xscrollincrement	    If the value of this option is set to a positive value then, the canvas is placed only to the multiple of this value.
# yscrollincrement	    It is mainly used for vertical movement and it works in the same way xscrollincrement option works.

import tkinter

# init tk
root = tkinter.Tk()

# creating canvas
mCanvas = tkinter.Canvas(root, bg="white", height=300, width=300)

# drawing two arcs
coord = 10, 10, 300, 300
arc1 = mCanvas.create_arc(coord, start=0, extent=150, fill="pink")
arc2 = mCanvas.create_arc(coord, start=150, extent=215, fill="blue")

# adding canvas to window and display it
mCanvas.pack()
root.mainloop()
