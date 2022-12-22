from tkinter import *
import pymysql
#from chatterbot.trainers import ListTrainer
from tkinter.scrolledtext import ScrolledText
import tkinter.messagebox
conn = pymysql.connect(host="localhost",user="root",password="",db="jntuk_ucen" )
mycursor = conn.cursor()

def data():
    #inner window
    def myfunction(event):
        canvas.configure(scrollregion=canvas.bbox("all"),width=1330,height=640,bg="white")
    
    global root
    root=Tk()
    root.geometry('10000x690')
    myframe1=Frame(root,relief=GROOVE,width=50,height=50,bd=1)
    myframe1.place(x=10,y=10)
    root.title("feedback")
    menubar = Menu(root)
    menubar.add_command(label="about", command=helloa)
    root.config(menu=menubar)
    canvas=Canvas(myframe1,bg="white")
    frame=Frame(canvas,bg="white")
    myscrollbar1=Scrollbar(myframe1,orient="vertical",command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar1.set)
    myscrollbar1.pack(side="right",fill="y")
    canvas.pack(side="left")
    canvas.create_window((0,0),window=frame,anchor='n')
    frame.bind("<Configure>",myfunction)
    
    
    
    global v1
    global v2
    global v3
    global v4
    global v5
    global v6
    global v7
    global v8
    global v9
    global v10
    global v11
    global v12
    global v13
    global v14
    global v15
    global v16
    global v17
    global v18
    global v19
    global v20
    
    v1=IntVar(root)
    v2=IntVar(root)
    v3=IntVar(root)
    v4=IntVar(root)
    v5=IntVar(root)
    v6=IntVar(root)
    v7=IntVar(root)
    v8=IntVar(root)
    v9=IntVar(root)
    v10=IntVar(root)
    v11=IntVar(root)
    v12=IntVar(root)
    v13=IntVar(root)
    v14=IntVar(root)
    v15=IntVar(root)
    v16=IntVar(root)
    v17=IntVar(root)
    v18=IntVar(root)
    v19=IntVar(root)
    v20=IntVar(root)
   
    label1 = Label (frame,text="\t\tSELECT SUBJECT NAME:\t\t",justify=LEFT,bg="white",font=("courier","16","bold"))
    label1.grid(row=0,column=0,sticky =W)
    global tkvar50
    if((tkvar1.get()=='CSE')and(tkvar2.get()=='I')and(tkvar3.get()=='I')):
        tkvar50 = StringVar(root)
        choices=[]
        mycursor.execute("select subjects from subject where branch='cse' and year='I' and sem='I'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices)                                                                                                                                                                                                                                                                                            
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices[0])
    if((tkvar1.get()=='CSE')and(tkvar2.get()=='I')and(tkvar3.get()=='II')):
        tkvar50 = StringVar(root)
        choices1 = []
        mycursor.execute("select subjects from subject where branch='cse' and year='I' and sem='II'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices1.append(m)
        
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices1)
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices1[0])
    if((tkvar1.get()=='CSE')and(tkvar2.get()=='II')and(tkvar3.get()=='I')): 
        tkvar50 = StringVar(root)
        choices2 = []
        mycursor.execute("select subjects from subject where branch='cse' and year='II' and sem='I'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices2.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices2[0])
    if((tkvar1.get()=='CSE')and(tkvar2.get()=='II')and(tkvar3.get()=='II')):
        tkvar50 = StringVar(root)
        choices3 = []
        mycursor.execute("select subjects from subject where branch='cse' and year='II' and sem='II'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices3.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices3)
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices3[0])
    if((tkvar1.get()=='CSE')and(tkvar2.get()=='III')and(tkvar3.get()=='I')):
        tkvar50 = StringVar(root)
        choices4 = []
        mycursor.execute("select subjects from subject where branch='cse' and year='III' and sem='I'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices4.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices4)                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices4[0])
    if((tkvar1.get()=='CSE')and(tkvar2.get()=='III')and(tkvar3.get()=='II')):
        tkvar50 = StringVar(root)
        choices5 = [ ]
        mycursor.execute("select subjects from subject where branch='cse' and year='III'and sem='II'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices5.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices5)                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices5[0])
    if((tkvar1.get()=='CSE')and(tkvar2.get()=='IV')and(tkvar3.get()=='I')):
        tkvar50 = StringVar(root)
        choices6 = []
        mycursor.execute("select subjects from subject where branch='cse' and year='IV'and sem='I'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices6.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices6)                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices6[0])
    if((tkvar1.get()=='CSE')and(tkvar2.get()=='IV')and(tkvar3.get()=='II')):
        tkvar50 = StringVar(root)
        choices7 = []
        mycursor.execute("select subjects from subject where branch='cse' and year='IV'and sem='II'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices7.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices7)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices7[0])
    if((tkvar1.get()=='ECE')and(tkvar2.get()=='I')and(tkvar3.get()=='I')):
        tkvar50 = StringVar(root)
        choices8 = []
        mycursor.execute("select subjects from subject where branch='ECE' and year='I'and sem='I'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices8.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices8)                                                                                                                                                                                                                                                                                            
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices8[0])
    if((tkvar1.get()=='ECE')and(tkvar2.get()=='I')and(tkvar3.get()=='II')):
        tkvar50 = StringVar(root)
        choices9 = []
        mycursor.execute("select subjects from subject where branch='ECE' and year='I'and sem='II'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices9.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices9)
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices9[0])
    if((tkvar1.get()=='ECE')and(tkvar2.get()=='II')and(tkvar3.get()=='I')): 
        tkvar50 = StringVar(root)
        choices10= []
        mycursor.execute("select subjects from subject where branch='ECE' and year='II'and sem='I'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices10.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices10)                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices10[0])
    if((tkvar1.get()=='ECE')and(tkvar2.get()=='II')and(tkvar3.get()=='II')):
        tkvar50 = StringVar(root)
        choices11 = []
        mycursor.execute("select subjects from subject where branch='ECE' and year='II'and sem='II'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices11.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices11)
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices11[0])
    if((tkvar1.get()=='ECE')and(tkvar2.get()=='III')and(tkvar3.get()=='I')):
        tkvar50 = StringVar(root)
        choices12 = []
        mycursor.execute("select subjects from subject where branch='ECE' and year='III'and sem='I'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices12.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices12)                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices12[0])
    if((tkvar1.get()=='ECE')and(tkvar2.get()=='III')and(tkvar3.get()=='II')):
        tkvar50 = StringVar(root)
        choices13 = []
        mycursor.execute("select subjects from subject where branch='ECE' and year='III'and sem='II'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices13.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices13)                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices13[0])
    if((tkvar1.get()=='ECE')and(tkvar2.get()=='IV')and(tkvar3.get()=='I')):
        tkvar50 = StringVar(root)
        choices14 = []
        mycursor.execute("select subjects from subject where branch='ECE' and year='IV'and sem='I'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices14.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices14)                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices14[0])
    if((tkvar1.get()=='ECE')and(tkvar2.get()=='IV')and(tkvar3.get()=='II')):
        tkvar50 = StringVar(root)
        choices15 = []
        mycursor.execute("select subjects from subject where branch='ECE' and year='IV'and sem='II'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices15.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices15)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices15[0])
    if((tkvar1.get()=='CIVIL')and(tkvar2.get()=='I')and(tkvar3.get()=='I')):
        tkvar50 = StringVar(root)
        choices16 = []
        mycursor.execute("select subjects from subject where branch='CIVIL' and year='I'and sem='I'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices16.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices16)                                                                                                                                                                                                                                                                                            
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices16[0])
    if((tkvar1.get()=='CIVIL')and(tkvar2.get()=='I')and(tkvar3.get()=='II')):
        tkvar50 = StringVar(root)
        choices17 = []
        mycursor.execute("select subjects from subject where branch='CIVIL' and year='I'and sem='II'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices17.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices17)
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices17[0])
    if((tkvar1.get()=='CIVIL')and(tkvar2.get()=='II')and(tkvar3.get()=='I')): 
        tkvar50 = StringVar(root)
        choices18 = []
        mycursor.execute("select subjects from subject where branch='CIVIL' and year='II'and sem='I'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices18.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices18)                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices18[0])
    if((tkvar1.get()=='CIVIL')and(tkvar2.get()=='II')and(tkvar3.get()=='II')):
        tkvar50 = StringVar(root)
        choices19 = []
        mycursor.execute("select subjects from subject where branch='CIVIL' and year='II'and sem='II'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices19.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices19)                                                                                                        
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices19[0])
    if((tkvar1.get()=='CIVIL')and(tkvar2.get()=='III')and(tkvar3.get()=='I')):
        tkvar50 = StringVar(root)
        choices20 = []
        mycursor.execute("select subjects from subject where branch='CIVIL' and year='III'and sem='I'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices20.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices20)                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices20[0])
    if((tkvar1.get()=='CIVIL')and(tkvar2.get()=='III')and(tkvar3.get()=='II')):
        tkvar50 = StringVar(root)
        choices21 = []
        mycursor.execute("select subjects from subject where branch='CIVIL' and year='III'and sem='II'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices21.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices21)                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices21[0])
    if((tkvar1.get()=='CIVIL')and(tkvar2.get()=='IV')and(tkvar3.get()=='I')):
        tkvar50 = StringVar(root)
        choices22 = []
        mycursor.execute("select subjects from subject where branch='CIVIL' and year='IV'and sem='I'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices22.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices22)                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices22[0])
    if((tkvar1.get()=='CIVIL')and(tkvar2.get()=='IV')and(tkvar3.get()=='II')):
        tkvar50 = StringVar(root)
        choices23 = []
        mycursor.execute("select subjects from subject where branch='CIVIL' and year='IV'and sem='II'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices23.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices23)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices23[0])
    if((tkvar1.get()=='EEE')and(tkvar2.get()=='I')and(tkvar3.get()=='I')):
        tkvar50 = StringVar(root)
        choices24 = []
        mycursor.execute("select subjects from subject where branch='EEE' and year='I'and sem='I'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices24.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices24)                                                                                                                                                                                                                                                                                            
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices24[0])
    if((tkvar1.get()=='EEE')and(tkvar2.get()=='I')and(tkvar3.get()=='II')):
        tkvar50 = StringVar(root)
        choices25 = []
        mycursor.execute("select subjects from subject where branch='EEE' and year='I'and sem='II'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices25.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices25)
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices25[0])
    if((tkvar1.get()=='EEE')and(tkvar2.get()=='II')and(tkvar3.get()=='I')): 
        tkvar50 = StringVar(root)
        choices26 = []
        mycursor.execute("select subjects from subject where branch='EEE' and year='II'and sem='I'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices26.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices26)                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices26[0])
    if((tkvar1.get()=='EEE')and(tkvar2.get()=='II')and(tkvar3.get()=='II')):
        tkvar50 = StringVar(root)
        choices27 = []
        mycursor.execute("select subjects from subject where branch='EEE' and year='II'and sem='II'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices27.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices27)
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices27[0])
    if((tkvar1.get()=='EEE')and(tkvar2.get()=='III')and(tkvar3.get()=='I')):
        tkvar50 = StringVar(root)
        choices28 = []
        mycursor.execute("select subjects from subject where branch='EEE' and year='III'and sem='I'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices28.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices28)                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices28[0])
    if((tkvar1.get()=='EEE')and(tkvar2.get()=='III')and(tkvar3.get()=='II')):
        tkvar50 = StringVar(root)
        choices29 = []
        mycursor.execute("select subjects from subject where branch='EEE' and year='III'and sem='II'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices29.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices29)                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices29[0])
    if((tkvar1.get()=='EEE')and(tkvar2.get()=='IV')and(tkvar3.get()=='I')):
        tkvar50 = StringVar(root)
        choices30 = []
        mycursor.execute("select subjects from subject where branch='EEE' and year='IV'and sem='I'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices30.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices30)                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices30[0])
    if((tkvar1.get()=='EEE')and(tkvar2.get()=='IV')and(tkvar3.get()=='II')):
        tkvar50 = StringVar(root)
        choices31 = []
        mycursor.execute("select subjects from subject where branch='EEE' and year='IV'and sem='II'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices31.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices31)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices31[0])
    if((tkvar1.get()=='MECH')and(tkvar2.get()=='I')and(tkvar3.get()=='I')):
        tkvar50 = StringVar(root)
        choices32 = []
        mycursor.execute("select subjects from subject where branch='MECH' and year='I'and sem='I'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices32.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices32)                                                                                                                                                                                                                                                                                            
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices32[0])
    if((tkvar1.get()=='MECH')and(tkvar2.get()=='I')and(tkvar3.get()=='II')):
        tkvar50 = StringVar(root)
        choices33= [ ]
        mycursor.execute("select subjects from subject where branch='MECH' and year='I'and sem='II'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices33.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices33)
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices33[0])
    if((tkvar1.get()=='MECH')and(tkvar2.get()=='II')and(tkvar3.get()=='I')): 
        tkvar50 = StringVar(root)
        choices34= []
        mycursor.execute("select subjects from subject where branch='MECH' and year='II'and sem='I'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices34.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices34)                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices34[0])
    if((tkvar1.get()=='MECH')and(tkvar2.get()=='II')and(tkvar3.get()=='II')):
        tkvar50 = StringVar(root)
        choices35 = []
        mycursor.execute("select subjects from subject where branch='MECH' and year='I'and sem='II'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices35.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices35)
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices35[0])
    if((tkvar1.get()=='MECH')and(tkvar2.get()=='III')and(tkvar3.get()=='I')):
        tkvar50 = StringVar(root)
        choices36 = []
        mycursor.execute("select subjects from subject where branch='MECH' and year='III'and sem='I'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices36.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices36)                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices36[0])
    if((tkvar1.get()=='MECH')and(tkvar2.get()=='III')and(tkvar3.get()=='II')):
        tkvar50 = StringVar(root)
        choices37 = []
        mycursor.execute("select subjects from subject where branch='MECH' and year='III'and sem='II'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices37.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices37)                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices37[0])
    if((tkvar1.get()=='MECH')and(tkvar2.get()=='IV')and(tkvar3.get()=='I')):
        tkvar50 = StringVar(root)
        choices38 = []
        mycursor.execute("select subjects from subject where branch='MECH' and year='IV'and sem='I'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices38.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices38)                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices38[0])
    if((tkvar1.get()=='MECH')and(tkvar2.get()=='IV')and(tkvar3.get()=='II')):
        tkvar50 = StringVar(root)
        choices39 = [ ]
        mycursor.execute("select subjects from subject where branch='MECH' and year='IV'and sem='II'")
        fs=mycursor.fetchall()
        for row in fs:
           for m in row:
               choices39.append(m)
        conn.commit()
        popupMenu = OptionMenu(frame, tkvar50, *choices39)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
        popupMenu.grid(row =0 , column =0,sticky=E)
        tkvar50.set(choices39[0])

    
    #questions and radio buttons
    label2 = Label (frame, text="1.Teacher is prepared at class and good at blackboard management:",justify=LEFT,bg="white",font=("open sans","9","bold italic"))
    label2.grid(row=1,column=0,sticky = NW)
    R1 = Radiobutton(frame, text="below average", variable= v1, value=1,bg="white",tristatevalue="x")
    R1.grid(row=2,column=0,sticky=NW)
    R2 = Radiobutton(frame, text="average\t\t\t\t", variable=v1, value=2,bg="white",tristatevalue="x")
    R2.grid(row=2,column=0)
    R3 = Radiobutton(frame, text="good\t\t\t\t", variable=v1, value=3,bg="white",tristatevalue="x")
    R3.grid(row=2,column=0,sticky=NE)
    R4 = Radiobutton(frame, text="very good\t\t\t\t", variable=v1, value=4,bg="white",tristatevalue="x")
    R4.grid(row=2,column=1,sticky=NW)
    R5 = Radiobutton(frame, text="excellent", variable=v1, value=5,bg="white",tristatevalue="x")
    R5.grid(row=2,column=2)
    label3 = Label (frame, text="2.Teacher knows his/her subject. His lecture is audible and expressed with clarity:",bg="white",font=("open sans","9","bold italic"))
    label3.grid(row=3,column=0,sticky = NW)
    R6 = Radiobutton(frame, text="below average", variable=v2, value=1,bg="white",tristatevalue="x")
    R6.grid(row=4,column=0,sticky = NW)
    R7 = Radiobutton(frame, text="average\t\t\t\t", variable=v2, value=2,bg="white",tristatevalue="x")
    R7.grid(row=4,column=0)
    R8 = Radiobutton(frame, text="good\t\t\t\t", variable=v2, value=3,bg="white",tristatevalue="x")
    R8.grid(row=4,column=0,sticky = NE)
    R9 = Radiobutton(frame, text="very good\t\t\t\t", variable=v2,value=4,bg="white",tristatevalue="x")
    R9.grid(row=4,column=1,sticky = NW)
    R10 = Radiobutton(frame, text="excellent", variable=v2, value=5,bg="white",tristatevalue="x")
    R10.grid(row=4,column=2)
    label4 = Label (frame, text="3.Teacher is organized,good gait and etiquette:",bg="white",font=("open sans","9","bold italic"))
    label4.grid(row=5,column=0,sticky = NW)
    R11 = Radiobutton(frame, text="below average", variable=v3, value=1,bg="white",tristatevalue="x")
    R11.grid(row=6,column=0,sticky = NW)
    R12 = Radiobutton(frame, text="average\t\t\t\t", variable=v3, value=2,bg="white",tristatevalue="x")
    R12.grid(row=6,column=0)
    R13 = Radiobutton(frame, text="good\t\t\t\t", variable=v3, value=3,bg="white",tristatevalue="x")
    R13.grid(row=6,column=0,sticky = NE)
    R14 = Radiobutton(frame, text="very good\t\t\t\t", variable=v3,value=4,bg="white",tristatevalue="x")
    R14.grid(row=6,column=1,sticky = NW)
    R15 = Radiobutton(frame, text="excellent", variable=v3,value=5,bg="white",tristatevalue="x")
    R15.grid(row=6,column=2)
    label5 = Label (frame, text="4.Teacher is punctual to class,plans class time and helps students to solve problems and think critically:",bg="white",font=("open sans","9","bold italic"))
    label5.grid(row=7,column=0,sticky = NW)
    R16 = Radiobutton(frame, text="below average", variable=v4, value=1,bg="white",tristatevalue="x")
    R16.grid(row=8,column=0,sticky = NW)
    R17 = Radiobutton(frame, text="average\t\t\t\t", variable=v4, value=2,bg="white",tristatevalue="x")
    R17.grid(row=8,column=0)
    R18 = Radiobutton(frame, text="good\t\t\t\t", variable=v4, value=3,bg="white",tristatevalue="x")
    R18.grid(row=8,column=0,sticky = NE)
    R19 = Radiobutton(frame, text="very good\t\t\t\t", variable=v4,value=4,bg="white",tristatevalue="x")
    R19.grid(row=8,column=1,sticky = NW)
    R20 = Radiobutton(frame, text="excellent", variable=v4,value=5,bg="white",tristatevalue="x")
    R20.grid(row=8,column=2)
    label6 = Label (frame, text="5.Teacher encourages Seminars/Workshops/Industrial Visits/Guest Lectures:",bg="white",font=("open sans","9","bold italic"))
    label6.grid(row=9,column=0,sticky = NW)
    R21 = Radiobutton(frame, text="below average", variable=v5, value=1,bg="white",tristatevalue="x")
    R21.grid(row=10,column=0,sticky = NW)
    R22 = Radiobutton(frame, text="average\t\t\t\t", variable=v5, value=2,bg="white",tristatevalue="x")
    R22.grid(row=10,column=0)
    R23 = Radiobutton(frame, text="good\t\t\t\t", variable=v5, value=3,bg="white",tristatevalue="x")
    R23.grid(row=10,column=0,sticky = NE)
    R24 = Radiobutton(frame, text="very good\t\t\t\t", variable=v5,value=4,bg="white",tristatevalue="x")
    R24.grid(row=10,column=1,sticky = NW)
    R25 = Radiobutton(frame, text="excellent", variable=v5,value=5,bg="white",tristatevalue="x")
    R25.grid(row=10,column=2)
    label7 = Label (frame, text="6.Teacher is clear in giving directions and explaining what is expected in tests. He has clear idea in setting question paper:",bg="white",font=("open sans","9","bold italic"))
    label7.grid(row=11,column=0,sticky = NW)
    R26 = Radiobutton(frame, text="below average", variable=v6, value=1,bg="white",tristatevalue="x")
    R26.grid(row=12,column=0,sticky = NW)
    R27 = Radiobutton(frame, text="average\t\t\t\t", variable=v6, value=2,bg="white",tristatevalue="x")
    R27.grid(row=12,column=0)
    R28 = Radiobutton(frame, text="good\t\t\t\t", variable=v6, value=3,bg="white",tristatevalue="x")
    R28.grid(row=12,column=0,sticky = NE)
    R29 = Radiobutton(frame, text="very good\t\t\t\t", variable=v6,value=4,bg="white",tristatevalue="x")
    R29.grid(row=12,column=1,sticky = NW)
    R30 = Radiobutton(frame, text="excellent", variable=v6,value=5,bg="white",tristatevalue="x")
    R30.grid(row=12,column=2)
    label8 = Label (frame, text="7.Teachers allows you to be active in the classroom learning environment:",bg="white",font=("open sans","9","bold italic"))
    label8.grid(row=13,column=0,sticky = NW)
    R31 = Radiobutton(frame, text="below average", variable=v7, value=1,bg="white",tristatevalue="x")
    R31.grid(row=14,column=0,sticky = NW)
    R32 = Radiobutton(frame, text="average\t\t\t\t", variable=v7, value=2,bg="white",tristatevalue="x")
    R32.grid(row=14,column=0)
    R33 = Radiobutton(frame, text="good\t\t\t\t", variable=v7, value=3,bg="white",tristatevalue="x")
    R33.grid(row=14,column=0,sticky = NE)
    R34 = Radiobutton(frame, text="very good\t\t\t\t", variable=v7,value=4,bg="white",tristatevalue="x")
    R34.grid(row=14,column=1,sticky = NW)
    R35 = Radiobutton(frame, text="excellent", variable=v7,value=5,bg="white",tristatevalue="x")
    R35.grid(row=14,column=2)
    label9 = Label (frame, text="8.Teacher manages the time well and covers the syllabus:",bg="white",font=("open sans","9","bold italic"))
    label9.grid(row=15,column=0,sticky = NW)
    R36 = Radiobutton(frame, text="below average", variable=v8, value=1,bg="white",tristatevalue="x")
    R36.grid(row=16,column=0,sticky = NW)
    R37 = Radiobutton(frame, text="average\t\t\t\t", variable=v8, value=2,bg="white",tristatevalue="x")
    R37.grid(row=16,column=0)
    R38 = Radiobutton(frame, text="good\t\t\t\t", variable=v8, value=3,bg="white",tristatevalue="x")
    R38.grid(row=16,column=0,sticky = NE)
    R39 = Radiobutton(frame, text="very good\t\t\t\t", variable=v8,value=4,bg="white",tristatevalue="x")
    R39.grid(row=16,column=1,sticky = NW)
    R40 = Radiobutton(frame, text="excellent", variable=v8,value=5,bg="white",tristatevalue="x")
    R40.grid(row=16,column=2)
    label8 = Label (frame, text="9.Teacher awards marks fairly.Teacher is impartial.Teacher conducts examination as per schedule:",bg="white",font=("open sans","9","bold italic"))
    label8.grid(row=17,column=0,sticky = NW)
    R41 = Radiobutton(frame, text="below average", variable=v9, value=1,bg="white",tristatevalue="x")
    R41.grid(row=18,column=0,sticky = NW)
    R42 = Radiobutton(frame, text="average\t\t\t\t", variable=v9, value=2,bg="white",tristatevalue="x")
    R42.grid(row=18,column=0)
    R43 = Radiobutton(frame, text="good\t\t\t\t", variable=v9, value=3,bg="white",tristatevalue="x")
    R43.grid(row=18,column=0,sticky = NE)
    R44 = Radiobutton(frame, text="very good\t\t\t\t", variable=v9,value=4,bg="white",tristatevalue="x")
    R44.grid(row=18,column=1,sticky = NW)
    R45 = Radiobutton(frame, text="excellent", variable=v9,value=5,bg="white",tristatevalue="x")
    R45.grid(row=18,column=2)
    label9 = Label (frame, text="10.I have learned a lot about this subject and the teacher motivates the students in gloabal aspects and soft skills besides teaching:",bg="white",font=("open sans","9","bold italic"))
    label9.grid(row=19,column=0,sticky = NW)
    R46 = Radiobutton(frame, text="below average", variable=v10, value=1,bg="white",tristatevalue="x")
    R46.grid(row=20,column=0,sticky = NW)
    R47 = Radiobutton(frame, text="average\t\t\t\t", variable=v10, value=2,bg="white",tristatevalue="x")
    R47.grid(row=20,column=0)
    R48 = Radiobutton(frame, text="good\t\t\t\t", variable=v10, value=3,bg="white",tristatevalue="x")
    R48.grid(row=20,column=0,sticky = NE)
    R49 = Radiobutton(frame, text="very good\t\t\t\t", variable=v10,value=4,bg="white",tristatevalue="x")
    R49.grid(row=20,column=1,sticky = NW)
    R50 = Radiobutton(frame, text="excellent", variable=v10,value=5,bg="white",tristatevalue="x")
    R50.grid(row=20,column=2)
    labe20 = Label (frame, text="11.Teachers helps towards varied academic interest of students.(like GATE/GRE/CAT):",bg="white",font=("open sans","9","bold italic"))
    labe20.grid(row=21,column=0,sticky = NW)
    R51 = Radiobutton(frame, text="below average", variable=v11, value=1,bg="white",tristatevalue="x")
    R51.grid(row=22,column=0,sticky = NW)
    R52 = Radiobutton(frame, text="average\t\t\t\t", variable=v11, value=2,bg="white",tristatevalue="x")
    R52.grid(row=22,column=0)
    R53 = Radiobutton(frame, text="good\t\t\t\t", variable=v11, value=3,bg="white",tristatevalue="x")
    R53.grid(row=22,column=0,sticky = NE)
    R54 = Radiobutton(frame, text="very good\t\t\t\t", variable=v11,value=4,bg="white",tristatevalue="x")
    R54.grid(row=22,column=1,sticky = NW)
    R55 = Radiobutton(frame, text="excellent", variable=v11,value=5,bg="white",tristatevalue="x")
    R55.grid(row=22,column=2)
    labe21 = Label (frame, text="12.Teacher uses advanced teaching aids like PPTs/Vedios/simulations:",bg="white",font=("open sans","9","bold italic"))
    labe21.grid(row=23,column=0,sticky = NW)
    R56 = Radiobutton(frame, text="below average", variable=v12, value=1,bg="white",tristatevalue="x")
    R56.grid(row=24,column=0,sticky = NW)
    R57 = Radiobutton(frame, text="average\t\t\t\t", variable=v12, value=2,bg="white",tristatevalue="x")
    R57.grid(row=24,column=0)
    R58 = Radiobutton(frame, text="good\t\t\t\t", variable=v12, value=3,bg="white",tristatevalue="x")
    R58.grid(row=24,column=0,sticky = NE)
    R59 = Radiobutton(frame, text="very good", variable=v12,value=4,bg="white",tristatevalue="x")
    R59.grid(row=24,column=1,sticky = NW)
    R60 = Radiobutton(frame, text="excellent", variable=v12,value=5,bg="white",tristatevalue="x")
    R60.grid(row=24,column=2)
    labe22 = Label (frame, text="13.Teacher encourages students to speak up and active in class:",bg="white",font=("open sans","9","bold italic"))
    labe22.grid(row=25,column=0,sticky = NW)
    R61 = Radiobutton(frame, text="below average", variable=v13, value=1,bg="white",tristatevalue="x")
    R61.grid(row=26,column=0,sticky = NW)
    R62 = Radiobutton(frame, text="average\t\t\t\t", variable=v13, value=2,bg="white",tristatevalue="x")
    R62.grid(row=26,column=0)
    R63 = Radiobutton(frame, text="good\t\t\t\t", variable=v13, value=3,bg="white",tristatevalue="x")
    R63.grid(row=26,column=0,sticky = NE)
    R64 = Radiobutton(frame, text="very good\t\t\t\t", variable=v13,value=4,bg="white",tristatevalue="x")
    R64.grid(row=26,column=1,sticky = NW)
    R65 = Radiobutton(frame, text="excellent", variable=v13,value=5,bg="white",tristatevalue="x")
    R65.grid(row=26,column=2)
    labe23 = Label (frame, text="14.Teacher encourages genuine Research and Poster/Paper presentation in premier institutions:",bg="white",font=("open sans","9","bold italic"))
    labe23.grid(row=27,column=0,sticky = NW)
    R66 = Radiobutton(frame, text="below average", variable=v14, value=1,bg="white",tristatevalue="x")
    R66.grid(row=28,column=0,sticky = NW)
    R67 = Radiobutton(frame, text="average\t\t\t\t", variable=v14, value=2,bg="white",tristatevalue="x")
    R67.grid(row=28,column=0)
    R68 = Radiobutton(frame, text="good\t\t\t\t", variable=v14, value=3,bg="white",tristatevalue="x")
    R68.grid(row=28,column=0,sticky = NE)
    R69 = Radiobutton(frame, text="very good\t\t\t\t", variable=v14,value=4,bg="white",tristatevalue="x")
    R69.grid(row=28,column=1,sticky = NW)
    R70 = Radiobutton(frame, text="excellent", variable=v14,value=5,bg="white",tristatevalue="x")
    R70.grid(row=28,column=2)
    labe24 = Label (frame, text="15.Teacher helps students in imparting Ethical and Moral Canducts:",bg="white",font=("open sans","9","bold italic"))
    labe24.grid(row=29,column=0,sticky = NW)
    R71 = Radiobutton(frame, text="below average", variable=v15, value=1,bg="white",tristatevalue="x")
    R71.grid(row=30,column=0,sticky = NW)
    R72 = Radiobutton(frame, text="average\t\t\t\t", variable=v15, value=2,bg="white",tristatevalue="x")
    R72.grid(row=30,column=0)
    R73 = Radiobutton(frame, text="good\t\t\t\t", variable=v15, value=3,bg="white",tristatevalue="x")
    R73.grid(row=30,column=0,sticky = NE)
    R74 = Radiobutton(frame, text="very good\t\t\t\t", variable=v15,value=4,bg="white",tristatevalue="x")
    R74.grid(row=30,column=1,sticky = NW)
    R75 = Radiobutton(frame, text="excellent", variable=v15,value=5,bg="white",tristatevalue="x")
    R75.grid(row=30,column=2)
    labe25 = Label (frame, text="16.Teacher adjusts class work when on leave or compensates missed classes.teacher is willing to accept responsibility for his/her own mistake:",bg="white",font=("open sans","9","bold italic"))
    labe25.grid(row=31,column=0,sticky = NW)
    R76 = Radiobutton(frame, text="below average", variable=v16, value=1,bg="white",tristatevalue="x")
    R76.grid(row=32,column=0,sticky = NW)
    R77 = Radiobutton(frame, text="average\t\t\t\t", variable=v16, value=2,bg="white",tristatevalue="x")
    R77.grid(row=32,column=0)
    R78 = Radiobutton(frame, text="good\t\t\t\t", variable=v16, value=3,bg="white",tristatevalue="x")
    R78.grid(row=32,column=0,sticky = NE)
    R79 = Radiobutton(frame, text="very good", variable=v16,value=4,bg="white",tristatevalue="x")
    R79.grid(row=32,column=1,sticky = NW)
    R80 = Radiobutton(frame, text="excellent", variable=v16,value=5,bg="white",tristatevalue="x")
    R80.grid(row=32,column=2,sticky = NW)
    labe26 = Label (frame, text="17.Teachers is consistent,fair and firm in discipline without being too strict:",bg="white",font=("open sans","9","bold italic"))
    labe26.grid(row=33,column=0,sticky = NW)
    R81 = Radiobutton(frame, text="below average", variable=v17, value=1,bg="white",tristatevalue="x")
    R81.grid(row=34,column=0,sticky = NW)
    R82 = Radiobutton(frame, text="average\t\t\t\t", variable=v17, value=2,bg="white",tristatevalue="x")
    R82.grid(row=34,column=0)
    R83 = Radiobutton(frame, text="good\t\t\t\t", variable=v17, value=3,bg="white",tristatevalue="x")
    R83.grid(row=34,column=0,sticky = NE)
    R84 = Radiobutton(frame, text="very good\t\t\t\t", variable=v17,value=4,bg="white",tristatevalue="x")
    R84.grid(row=34,column=1,sticky = NW)
    R85 = Radiobutton(frame, text="excellent", variable=v17,value=5,bg="white",tristatevalue="x")
    R85.grid(row=34,column=2)
    labe27 = Label (frame, text="18.Teacher is interactive and encourages discussions and Conversastions:",bg="white",font=("open sans","9","bold italic"))
    labe27.grid(row=35,column=0,sticky = NW)
    R86 = Radiobutton(frame, text="below average", variable=v18, value=1,bg="white",tristatevalue="x")
    R86.grid(row=36,column=0,sticky = NW)
    R87 = Radiobutton(frame, text="average\t\t\t\t", variable=v18, value=2,bg="white",tristatevalue="x")
    R87.grid(row=36,column=0)
    R88 = Radiobutton(frame, text="good\t\t\t\t", variable=v18, value=3,bg="white",tristatevalue="x")
    R88.grid(row=36,column=0,sticky = NE)
    R89 = Radiobutton(frame, text="very good\t\t\t\t", variable=v18,value=4,bg="white",tristatevalue="x")
    R89.grid(row=36,column=1,sticky = NW)
    R90 = Radiobutton(frame, text="excellent", variable=v18,value=5,bg="white",tristatevalue="x")
    R90.grid(row=36,column=2)
    labe28 = Label (frame, text="19.Teacher is avaliable/accessible to the student:",bg="white",font=("open sans","9","bold italic"))
    labe28.grid(row=37,column=0,sticky = NW)
    R100 = Radiobutton(frame, text="below average", variable=v19, value=1,bg="white",tristatevalue="x")
    R100.grid(row=38,column=0,sticky = NW)
    R102 = Radiobutton(frame, text="average\t\t\t\t", variable=v19, value=2,bg="white",tristatevalue="x")
    R102.grid(row=38,column=0)
    R103 = Radiobutton(frame, text="good\t\t\t\t", variable=v19, value=3,bg="white",tristatevalue="x")
    R103.grid(row=38,column=0,sticky = NE)
    R104 = Radiobutton(frame, text="very good\t\t\t\t", variable=v19,value=4,bg="white",tristatevalue="x")
    R104.grid(row=38,column=1,sticky = NW)
    R105= Radiobutton(frame, text="excellent", variable=v19,value=5,bg="white",tristatevalue="x")
    R105.grid(row=38,column=2)
    labe29 = Label (frame, text="20.Overall performance of a teacher:",bg="white",font=("open sans","9","bold italic"))
    labe29.grid(row=39,column=0,sticky = NW)
    R106 = Radiobutton(frame, text="below average", variable=v20, value=1,bg="white",tristatevalue="x")
    R106.grid(row=40,column=0,sticky = NW)
    R107 = Radiobutton(frame, text="average\t\t\t\t", variable=v20, value=2,bg="white",tristatevalue="x")
    R107.grid(row=40,column=0)
    R108= Radiobutton(frame, text="good\t\t\t\t", variable=v20, value=3,bg="white",tristatevalue="x")
    R108.grid(row=40,column=0,sticky = NE)
    R109 = Radiobutton(frame, text="very good", variable=v20,value=4,bg="white",tristatevalue="x")
    R109.grid(row=40,column=1,sticky = NW)
    R200 = Radiobutton(frame, text="excellent", variable=v20,value=5,bg="white",tristatevalue="x")
    R200.grid(row=40,column=2)
    label2 = Label (frame, text="additional_feedback",justify=LEFT,bg="white",font=("open sans","9","bold italic"))
    label2.grid(row=41,column=0,sticky = NW)
    global text
    text=ScrolledText(frame)
    text.grid(row=42,column=0,sticky=W)
    text.config(width=110,height=20)
    MyButton1 = Button(frame, text="submit", width=10,command=get_radiobutton_id)
    MyButton1.grid(row=43,column=4)
    global fetched_content
    fetched_content = 'NULL'
    root.mainloop()

def helloa():
        popupmsg1("project details : \ndeveloper : Y.DEDEEPYA\ncollege : JTNUK-UCEN\nbranch : CSE 3rd YEAR ")
def dest():
    popup.destroy()
def popupmsg(msg):
    global popup
    popup=Tk()
    popup.wm_title("!")
    popup.config(bg="white")
    label90=Label(popup,text=msg,font=("open sans","9","bold italic"),bg='red')
    label90.grid(row=0,column=0)
    b1=Button(popup,text="okay",command=dest)
    b1.grid(row=1,column=0)
    #tkinter.messagebox.showinfo("submit message", "you should fill all the questions")
def get_radiobutton_id():
   global fetched_content
   fetched_content = text.get('1.0', 'end-1c')
   x=str(tkvar50.get())
   s=0
   
   mylist=[v1.get(),v2.get(),v3.get(),v4.get(),v5.get(),v6.get(),v7.get(),v8.get(),v9.get(),v10.get(),v11.get(),v12.get(),v13.get(),v14.get(),v15.get(),v16.get(),v17.get(),v18.get(),v19.get(),v20.get()]
   if(0 in mylist):
       popupmsg("you should fill all the questions")
   else:
       
       z=(v1.get()+v2.get()+v3.get()+v4.get()+v5.get()+v6.get()+v7.get()+v8.get()+v9.get()+v10.get()+v11.get()+v12.get()+v13.get()+v14.get()+v15.get()+v16.get()+v17.get()+v18.get()+v19.get()+v20.get())/20
       
       mycursor.execute("show tables from jntuk_ucen")
       qa=mycursor.fetchall()
       
       u=[]
       for row in qa:
           for g in row:
               u.append(g)
               
       #print(u[0])
       #zi=[]
       #zi.append(x.lower())
       #print(zi[0])
       #if(zi[0] not in u):
        #   print(len(zi[0]))
        #   print(u)
         #  print(len(u[0]))
       #else:
        #   print("hi")
        
       if(x.lower() not in u):
           mycursor.execute("create table {}(q1 int,q2 int,q3 int,q4 int,q5 int,q6 int,q7 int,q8 int,q9 int,q10 int,q11 int,q12 int,q13 int,q14 int,q15 int,q16 int,q17 int,q18 int,q19 int,q20 int,additionalfeedback text,average double,totalavg double)".format(x))
       mycursor.execute("select avg(average) from {}".format(x))
       l=mycursor.fetchall()
       mycursor.execute("select count(average) from {}".format(x))
       n=mycursor.fetchall()
       for row in n:
           b=row[0]
       for row in l:
           h=row[0]
    
       if(h==None):
           q=z
       else:
            q=((h*b)+z)/(b+1)
       mycursor.execute("INSERT INTO {} (q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,additionalfeedback,average,totalavg) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(x),(v1.get(),v2.get(),v3.get(),v4.get(),v5.get(),v6.get(),v7.get(),v8.get(),v9.get(),v10.get(),v11.get(),v12.get(),v13.get(),v14.get(),v15.get(),v16.get(),v17.get(),v18.get(),v19.get(),v20.get(),fetched_content,z,q)) 
       conn.commit()
       popupmsg1("succesfully submited")
       root.destroy()
def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=1300,height=600)
root1=Tk()
root1.geometry('10000x700')
myframe=Frame(root1, width=500, height=150, background="white")
myframe.place(x=10,y=10)
root1.title("feedbackform")
menubar = Menu(root1)
menubar.add_command(label="about", command=helloa)
root1.config(menu=menubar)
canvas=Canvas(myframe)
frame=Frame(canvas)
myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

myscrollbar.pack(side="right",fill="y")
canvas.pack(side="left")
canvas.create_window((0,0),window=frame,anchor='center')
frame.bind("<Configure>",myfunction)

label2 = Label (frame,text="\n\n\n\n\n\n\n\n\t\t\t\tBRANCH :",justify=LEFT,font=("courier","16","bold"))
label2.grid(row=0,column=0,sticky = E)
tkvar1 = StringVar(root1)

choices = [ 'CSE','ECE','EEE','MECH','CIVIL' ]
popupMenu = OptionMenu(frame, tkvar1, *choices)
popupMenu.grid(row =0 , column =1,sticky=S)
tkvar1.set('CSE')
label2 = Label (frame,text="YEAR  : ",justify=LEFT,font=("courier","16","bold"))
label2.grid(row=1,column=0,sticky = E)
tkvar2 = StringVar(root1)
choices = [ 'I','II','III','IV']
popupMenu = OptionMenu(frame, tkvar2, *choices)
popupMenu.grid(row = 1, column =1)
tkvar2.set('IV')
label2 = Label (frame,text="SEM : ",justify=LEFT,font=("courier","16","bold"))
label2.grid(row=2,column=0,sticky = E)
tkvar3 = StringVar(root1)
choices = ['I','II']
popupMenu = OptionMenu(frame, tkvar3, *choices)
popupMenu.grid(row = 2, column =1)
tkvar3.set('I')
MyButton0 = Button(frame, text="submit", width=10,command=data)
MyButton0.grid(row=4,column=2,sticky=E)
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
def destroy():
        root3.destroy()
root1.mainloop()
