# W = Label(master,options)   
# Name of the option	                Description
# 
# anchor	                    This option is mainly used for controlling the position of text in the provided widget size. The default value is CENTER which is used to align the text in center in the provided space.
# bd	                        This option is used for the border width of the widget. Its default value is 2 pixels.
# bitmap	                    This option is used to set the bitmap equals to the graphical object specified so that now the label can represent the graphics instead of text.
# bg	                        This option is used for the background color of the widget.
# cursor	                    This option is used to specify what type of cursor to show when the mouse is moved over the label. The default of this option is to use the standard cursor.
# fg	                        This option is used to specify the foreground color of the text that is written inside the widget.
# font	                        This option specifies the font type of text inside the label.
# height	                    This option indicates the height of the widget
# image	                        This option indicates the image that is shown as the label.
# justify	                    This option specifies the alignment of multiple lines in the label. The default value is CENTER. Other values are RIGHT, LEFT; you can justify according to your requirement
# padx	                        This option indicates the horizontal padding of the text. The default value of this option is 1.
# pady	                        This option indicates the vertical padding of the text. The default value of this option is 1.
# relief	                    This option indicates the type of border. The default value of this option is FLAT
# text	                        This option is set to the string variable and it may contain one or more than one line of text
# textvariable	                This option is associated with a Tkinter variable that is (StringVar) with a label. If you change the value of this variable then text inside the label gets updated.
# underline	                    This option is used to underline a specific part of the text. The default value of this option =-1(no underline); you can set it to any integer value up to n and counting starts from 0.
# width	                        This option indicates the width of the widget.
# wraplength	                Rather than having only one line as the label text, you can just break it to any number of lines where each line has the number of characters specified to this option.


from tkinter import *   
 
win = Tk()  
  
win.geometry("400x250")  
  
#creating a label  
username = Label(win, text = "Username").place(x = 30,y = 50)  
  
#creating second label  
password = Label(win, text = "Password").place(x = 30, y = 90)  
    
submitbutton = Button(win, text = "Submit",activebackground = "red", activeforeground = "blue").place(x = 30, y = 120)  
  
e1 = Entry(win,width = 20).place(x = 100, y = 50)  
    
e2 = Entry(win, width = 20).place(x = 100, y = 90)    
  
win.mainloop()  