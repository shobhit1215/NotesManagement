from tkinter import *
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pandas
import pymysql

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
    def submitdb():
        global con,mycursor
        host=hostval.get()
        user=userval.get()
        password=passval.get()
        # host = 'localhost'
        # user = 'root'
        # password = 'shobhit'
        try:
            con=pymysql.connect(host=host,user=user,password=password)
            mycursor=con.cursor()
            print("Done")
        except:
            messagebox.showerror('Notification','Data is incorrect please try again')
            return
        try:
            str='create database recordmanagement'
            mycursor.execute(str)
            str='use recordmanagement'
            mycursor.execute(str)
            str='create table records(serial int,description varchar(100),detail1 varchar(200),detail2 varchar(200),detail3 varchar(200))'
            mycursor.execute(str)
            str = 'alter table records modify column serial int not null'
            mycursor.execute(str)
            str = 'alter table records modify column serial int primary key'
            mycursor.execute(str)
            messagebox.showinfo('Notification', 'Database created and now you are connected to the database ...', parent=dbroot)


        except:
            str='use recordmanagement'
            mycursor.execute(str)
            messagebox.showinfo('Notification','Now you are connected to the database ...',parent=dbroot)




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
    submitbttn=Button(dbroot,text='Submit',font=('roman',15,'bold'),bg='red',bd=5,width=20,activebackground='Blue',activeforeground='white',command=submitdb)
    submitbttn.place(x=150,y=190)

    dbroot.mainloop()


def addrecord():
    def submitadd():
        try:
            id=idval.get()
            name=nameval.get()
            disc1=disc1val.get()
            disc2=disc2val.get()
            disc3=disc3val.get()
            try:
                str='insert into records values(%s,%s,%s,%s,%s)'
                mycursor.execute(str,(id,name,disc1,disc2,disc3))
                con.commit()
            # print("Yes")
                value=messagebox.askyesno('Notification','Record has been entered .. Do you want to enter again ',parent=addroot)
                if(value==True):
                    idval.set('')
                    nameval.set('')
                    disc1val.set('')
                    disc2val.set('')
                    disc3val.set('')
            except:
                messagebox.showerror('Notifications','ID alreay exist..Try another ID ',parent=addroot)

            str ='select * from records'
            mycursor.execute(str)
            datas=mycursor.fetchall()
            datatable.delete(*datatable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4]]
                datatable.insert('',END,values=vv)
        except:
            messagebox.showinfo('Notification','Connect to database')

        # print(datas)


    addroot=Toplevel(master=dataentryframe)
    addroot.grab_set()
    addroot.geometry('470x370+220+200')
    addroot.title('Add Record')
    addroot.config(bg='blue')
    addroot.resizable(False,False)
    ##############################################add labels
    idlabel=Label(addroot,text="Enter Serial No : ",bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(addroot, text="Description: ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12, anchor='w')
    namelabel.place(x=10, y=70)

    desc1label = Label(addroot, text="Enter Detail1 : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12, anchor='w')
    desc1label.place(x=10, y=130)

    disc2label = Label(addroot, text="Enter Detail2 : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12, anchor='w')
    disc2label.place(x=10, y=190)

    disc3label = Label(addroot, text="Enter Detail3 : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12, anchor='w')
    disc3label.place(x=10, y=250)
    ###############################33add entry
    idval=StringVar()
    nameval = StringVar()
    disc1val = StringVar()
    disc2val = StringVar()
    disc3val = StringVar()
    identry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    disc1entry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=disc1val)
    disc1entry.place(x=250, y=130)

    disc2entry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=disc2val)
    disc2entry.place(x=250, y=190)

    disc3entry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=disc3val)
    disc3entry.place(x=250, y=250)

    submitbtn=Button(addroot,text="Submit",font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='red',command=submitadd)
    submitbtn.place(x=150,y=310)
    addroot.mainloop()


def searchrecord():
    def submitsearch():
        try:
            id = idval.get()
            name = nameval.get()
        # disc1 = disc1val.get()
        # disc2 = disc2val.get()
        # disc3 = disc3val.get()
            if(id!=''):
                str='select * from records where serial=%s'
                mycursor.execute(str,(id))
                datas=mycursor.fetchall()
                datatable.delete(*datatable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4]]
                    datatable.insert('', END, values=vv)

            if (name != ''):
                str = 'select * from records where description=%s'
                mycursor.execute(str, (name))
                datas = mycursor.fetchall()
                datatable.delete(*datatable.get_children())
                for i in datas:
                    vv = [i[0], i[1], i[2], i[3], i[4]]
                    datatable.insert('', END, values=vv)
        except:
            messagebox.showinfo('Notification','Please connect to database or enter correct details')

        # if (disc1 != ''):
        #     str = 'select * from records where detail1=%s'
        #     mycursor.execute(str, (disc1))
        #     datas = mycursor.fetchall()
        #     datatable.delete(*datatable.get_children())
        #     for i in datas:
        #         vv = [i[0], i[1], i[2], i[3], i[4]]
        #         datatable.insert('', END, values=vv)
        #
        # if (disc2 != ''):
        #     str = 'select * from records where detail2=%s'
        #     mycursor.execute(str, (disc2))
        #     datas = mycursor.fetchall()
        #     datatable.delete(*datatable.get_children())
        #     for i in datas:
        #         vv = [i[0], i[1], i[2], i[3], i[4]]
        #         datatable.insert('', END, values=vv)
        #
        # if (disc3 != ''):
        #     str = 'select * from records where detail3=%s'
        #     mycursor.execute(str, (disc3))
        #     datas = mycursor.fetchall()
        #     datatable.delete(*datatable.get_children())
        #     for i in datas:
        #         vv = [i[0], i[1], i[2], i[3], i[4]]
        #         datatable.insert('', END, values=vv)


        # print("Searched")
    searchroot = Toplevel(master=dataentryframe)
    searchroot.grab_set()
    searchroot.geometry('470x370+220+200')
    searchroot.title('Search Record...On the basis of any of the two fields')
    searchroot.config(bg='blue')
    searchroot.resizable(False, False)
    ##############################################add labels
    idlabel = Label(searchroot, text="Enter Serial No : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                    borderwidth=3, width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(searchroot, text="Description: ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    namelabel.place(x=10, y=70)

    # desc1label = Label(searchroot, text="Enter Detail1 : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
    #                    borderwidth=3, width=12, anchor='w')
    # desc1label.place(x=10, y=130)
    #
    # disc2label = Label(searchroot, text="Enter Detail2 : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
    #                    borderwidth=3, width=12, anchor='w')
    # disc2label.place(x=10, y=190)
    #
    # disc3label = Label(searchroot, text="Enter Detail3 : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
    #                    borderwidth=3, width=12, anchor='w')
    # disc3label.place(x=10, y=250)
    ###############################33add entry
    idval = StringVar()
    nameval = StringVar()
    # disc1val = StringVar()
    # disc2val = StringVar()
    # disc3val = StringVar()
    identry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    # disc1entry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=disc1val)
    # disc1entry.place(x=250, y=130)
    #
    # disc2entry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=disc2val)
    # disc2entry.place(x=250, y=190)
    #
    # disc3entry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=disc3val)
    # disc3entry.place(x=250, y=250)

    submitbtn = Button(searchroot, text="Submit", font=('roman', 15, 'bold'), width=20, bd=5, activebackground='blue',
                       activeforeground='white', bg='red', command=submitsearch)
    submitbtn.place(x=150, y=310)

    searchroot.mainloop()

def deleterecord():
    try:
        cc = datatable.focus()
        content = datatable.item(cc)
        # print(content)
        pp = content['values'][0]
        str = 'delete from records where serial=%s'
        mycursor.execute(str,(pp))
        con.commit()
        messagebox.showinfo('Notifications','Record with Serial No. {} deleted successfully..'.format(pp))
        str = 'select * from records'
        mycursor.execute(str)
        datas = mycursor.fetchall()
        datatable.delete(*datatable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4]]
            datatable.insert('', END, values=vv)
    except:
        messagebox.showinfo('Notification','Please connect to a databse and select a record')

    # print('delete record')


def updaterecord():

    def submitupdate():
        id = idval.get()
        name = nameval.get()
        disc1 = disc1val.get()
        disc2 = disc2val.get()
        disc3 = disc3val.get()
        str='update records set description=%s,detail1=%s,detail2=%s,detail3=%s where serial=%s'
        mycursor.execute(str,(name,disc1,disc2,disc3,id))
        con.commit()
        messagebox.showinfo('Notification','Record with serial No {} updated successfully'.format(id),parent=updateroot)
        str = 'select * from records'
        mycursor.execute(str)
        datas = mycursor.fetchall()
        datatable.delete(*datatable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4]]
            datatable.insert('', END, values=vv)


    # updateroot = Toplevel(master=dataentryframe)
    # updateroot.grab_set()
    # updateroot.geometry('470x370+220+200')
    # updateroot.title('Add Record')
    # updateroot.config(bg='blue')
    # updateroot.resizable(False, False)
    # ##############################################add labels
    # idlabel = Label(updateroot, text="Enter Serial No : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
    #                 borderwidth=3, width=12, anchor='w')
    # idlabel.place(x=10, y=10)
    #
    # namelabel = Label(updateroot, text="Description: ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
    #                   borderwidth=3, width=12, anchor='w')
    # namelabel.place(x=10, y=70)
    #
    # desc1label = Label(updateroot, text="Enter Detail1 : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
    #                    borderwidth=3, width=12, anchor='w')
    # desc1label.place(x=10, y=130)
    #
    # disc2label = Label(updateroot, text="Enter Detail2 : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
    #                    borderwidth=3, width=12, anchor='w')
    # disc2label.place(x=10, y=190)
    #
    # disc3label = Label(updateroot, text="Enter Detail3 : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
    #                    borderwidth=3, width=12, anchor='w')
    # disc3label.place(x=10, y=250)
    # ###############################33add entry
    # idval = StringVar()
    # nameval = StringVar()
    # disc1val = StringVar()
    # disc2val = StringVar()
    # disc3val = StringVar()
    # identry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=idval)
    # identry.place(x=250, y=10)
    #
    # nameentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    # nameentry.place(x=250, y=70)
    #
    # disc1entry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=disc1val)
    # disc1entry.place(x=250, y=130)
    #
    # disc2entry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=disc2val)
    # disc2entry.place(x=250, y=190)
    #
    # disc3entry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=disc3val)
    # disc3entry.place(x=250, y=250)
    #
    # submitbtn = Button(updateroot, text="Submit", font=('roman', 15, 'bold'), width=20, bd=5, activebackground='blue',
    #                    activeforeground='white', bg='red', command=submitupdate)
    # submitbtn.place(x=150, y=310)
    cc=datatable.focus()
    content=datatable.item(cc)
    pp=content['values']
    if(len(pp)!=0):
        updateroot = Toplevel(master=dataentryframe)
        updateroot.grab_set()
        updateroot.geometry('470x370+220+200')
        updateroot.title('Add Record')
        updateroot.config(bg='blue')
        updateroot.resizable(False, False)
        ##############################################add labels
        idlabel = Label(updateroot, text="Enter Serial No : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
        idlabel.place(x=10, y=10)

        namelabel = Label(updateroot, text="Description: ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                          borderwidth=3, width=12, anchor='w')
        namelabel.place(x=10, y=70)

        desc1label = Label(updateroot, text="Enter Detail1 : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                           borderwidth=3, width=12, anchor='w')
        desc1label.place(x=10, y=130)

        disc2label = Label(updateroot, text="Enter Detail2 : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                           borderwidth=3, width=12, anchor='w')
        disc2label.place(x=10, y=190)

        disc3label = Label(updateroot, text="Enter Detail3 : ", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                           borderwidth=3, width=12, anchor='w')
        disc3label.place(x=10, y=250)
        ###############################33add entry
        idval = StringVar()
        nameval = StringVar()
        disc1val = StringVar()
        disc2val = StringVar()
        disc3val = StringVar()
        identry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=idval)
        identry.place(x=250, y=10)

        nameentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
        nameentry.place(x=250, y=70)

        disc1entry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=disc1val)
        disc1entry.place(x=250, y=130)

        disc2entry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=disc2val)
        disc2entry.place(x=250, y=190)

        disc3entry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=disc3val)
        disc3entry.place(x=250, y=250)

        submitbtn = Button(updateroot, text="Submit", font=('roman', 15, 'bold'), width=20, bd=5,
                           activebackground='blue',
                           activeforeground='white', bg='red', command=submitupdate)
        submitbtn.place(x=150, y=310)
        idval.set(pp[0])
        nameval.set(pp[1])
        disc1val.set(pp[2])
        disc2val.set(pp[3])
        disc3val.set(pp[4])
        updateroot.mainloop()
    else:
        messagebox.showinfo('Notification','Please connect to a databse and select a record')

    # updateroot.mainloop()

def showrecord():
    try:
        str = 'select * from records'
        mycursor.execute(str)
        datas = mycursor.fetchall()
        datatable.delete(*datatable.get_children())
        for i in datas:
           vv = [i[0], i[1], i[2], i[3], i[4]]
           datatable.insert('', END, values=vv)
    except:
        messagebox.showinfo('Notification','Please connect to database first')

def exportrecord():
    try:
        ff=filedialog.asksaveasfilename()
        gg=datatable.get_children()
        id,name,disc1,disc2,disc3=[],[],[],[],[]
        for i in gg:
            content=datatable.item(i)
            pp=content['values']
            id.append(pp[0]),name.append(pp[1]),disc1.append(pp[2]),disc2.append(pp[3]),disc3.append(pp[4])
        dd=['Serial','Description','Detail1','Detail2','Detail3']
        df=pandas.DataFrame(list(zip(id,name,disc1,disc2,disc3)),columns=dd)
        paths=r'{}.csv'.format(ff)
        df.to_csv(paths,index=False)
        messagebox.showinfo('Notification','Student data is saved {}'.format(paths))
    except:
        messagebox.showinfo('Notification','Connect to database and have some records in Datatable')



def exitrecord():
    res=messagebox.askyesnocancel('Notification','Do you want to exit? ')
    print(res)
    if(res==True):
        root.destroy()

#Main application begin's
root=Tk()
root.geometry('1000x700+200+50')
root.title('Manage your Notes here')
root.config(bg='yellow')
root.resizable(False,False)
root.wm_iconbitmap('notes_management.ico')

######################################Frames
#Data Entry Frames Label
dataentryframe=Frame(root,bg='white',relief=GROOVE,borderwidth=5)
dataentryframe.place(x=20,y=80,width=450,height=600)

frontlabel=Label(dataentryframe,text='.........Welcome............',width=23,font=('arial',22,'bold'),bg='gold2')
frontlabel.pack(side=TOP,expand=True)
addbtn=Button(dataentryframe,text='1. Add Record',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activeforeground='white',relief=RIDGE,activebackground='blue',command=addrecord)
addbtn.pack(side=TOP,expand=True)

searchbtn=Button(dataentryframe,text='2. Search Record',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activeforeground='white',relief=RIDGE,activebackground='blue',command=searchrecord)
searchbtn.pack(side=TOP,expand=True)

deletebtn=Button(dataentryframe,text='3.Delete Record',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activeforeground='white',relief=RIDGE,activebackground='blue',command=deleterecord)
deletebtn.pack(side=TOP,expand=True)

updatebtn=Button(dataentryframe,text='4. Update Record',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activeforeground='white',relief=RIDGE,activebackground='blue',command=updaterecord)
updatebtn.pack(side=TOP,expand=True)

showallbtn=Button(dataentryframe,text='5. Show All Record',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activeforeground='white',relief=RIDGE,activebackground='blue',command=showrecord)
showallbtn.pack(side=TOP,expand=True)

exportbtn=Button(dataentryframe,text='6. Export Data',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activeforeground='white',relief=RIDGE,activebackground='blue',command=exportrecord)
exportbtn.pack(side=TOP,expand=True)

exitbtn=Button(dataentryframe,text='7. Exit',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activeforeground='white',relief=RIDGE,activebackground='blue',command=exitrecord)
exitbtn.pack(side=TOP,expand=True)

showentryframe=Frame(root,bg='white',relief=GROOVE,borderwidth=5)
showentryframe.place(x=490,y=80,width=500,height=600)

####################3333.... Show data frame
style=ttk.Style()
style.configure('Treeview.Heading',font=('chiller',20,'bold'),foregroung='blue')
style.configure('Treeview',font=('times',15,'bold'),foreground='black',background='cyan')
scroll_x=Scrollbar(showentryframe,orient=HORIZONTAL)
scroll_y=Scrollbar(showentryframe,orient=VERTICAL)

datatable=Treeview(showentryframe,columns=('Serial No.','Description','Detail 1','Detail 2','Detail 3'),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=datatable.xview)
scroll_y.config(command=datatable.yview)
datatable.heading('Serial No.',text='Serial No.')
datatable.heading('Description',text='Description')
datatable.heading('Detail 1',text='Detail 1')
datatable.heading('Detail 2',text='Detail 2')
datatable.heading('Detail 3',text='Detail 3')
datatable['show']='headings'
datatable.column('Serial No.',width=150)
datatable.column('Description',width=200)
datatable.column('Detail 1',width=300)
datatable.column('Detail 2',width=300)
datatable.column('Detail 3',width=300)
datatable.pack(fill=BOTH,expand=1)

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
