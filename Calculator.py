#importing libraries
import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

#Creating window using GUI
window=tk.Tk()
window.title("Calculator")

#Geometry for window
frame=tk.Frame(master=window, bg='lightgreen' , padx=30)
frame.pack()
entry= tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=3, ipady=3, pady=5)

#Defining function for entering numbers
def myclick(number):
    entry.insert(tk.END, number)

#Defining function for EQUAL
def equal():
    try:
        y= str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error!", "Syntax Error!") 

#Defining function for CLEAR
def clear():
    entry.delete(0, tk.END)

#Creating BUTTONS......

button1=tk.Button(master=frame, text='1', padx=15, pady=5, width=3, command=lambda:myclick(1))
button1.grid(row=3, column=0, pady=3)

button2=tk.Button(master=frame, text='2', padx=15, pady=5, width=3, command=lambda:myclick(2))
button2.grid(row=3, column=1, pady=3)

button3=tk.Button(master=frame, text='3', padx=15, pady=5, width=3, command=lambda:myclick(3))
button3.grid(row=3, column=2, pady=3)

button4=tk.Button(master=frame, text='4', padx=15, pady=5, width=3, command=lambda:myclick(4))
button4.grid(row=2, column=0, pady=3)

button5=tk.Button(master=frame, text='5', padx=15, pady=5, width=3, command=lambda:myclick(5))
button5.grid(row=2, column=1, pady=3)

button6=tk.Button(master=frame, text='6', padx=15, pady=5, width=3, command=lambda:myclick(6))
button6.grid(row=2, column=2, pady=3)

button7=tk.Button(master=frame, text='7', padx=15, pady=5, width=3, command=lambda:myclick(7))
button7.grid(row=1, column=0, pady=3)

button8=tk.Button(master=frame, text='8', padx=15, pady=5, width=3, command=lambda:myclick(8))
button8.grid(row=1, column=1, pady=3)

button9=tk.Button(master=frame, text='9', padx=15, pady=5, width=3, command=lambda:myclick(9))
button9.grid(row=1, column=2, pady=3)

button0=tk.Button(master=frame, text='0', padx=15, pady=5, width=3, command=lambda:myclick(0))
button0.grid(row=4,  column=0, pady=3)

button_add=tk.Button(master=frame, text='+', padx=15, pady=5, width=3, command=lambda:myclick('+'))
button_add.grid(row=4, column=2, pady=3)

button_sub=tk.Button(master=frame, text='-', padx=15, pady=5, width=3, command=lambda:myclick('-'))
button_sub.grid(row=3, column=3, pady=3)

button_mul=tk.Button(master=frame, text='*', padx=15, pady=5, width=3, command=lambda:myclick('*'))
button_mul.grid(row=2, column=3, pady=3)

button_div=tk.Button(master=frame, text='/', padx=15, pady=5, width=3, command=lambda:myclick('/'))
button_div.grid(row=1, column=3, pady=3)

button_equal=tk.Button(master=frame, text='=', padx=15, pady=5, width=3, command=equal)
button_equal.grid(row=4, column=3, pady=3)

button_clear=tk.Button(master=frame, text='clear', padx=15, pady=5, width=3, command=clear)
button_clear.grid(row=4, column=1, pady=3)

#Finally calling window------
window.mainloop()