#!/usr/bin/python
from tkinter import *
import mysql.connector  
from mysql.connector import Error
import tkinter.messagebox as mess
hare=Tk()
hieght=400
width=500
hare.geometry("800x800")
hare.title("My first GUI")

def post():
    myconn = mysql.connector.connect(host = "rome.viewen.com", user = "desiretr_vishnu",passwd = "Vishnu1999",database="desiretr_python")  
  
    #printing the connection object   
    print(myconn)  
    cur = myconn.cursor()  
    sql = "insert into users(f_name,l_name,ibsn,date,book) values (%s, %s, %s, %s, %s)"  
  
    #The row values are provided in the form of tuple   
    val = (fname1.get(),lname1.get(),ibsn1.get(),date1.get(),book_name1.get())  
  
    try:  
    #inserting the values into the table  
        cur.execute(sql,val)  
  
    #commit the transaction   
        tab=myconn.commit()
        if tab == None:
            mess.showinfo("Result","Book Issued suceesfully")
        else:
            mess.showinfo("Result"," OOPS There might be some problem")
      
    except:  
        myconn.rollback()  
  
    print(cur.rowcount,"record inserted!")

    myconn.close()  
def get():
    myconn = mysql.connector.connect(host = "rome.viewen.com", user = "desiretr_vishnu",passwd = "Vishnu1999",database="desiretr_python")  
  
    #printing the connection object   
    print(myconn)  
    cur = myconn.cursor()  
    sql = "insert into vapas(f_name,ibsn,book,date) values (%s, %s, %s, %s)"  
  
    #The row values are provided in the form of tuple   
    val = (lname_val.get(),ibsn_val.get(),book_val.get(),date_val.get())  
  
    try:  
    #inserting the values into the table  
        cur.execute(sql,val)  
  
    #commit the transaction   
        dekh=myconn.commit()  
        if dekh == None:
            mess.showinfo("Result","Book Returned suceesfully")
        else:
            mess.showinfo("Result"," OOPS There might be some problem")
    except:  
        myconn.rollback()  
  
    print(cur.rowcount,"record inserted!")

    myconn.close()  
def search():
   
    
    #Create the connection object   
    myconn = mysql.connector.connect(host = "rome.viewen.com", user = "desiretr_vishnu",passwd = "Vishnu1999",database="desiretr_python")    
  
    #creating the cursor object  
    cur = myconn.cursor()  
  
    try:  
        #Reading the Employee data      
   
        sql_Query = "select book from vapas where book =%s"
        
  
        #fetching the rows from the cursor object  
        """result = cur.fetchall()    
        print(ibsn_value.get())
        for record in result:
            print(record) """
        name=(ibsn_value.get(),)
        cursor = myconn.cursor(buffered=True)
        cursor.execute(sql_Query, name)
        record = cursor.fetchone()
        print(record)
        if record == None:
            mess.showinfo("Result","Not in Stock")
        else:
            mess.showinfo("Result","Is in Stock")
            
    except mysql.connector.Error as error:
        print("Failed to get record from database: {}".format(error))
      
    myconn.close()  
t=Label(hare,text="issue",bg="red").place(x=50,y=5)
fname=Label(hare,text="First Name")
lname=Label(hare,text="Last Name")
ibsn=Label(hare,text="Book IBSN ")
date=Label(hare,text="Date")
book_name=Label(hare,text="Book Name")

fname.grid(row=3,column=4)
lname.grid(row=4,column=4)
ibsn.grid(row=5,column=4)
date.grid(row=6,column=4)
book_name.grid(row=7,column=4)

fname1=StringVar()
lname1=StringVar()
ibsn1=IntVar()
date1=StringVar()
book_name1=StringVar()

fname_entry=Entry(hare,textvariable=fname1)
lname_entry=Entry(hare,textvariable=lname1)
ibsn_entry=Entry(hare,textvariable=ibsn1)
date_entry=Entry(hare,textvariable=date1)
book_name_entry=Entry(hare,textvariable=book_name1)

fname.grid(row=3,column=1)
lname.grid(row=4,column=1)
ibsn.grid(row=5,column=1)
date.grid(row=6,column=1)
book_name.grid(row=7,column=1)


fname_entry.grid(row=3,column=3)
lname_entry.grid(row=4,column=3)
ibsn_entry.grid(row=5,column=3)
date_entry.grid(row=6,column=3)
book_name_entry.grid(row=7,column=3)
Button(text="Submit", command=post).grid(row=8,column=3)


r=Label(hare,text="Return",bg="red").place(x=230,y=3)
lname_return=Label(hare,text="First Name")
ibsn_return=Label(hare,text="Book IBSN ")
date_return=Label(hare,text="Date")
book_return=Label(hare,text="Book name")
lname_return.grid(row=5,column=6)
ibsn_return.grid(row=6,column=6)
date_return.grid(row=7,column=6)
book_return.grid(row=8,column=6)

lname_val=StringVar()
ibsn_val=IntVar()
date_val=StringVar()
book_val=StringVar()

lname_en_val=Entry(hare,textvariable=lname_val)
ibsn_en_val=Entry(hare,textvariable=ibsn_val)
date_en_val=Entry(hare,textvariable=date_val)
book_en_val=Entry(hare,textvariable=book_val)

lname_en_val.grid(row=5,column=9)
ibsn_en_val.grid(row=6,column=9)
date_en_val.grid(row=7,column=9)
book_en_val.grid(row=8,column=9)
Button(text="Submit", command=get).grid(row=9,column=9)

s=Label(hare,text="serach",bg="blue").place(x=500,y=4)


ibsn_sea=Label(hare,text="Book Name ")
ibsn_sea.grid(row=6,column=10)



ibsn_value=StringVar()


ibsn_en_value=Entry(hare,textvariable=ibsn_value)



ibsn_en_value.grid(row=6,column=11)

Button(text="Search", command=search).grid(row=7,column=11)


hare.mainloop()
