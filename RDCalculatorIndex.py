from tkinter import *
import os
import sys
from tkinter import messagebox

root = Tk()
root.title("RD CALCULATOR")




label1 = Label(root,text="! WELCOME TO RD CALCULATOR !",font=("Arial Black",32,"bold"),fg="white",bg="black").pack()

label1 = Label(root,text="--------HEY USER PLEASE CLICK ON YOUR BANK ---------",font=("Arial Black",18,"bold"),fg="white",bg="black").pack()
label2 = Label(root,text="--------USER IF YOUR BANKING ACCOUNTS BELONGS TO THESE BANKS PLEASE PROCEED---------",font=("Arial Black",12,"bold"),fg="red",bg="white").pack()
# SBI FUNCTION HERE
def sbihere():
    os.system('python SBI.py')

# HDFC FUNCTION HERE
def hdfchere():
    os.system('python HDFC.py')

# YES BANK FUNCTION HERE
def yesbankhere():
    os.system('python YES.py')

# AXIS FUNCTION HERE
def axisbankhere():
    os.system('python AXIS.py')

# ICICI FUNCTION HERE
def icicihere():
    os.system('python ICICI.py')

# HSBC FUNCTION HERE
def hsbchere():
    os.system('python HSBC.py')






#CREATING SBI BUTTON
sbibutton = Button(root,text="SBI",width=10,font=("Arial Black",12,"bold"),fg="green",bg="white",command=sbihere).place(x=100,y=200)

#CREATING HDFC BUTTON
hdfcbutton = Button(root,text="HDFC",width=10,font=("Arial Black",12,"bold"),fg="green",bg="white",command=hdfchere).place(x=500,y=200)

#CREATING YES BUTTON
yesbankbutton = Button(root,text="YES BANK",width=10,font=("Arial Black",12,"bold"),fg="green",bg="white",command=yesbankhere).place(x=1000,y=200)

#CREATING AXIS BUTTON
axisbutton = Button(root,text="AXIS BANK",width=10,font=("Arial Black",12,"bold"),fg="green",bg="white",command=axisbankhere).place(x=100,y=300)

#CREATING ICICI BUTTON
icicibutton = Button(root,text="ICICI",width=10,font=("Arial Black",12,"bold"),fg="green",bg="white",command=icicihere).place(x=500,y=300)

#CREATING HSBC BUTTON
hsbcbutton = Button(root,text="HSBC",width=10,font=("Arial Black",12,"bold"),fg="green",bg="white",command=hsbchere).place(x=1000,y=300)


# CREATING MESSAGE BOX

def notfound():
    root.geometry("100x100")
    messagebox.showerror("ERROR", "SORRY YOUR BANK CAN'T BE FOUND HERE !")

notfoundbutton = Button(root,text="NOTFOUND",width=10,font=("Arial Black",12,"bold"),fg="green",bg="white",command=notfound).place(x=500,y=400)




root.mainloop()
