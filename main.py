import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector as my

from tkinter import *


def getValue(event=""):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0, select['Identity Number'])
    e2.insert(0, select['Emp Name'])
    e3.insert(0, select['Contact'])
    e4.insert(0, select['Salary'])


# cols = ('Identity Number', 'Emp Name', 'Contact', 'Salary')

def Add():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    fee = e4.get()

    mysqldb = my.connect(host='localhost', user='root', password='root', database='payroll_b2')
    mycursor = mysqldb.cursor()

    try:
        sql = "insert into registration (id,empname,mobile,salary) value(%s,%s,%s,%s)"
        val = (studid, studname, coursename, fee)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Employee inserted successfully")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()

    except Exception as e:
        print(e)
        messagebox.showwarning("                        Input error", "        Duplicate Id number or \nRecords not inserted completely")
        mysqldb.rollback()
        mysqldb.close()


def update():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    fee = e4.get()
    mysqldb = my.connect(host='localhost', user='root', password='root', database='payroll_b2')
    mycursor = mysqldb.cursor()

    try:
        sql = "Update registration set empname = %s, mobile = %s, salary = %s where id = %s"
        val = (studname, coursename, fee, studid)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record updated successfully")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()

    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def delete():
    studid = e1.get()
    mysqldb = my.connect(host='localhost', user='root', password='root', database='payroll_b2')
    mycursor = mysqldb.cursor()

    try:
        sql = "delete from registration where id = %s"
        val = (studid,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record deleted successfully")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()

    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def show():
    mysqldb = my.connect(host='localhost', user='root', password='root', database='payroll_b2')
    mycursor = mysqldb.cursor()
    mycursor.execute('select id,empname,mobile,salary from registration')
    records = mycursor.fetchall()
    print(records)

    for i, (id, empname, mobile, salary) in enumerate(records, start=0):
        listBox.insert("", 'end', values=(id, empname, mobile, salary))
        mysqldb.close()


def search():
    for item in listBox.get_children():
        listBox.delete(item)
    studid = e1.get()

    mysqldb = my.connect(host='localhost', user='root', password='root', database='payroll_b2')
    mycursor = mysqldb.cursor()
    mycursor.execute("select * from registration where id = '" + studid + "'")
    records = mycursor.fetchall()
    print(type(records))
    print(len(records))
    if len(records) == 1:
        print(records)
        for i, (id, emname, contact, sal) in enumerate(records, start=0):
            listBox.insert("", 'end', values=(id, emname, contact, sal))
            mysqldb.close()
    #
    else:
        messagebox.showwarning("Input error", "Id not found")



def clear_all():
    for item in listBox.get_children():
        listBox.delete(item)


root = Tk()
root.geometry('820x500')
root.title('Employee Hub')
root.configure(bg='#2a3c4a')
global e1
global e2
global e3
global e4

tk.Label(root, text='EMPLOYEE REGISTRATION', bg='#2a3c4a', fg='#cad6eb', font=('Bahnschrift light', 27, 'bold')).place(
    x=320, y=20)
tk.Label(root, text='PORTAL', bg='#2a3c4a', fg='#cad6eb', font=('Bahnschrift light', 27, 'bold')).place(
    x=450, y=63)
tk.Label(root, text="Employee Id", bg='#2a3c4a', fg='#cad6eb', font=('Bahnschrift light', 10, 'bold')).place(x=10, y=10)
tk.Label(root, text="Employee name", bg='#2a3c4a', fg='#cad6eb', font=('Bahnschrift light', 10, 'bold')).place(x=10,
                                                                                                               y=40)
tk.Label(root, text="Mobile", bg='#2a3c4a', fg='#cad6eb', font=('Bahnschrift light', 10, 'bold')).place(x=10, y=70)
tk.Label(root, text="Salary", bg='#2a3c4a', fg='#cad6eb', font=('Bahnschrift light', 10, 'bold')).place(x=10, y=100)

e1 = Entry(root, bg='#2d73a8')
e1.place(x=140, y=10)

e2 = Entry(root, bg='#2d73a8')
e2.place(x=140, y=40)

e3 = Entry(root, bg='#2d73a8')
e3.place(x=140, y=70)

e4 = Entry(root, bg='#2d73a8')
e4.place(x=140, y=100)

Button(root, text="ADD", command=Add, height=3, width=13, bg='#2d73a8', font=('Bahnschrift light', 10, 'bold'),
       borderwidth=10).place(x=30, y=140)
Button(root, text="UPDATE", command=update, height=3, width=13, bg='#2d73a8',
       font=('Bahnschrift light', 10, 'bold'), borderwidth=10).place(x=180, y=140)
Button(root, text="DELETE", command=delete, height=3, width=13, bg='#2d73a8',
       font=('Bahnschrift light', 10, 'bold'), borderwidth=10).place(x=330, y=140)
# Button(root, text='SHOW', command=show, height=3, width=13, bg='#2d73a8', font=('Bahnschrift light', 10, 'bold')).place(+
#     x=680, y=140)
Button(root, text='SEARCH', command=search, height=3, width=13, bg='#2d73a8',
       font=('Bahnschrift light', 10, 'bold'), borderwidth=10).place(x=480, y=140)

Button(root, text='CLEAR', command=clear_all, height=3, width=13, bg='#2d73a8',
       font=('Bahnschrift light', 10, 'bold'), borderwidth=10).place(x=480 + 150, y=140)

cols = ('Identity Number', 'Emp Name', 'Contact', 'Salary')
listBox = ttk.Treeview(root, columns=cols, show='headings', height=11)
for col in cols:
    listBox.heading(col, text=col)
listBox.grid(row=1, column=0, columnspan=2)

listBox.place(x=10, y=230)
show()
listBox.bind('<Double-Button-1>', getValue)
root.mainloop()
