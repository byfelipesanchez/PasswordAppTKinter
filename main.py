from cgitb import text
from distutils import command
from json.tool import main
import sqlite3, hashlib
from tkinter import *
from tkinter import font
from tkinter import simpledialog
from functools import partial
import smtplib #todo: email sender when complete login



#database code

with sqlite3.connect('database.db') as db:
    c = db.cursor()

    c.execute('CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY, site_name TEXT NOT NULL, username TEXT NOT NULL, password TEXT NOT NULL)')


def pop_up(text):
    answer = simpledialog.askstring("input string", text)

    return answer

def delete_popup():
    abc = simpledialog.askstring("DELETE?", text)

    
#app

window = Tk()
window.title("password application")

# def hash_passwords():
#     hash = hashlib.md5(input)
#     hash = hash.hexdigest()

def loginScreen():
    
    window.geometry("1350x1200")
    lbl = Label(window, text=" password", font=("Arial, Bold", 20))
    lbl.config(anchor=CENTER)
    lbl.pack(pady = 15)

    txt = Entry(window, width=20, show="*")
    txt.pack(pady=10)
    txt.focus()

    lbl1 = Label(window, text='check password', font=("Arial, Bold", 20))
    lbl1.pack()

    txt1 = Entry(window, width=20, show="*")
    txt1.pack(pady=10)
    
    def checkPassword():
        password = "test"

        if password == txt.get():
            secondPassword()
            print("Correct")
        else:
            quit()

    btn = Button(window, text='Continue', font=("Arial, Bold", 20), command=checkPassword)
    btn.pack(pady=15)

#TODO: add button that, if pressed, quits and emails me


def secondPassword():
    for widegt in window.winfo_children():
        widegt.destroy()
    window.geometry("1350x1200")

    lbl = Label(window, text="Enter Second Password", font=("Arial Bold", 20))
    lbl.config(anchor=CENTER)
    lbl.pack(pady = 15)

    txt = Entry(window, width=20, show="*")
    txt.pack()
    txt.focus()

    lbl1 = Label(window)
    lbl1.pack()

    def checkPassword():
        password = "test"

        if password == txt.get():
            birthdayScreen()
            print("Correct")
        else:
            lbl1.config(text="Incorrect Password")
            quit()

    btn = Button(window, text='Continue', font=("Arial, Bold", 20), command=checkPassword)
    btn.pack(pady=15)


def birthdayScreen():
    for widegt in window.winfo_children():
        widegt.destroy()
    window.geometry("1350x1200")

    lbl = Label(window, text="When's my birthday? (DD/MM/YYYY)", font=("Arial Bold", 20))
    lbl.config(anchor=CENTER)
    lbl.pack(pady = 15)

    txt = Entry(window, width=20, show="*")
    txt.pack()
    txt.focus()

    lbl1 = Label(window)
    lbl1.pack()

    def check_password():
        password = "17/06/2004"

        if password == txt.get():
            mainScreen()
            print("Correct")
        else:
            lbl1.config(text="Incorrect Password")
            quit()

    btn = Button(window, text='Continue', font=("Arial, Bold", 20), command=check_password)
    btn.pack(pady=15)


def mainScreen():
    for widget in window.winfo_children():
        widget.destroy()

    def add_entry():
        text1 = "Website Name"
        text2 = "Username"
        text3 = "Password"

        website = pop_up(text1)
        username = pop_up(text2)
        password = pop_up(text3)

        insert_fields = '''INSERT INTO passwords(site_name, username, password) VALUES(?,?,?)'''

        c.execute(insert_fields, (website, username, password))
        db.commit()

        mainScreen()

    def remove_entry(input):
        delete_popup()
        c.execute('DELETE FROM passwords WHERE id=?', (input,))
        db.commit()
        mainScreen()


    window.geometry("1350x1200")

    lbl = Label(window, text=f"Here Are Your Passwords", font=("Arial Bold ", 20 ), padx= 20, pady=10)
    lbl.grid(column = 1 )
    # lbl.pack(pady = 15)

    btn = Button(window, text="Add", command = add_entry)
    btn.grid(column=1, pady=10)
    # btn.pack(pady=50)

    lbl = Label(window, text="Website Name")
    lbl.grid(row=2, column=0, padx=88)
    lbl = Label(window, text="Username")
    lbl.grid(row=2, column=1, padx=88)
    lbl = Label(window, text="Password")
    lbl.grid(row=2, column=2, padx=88)

    c.execute("SELECT * FROM passwords")
    if(c.fetchall() != None):
        i = 0
        while True:
            c.execute("SELECT * FROM passwords")
            array = c.fetchall()

            lbl1 = Label(window, text=(array[i][1]), font=('Arial', 10))
            lbl1.grid(row=i+3, column=0, padx=88)
            lbl1 = Label(window, text=(array[i][2]), font=('Arial', 10))
            lbl1.grid(row=i+3, column=1, padx=88)
            lbl1 = Label(window, text=(array[i][3]), font=('Arial', 10))
            lbl1.grid(row=i+3, column=2, padx=88)

            btn = Button(window, text="Delete", command=partial(remove_entry, array[i][0]))
            btn.grid(row=i+3, column=3, pady=10)

            i += 1
            c.execute( "SELECT * FROM passwords")
            if len(c.fetchall()) <=i:
                break


loginScreen()
window.mainloop()