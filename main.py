from tkinter import *
from tkinter import Toplevel
import time

#Functions
def tick():
    time_str=time.strftime("%H:%M:%S")
    date_str=time.strftime("%d/%m/%y")
    clock.config(text='Date: '+date_str+"\n"+"Time: "+time_str)
    clock.after(1,tick)
def intro():
    global count,text
    if(count>=len(ss)):
        count=0
        text=''
        sliderlabel.config(text=text)
    else:
        text=text+ss[count]
        sliderlabel.config(text=text)
        count+=1
    sliderlabel.after(200,intro)

def connectdb():
    dbroot=Toplevel()
    dbroot.grab_set()
    dbroot.title('Connect to Database')
    dbroot.geometry('470x250+800+230')
    dbroot.resizable(False,False)
    dbroot.config(bg='blue')
    #####Connect labels
    hostlabel=Label(dbroot,text="Enter Host: ",bg='Yellow',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    hostlabel.place(x=10,y=10)
    userlabel = Label(dbroot, text="Enter User: ", bg='Yellow', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    userlabel.place(x=10, y=60)
    passlabel = Label(dbroot, text="Enter Password: ", bg='Yellow', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    passlabel.place(x=10, y=110)
    ######Connect Entry
    hostval=StringVar()
    userval=StringVar()
    passval=StringVar()

    hostentry=Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)

    userentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=userval)
    userentry.place(x=250, y=60)

    passentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=passval)
    passentry.place(x=250, y=110)

    ######connect button
    submitbttn=Button(dbroot,text='Submit',font=('roman',15,'bold'),bg='red',bd=5,width=20,activebackground='Blue',activeforeground='white')
    submitbttn.place(x=150,y=190)

    dbroot.mainloop()




#Main application begin's
root=Tk()
root.geometry('1000x600+200+50')
root.title('Manage your Notes here')
root.config(bg='yellow')
root.resizable(False,False)

#Frames

dataentryframe=Frame(root,bg='white',relief=GROOVE,borderwidth=5)
dataentryframe.place(x=20,y=80,width=450,height=500)

showentryframe=Frame(root,bg='white',relief=GROOVE,borderwidth=5)
showentryframe.place(x=490,y=80,width=500,height=500)

#Slider

ss='Manage Your Notes'
count=0
text=''
sliderlabel=Label(root,text=ss,font=('chiller',30,'bold'),relief=GROOVE,borderwidth=4,bg='cyan')
sliderlabel.place(x=260,y=0)
intro()

#Clock

clock=Label(root,font=('times',15,'bold'),relief=RIDGE,borderwidth=4,bg='lawn green')
clock.place(x=0,y=0)
tick()

#Button
connectbutton=Button(root,text="Connect to Database",width=23,font=('times',15,'bold'),relief=RIDGE,borderwidth=4,bg='lawn green',activebackground='Blue',activeforeground='white',command=connectdb)
connectbutton.place(x=700,y=0)


root.mainloop()
