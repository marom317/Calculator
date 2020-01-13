from tkinter import *

root = Tk()
root.title("My Calculator")

entry = Entry(root, width=60, borderwidth= 5)
entry.grid(row=1, column=1, columnspan=4 , padx=10,)

def button_click(num):
    last_num = entry.get()
    entry.delete(0,END)
    entry.insert(0,str(last_num)+str(num))

def clear():
    entry.delete(0, END)

def divide():
    first_num = entry.get()
    global f_num
    global operation
    f_num = int(first_num)
    operation = "divide"
    entry.delete(0, END)

def plus():
    first_num = entry.get()
    global f_num
    global operation
    f_num = int(first_num)
    operation = "plus"
    entry.delete(0, END)
def minus():
    first_num = entry.get()
    global f_num
    global operation
    f_num = int(first_num)
    operation = "minus"
    entry.delete(0, END)
def multy():
    first_num = entry.get()
    global f_num
    global operation
    f_num = int(first_num)
    operation = "multy"
    entry.delete(0, END)
def equl():
    s_num = entry.get()
    entry.delete(0,END)
    if operation == "plus":
        entry.insert(0, f_num + int(s_num))
    if operation == "minus":
        entry.insert(0, f_num - int(s_num))
    if operation == "multy":
        entry.insert(0, f_num * int(s_num))
    if operation == "divide":
        entry.insert(0, f_num / int(s_num))

# Make buttons
button_1 = Button(root, text="1", padx=40, pady=20, command= lambda: button_click(1) )
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2) )
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3) )
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4) )
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5) )
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6) )
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7) )
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8) )
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9) )
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0) )

button_multy = Button(root, text="*", padx=40, pady=20, command=multy )
button_divade = Button(root, text="/", padx=40, pady=20, command=divide )
button_plus = Button(root, text="+", padx=40, pady=20, command=plus )
button_minus = Button(root, text="-", padx=40, pady=20, command=minus )

button_equl = Button(root, text="=", padx=40, pady=20, command=equl )
button_clear = Button(root,width=5, text="CLEAR", padx=26, pady=20, command=clear, )

# Place the buttons

button_1.grid(row=4,column=1)
button_2.grid(row=4,column=2)
button_3.grid(row=4,column=3)

button_4.grid(row=3,column=1)
button_5.grid(row=3,column=2)
button_6.grid(row=3,column=3)

button_7.grid(row=2,column=1)
button_8.grid(row=2,column=2)
button_9.grid(row=2,column=3)

button_multy.grid(row=2,column=4)
button_divade.grid(row=3,column=4)
button_plus.grid(row=5,column=4)
button_minus.grid(row=4,column=4)

button_equl.grid(row=5,column=3)
button_clear.grid(row=5,column=2)

root.mainloop()