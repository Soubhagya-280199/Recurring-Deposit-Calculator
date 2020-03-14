from tkinter import *


root =Tk()

root.title("WELCOME TO AXIS BANK ")

# CREATING THE CANVAS PLATFORM
canvas1 = Canvas(root,width=400,height = 300)
canvas1.pack()


lable1=Label(root,text="Enter Your Principal Amount ",font=("Arial black",14,"bold"),fg="blue")
canvas1.create_window(30,140,window=lable1)

## CREATING THE ENTRY WIDGETS
entry1=Entry(root)
canvas1.create_window(250,140,window=entry1)

lable2=Label(root,text="Enter Your Months",font=("Arial black",14,"bold"),fg="blue")
canvas1.create_window(30,170,window=lable2)

# CREATING THE ENTRY WIDGETS
entry2=Entry(root)
canvas1.create_window(250,170,window=entry2)


def getamount():
    p=float(entry1.get())
    m=float(entry2.get())
    r=0

    # INTEREST TERMS OF PERIOD #

    if m > 12:
        r=float(5.80)
    else:
        r=float(5.80)


    SI = p * (m * (m + 1)) / 24 * (r / 100)
    mat = round((p * m) + SI)




    lable2=Label(root,text=float((mat)),font=("Arial black",24),fg="red")
    canvas1.create_window(300,230,window=lable2)


submit1=Button(text="Get the amount",font=("Arial black",12,"bold"),fg="Green",command=getamount)
canvas1.create_window(100,230,window=submit1)

def quitpage():
    quit()


exit1=Button(text="Exit",font=("Arial black",20,"bold"),fg="Red",command=quitpage)
canvas1.create_window(200,300,window=exit1)




root.mainloop()

