import tkinter
from tkinter import *
import tkinter.messagebox
import csv
import uuid

from library import back


class kol:
    y = Tk()
    y.geometry("350x250")
    y.title("Library_prototype")

    ID = StringVar()
    Book_name = StringVar()
    student_name = StringVar()
    student_class = StringVar()
    amount = StringVar()

    def idi():
        id = uuid.uuid4()
        tkinter.messagebox.showinfo("ID", id.node)

    button5 = Button(y, text="Get ID", command=idi, relief=RIDGE)
    button5.grid(row=2, column=1)

    def issue():
        x = Tk()
        lab1 = Label(x, text="Enter ID")
        lab1.grid(row=7, column=1)
        entry_text = tkinter.StringVar()
        entry17 = Entry(x, width=30)
        entry17.grid(row=7, column=2)
        entry17.config(text=uuid.uuid4().node)
        lab = Label(x, text="Enter the Book name")
        lab.grid(row=3, column=1)
        entry1 = Entry(x, width=30)
        entry1.grid(row=3, column=2)
        # nentry1=entry1.get()
        lab = Label(x, text="Enter the Student Name")
        lab.grid(row=4, column=1)
        entry2 = Entry(x, width=30)
        entry2.grid(row=4, column=2)
        # nentry2=entry2.get()

        lab = Label(x, text="Enter Student's Class ")
        lab.grid(row=5, column=1)
        entry3 = Entry(x, width=30)
        entry3.grid(row=5, column=2)
        # nentry3=entry3.get()

        lab = Label(x, text="Amount Deposited")
        lab.grid(row=6, column=1)
        entry4 = Entry(x, width=30)
        entry4.grid(row=6, column=2)

        # nentry=entry4.get()
        def get():
            back.add(entry17.get(), entry1.get(), entry2.get(), entry3.get(), entry4.get())

        button3 = Button(x, text="SAVE", command=get, relief=RIDGE)
        button3.grid(row=8, column=1)
        x.mainloop()

    button1 = Button(y, text="ISSUE BOOK", command=issue, relief=GROOVE, bd=5, height=2, width=11)
    button1.grid(row=1, column=1)

    def search():
        x = Tk()
        lab = Label(x, text="Enter Student Name")
        lab.grid(row=6, column=1)
        entry5 = Entry(x, width=30)
        entry5.grid(row=6, column=2)
        back.display(entry5.get())
        T = Text(x, height=2, width=30)
        T.grid(row=8, column=3)

        def disp():
            print('in main disp')
            back.display(entry5.get())
            for v in back.display():
                print(v)

            T.insert(END, v, str(""))

        button4 = Button(x, text="show result", command=disp, relief=GROOVE, bd=5, height=2, width=11)
        button4.grid(row=10, column=1)
        x.mainloop()

    button2 = Button(y, text="SEARCH", command=search, relief=RAISED, bd=5, height=2, width=11)
    button2.grid(row=1, column=2)

    y.mainloop()
