# Pack() 
# widget.pack(options)  --> fill,side,expand

import tkinter as tk

win = tk.Tk()

frame1 = tk.Frame(master=win, width=200, height=100, bg="Yellow")
# setting fill, side and expand
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=win, width=100, bg="blue")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=win, width=50, bg="green")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

win.mainloop()


# grid() 
# widget.grid(options)  --> Column,Row,Columnspan,Rowspan,padx,pady,ipadx,ipady,Sticky

import tkinter as tk

win = tk.Tk()

for i in range(5):
    for j in range(3):
        frame = tk.Frame(
            master=win,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()

win.mainloop()

#place()    
# widget.place(options)     --> x, y,height,width,Anchor,bordermode,relx,rely,relheight,relwidth

from tkinter import *
top = Tk()  
top.geometry("400x250")  
Username = Label(top, text = "Username").place(x = 10,y = 50)  
email = Label(top, text = "Email").place(x = 10, y = 90)  
password = Label(top, text = "Password").place(x = 10, y = 130)  
e1 = Entry(top).place(x = 80, y = 50)  
e2 = Entry(top).place(x = 80, y = 90)  
e3 = Entry(top).place(x = 80, y = 130)  
top.mainloop()  
