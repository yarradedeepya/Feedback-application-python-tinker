from tkinter import *
import pymysql
#from chatterbot.trainers import ListTrainer
from tkinter.scrolledtext import ScrolledText
import tkinter.messagebox
conn = pymysql.connect(host="localhost",user="root",password="",db="jntuk_ucen" )
mycursor = conn.cursor()
def helloc():
    if(entry40.get()==entry54.get()):
        mycursor.execute("INSERT INTO passwor (passwords) values(%s)",entry40.get())
        conn.commit()
        tkinter.messagebox.showinfo("submit message", "succes")
        
    else:
        popupmsg1("password not matched")
        
        
        
def add():
        if entry1.get()=="":
            popupmsg1("error")
            return 0
        pk=[]
        mycursor.execute("select subjects from subject")
        ds=mycursor.fetchall()
        for i in ds:
            for j in i:
                pk.append(j)
        if entry1.get() in pk:
            popupmsg1("already subject exists")
        else:
            mycursor.execute("insert into subject (subjects,branch,year,sem) values(%s,%s,%s,%s)",(entry1.get(),tkvar1.get(),tkvar2.get(),tkvar3.get()))
            conn.commit()
            popupmsg1("sucess")
def dele():
            print(tkvar50.get())
            mycursor.execute("delete from subject where subjects='{}'".format(tkvar50.get()))
            conn.commit()
            popupmsg1("sucess")

def setpass():
        global root4
        root4=Tk()
        root4.geometry('500x300')
        root4.title("feedback")
        #root3.config(bg="black")
        label1900 = Label (root4,text="enter new password:",justify=LEFT,font=("courier","10","bold"))
        label1900.grid(row=0,column=0,sticky =W)
        label1901 = Label (root4,text="confirm password:",justify=LEFT,font=("courier","10","bold"))
        label1901.grid(row=1,column=0,sticky =W)
        global entry54
        global entry40
        entry54 = Entry(root4,show="*",font=("courier","12","bold"))
        entry54.grid(row=0,column=1)
        entry40 = Entry(root4,show="*",font=("courier","12","bold"))
        entry40.grid(row=1,column=1)
        print(entry40.get())
        print(entry54.get())
        MyButton03 = Button(root4, text="submit", width=10,command=helloc)
        MyButton03.grid(row=0,column=2,sticky=E)
       
def work():
        global password
        password = entry.get()
        global pd
        pd = StringVar(root1)
        global count1
        global passw
        global count1
        mycursor.execute("select count(id) from passwor")
        count=mycursor.fetchall()
        #print(count)
        for i in count:
            for j  in i:
                count1=j+24
        #print(count1)
        mycursor.execute("select passwords from passwor where id='{}'".format(count1))
        conn.commit()
        passw =mycursor.fetchall()
       # print(passw)
        for i in passw:
            for j  in i:
                pd=j
       
        #print(pd)
        if(password=='dd54' or password==pd):
            global tkvar1
            global tkvar2
            global tkvar3
            label2 = Label (root1,text="\nBRANCH :",justify=LEFT,font=("courier","10","bold"))
            label2.grid(row=1,column=0,sticky = E)
            tkvar1 = StringVar(root1)

            choices = [ 'CSE','ECE','EEE','MECH','CIVIL' ]
            popupMenu = OptionMenu(root1, tkvar1, *choices)
            popupMenu.grid(row =1 , column =1,sticky=S)
            tkvar1.set('CSE')
            label2 = Label (root1,text="YEAR  : ",justify=LEFT,font=("courier","10","bold"))
            label2.grid(row=2,column=0,sticky = E)
            tkvar2 = StringVar(root1)
            choices = [ 'I','II','III','IV']
            popupMenu = OptionMenu(root1, tkvar2, *choices)
            popupMenu.grid(row = 2, column =1)
            tkvar2.set('IV')
            label2 = Label (root1,text="SEM : ",justify=LEFT,font=("courier","10","bold"))
            label2.grid(row=3,column=0,sticky = E)
            tkvar3 = StringVar(root1)
            choices = ['I','II']
            popupMenu = OptionMenu(root1, tkvar3, *choices)
            popupMenu.grid(row = 3, column =1)
            tkvar3.set('I')
            label191 = Label (root1,text="enter subject:",justify=LEFT,font=("courier","10","bold"))
            label191.grid(row=4,column=0,sticky =W)
            global entry1
            entry1 = Entry(root1)
            entry1.grid(row=4,column=1)
            global tkvar50
            tkvar50 = StringVar(root1)
            choices=[]
            mycursor.execute("select subjects from subject")
            fs=mycursor.fetchall()
            for row in fs:
                    for m in row:
                       choices.append(m)
            conn.commit()
            popupMenu = OptionMenu(root1, tkvar50, *choices)                                                                                                                                                                                                                                                                                            
            popupMenu.grid(row =4 , column =2,sticky=E)
            print(tkvar50.get())
            MyButton01 = Button(root1, text="ADD subject", width=10,command=add)
            MyButton01.grid(row=5,column=0,sticky=E)
            
            MyButton02 = Button(root1, text="delete subject", width=10,command=dele)
            MyButton02.grid(row=5,column=3,sticky=E)
            MyButton02 = Button(root1, text="reset password", width=13,command=setpass)
            MyButton02.grid(row=6,column=0,sticky=SE)
            label171 = Label (root1,text="*NOTE:",justify=LEFT,font=("courier","11","bold"))
            label171.grid(row=7,column=0,sticky =W)
            label191 = Label (root1,text="subject entry should not allow\nwhitespace or symbols\nsubjectformate- subjectname_branchname ",justify=LEFT,font=("courier","10","bold"))
            label191.grid(row=7,column=1,sticky =W)

        else:
             popupmsg1("wrong password")
def helloa():
        popupmsg1("project details : \ndeveloper : Y.DEDEEPYA\ncollege : JTNUK-UCEN\nbranch : CSE 3rd YEAR ")
def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=1300,height=600)


def destroy2():
    popup1.destroy()
def popupmsg1(msg):
    global popup1
    popup1=Tk()
    popup1.wm_title("$")
    #popup1.config(bg="white")
    label90=Label(popup1,text=msg,font=("open sans","9","bold italic"))
    label90.grid(row=0,column=0)
    b1=Button(popup1,text="okay",command=destroy2)
    b1.grid(row=1,column=0)


    
root1=Tk()
root1.geometry('10000x700000')

root1.title("feedbackform")
menubar = Menu(root1)
menubar.add_command(label="about", command=helloa)
root1.config(menu=menubar)
label190 = Label (root1,text="enter password:",justify=LEFT,font=("courier","10","bold"))
label190.grid(row=0,column=0,sticky =W)
entry = Entry(root1,show="*",font=("courier","12","bold"))
entry.grid(row=0,column=1)
MyButton03 = Button(root1, text="submit", width=10,command=work)
MyButton03.grid(row=0,column=2,sticky=E)
root1.mainloop()
