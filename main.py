from tkinter import *
import random
from tkinter import messagebox


def new():
    import sqlite3
    import os
    import random
    window = Tk()
    window.geometry("600x300")
    window.configure(bg="cyan")
    window.title("LOGIN")

    def login():          #login function

        def login_database():
            conn = sqlite3.connect("1.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM test WHERE email=? AND password=?", (e1.get(), e2.get()))
            row = cur.fetchall()
            conn.close()
            print(row)
            if row != []:
                user_name = row[0][1]
                l3.config(text="User name found with name: " + user_name)
                window.destroy()
                login_window.destroy()


            else:
                l3.config(text="User not found ")

        login_window = Tk()

        login_window.geometry("500x450")
        login_window.configure(bg="Light Blue")
        l1 = Label(login_window, text="EMAIL", font=('Times', 16, 'bold'), bg="Light Blue")
        l1.place(x=10, y=50)
        l2 = Label(login_window, text="PASSWORD", font=('Times', 16, 'bold'), bg="Light Blue")
        l2.place(x=10, y=100)
        l3 = Label(login_window, font=('Times', 16, 'bold'), bg="Light Blue")
        l3.place(x=50, y=300)

        email_text = StringVar()
        e1 = Entry(login_window, textvariable=email_text, font=('Times', 16, 'bold'), bg="Light Blue")
        e1.place(x=200, y=50)
        password_text = StringVar()
        e2 = Entry(login_window, textvariable=password_text , font=('Times', 16, 'bold'), bg="Light Blue")
        e2.place(x=200, y=100)

        b1 = Button(login_window, text="login", width=20, font=('Times', 16, 'bold'), bg="yellow",
                    command=login_database)
        b1.place(x=100, y=200)
        login_window.mainloop()

    def signup():

        def signup_database():
            conn = sqlite3.connect("1.db")
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY,name text,email text, password text)")
            cur.execute("INSERT INTO test Values(Null,?,?,?)", (e1.get(), e2.get(), e3.get()))
            l4 = Label(signup_window, text="account created", font="times 15")
            l4.grid(row=6, column=2)
            conn.commit()
            conn.close()

        signup_window = Tk()
        signup_window.geometry("600x400")
        signup_window.configure(bg="Light Blue")
        l1 = Label(signup_window, text="USE NAME", font="times 25", bg="Light Blue")
        l1.grid(row=1, column=1)
        l2 = Label(signup_window, text="USER EMAIL", font="times 25", bg="Light Blue")
        l2.grid(row=2, column=1)
        l3 = Label(signup_window, text="USER PASSWORD", font="times 25", bg="Light Blue")
        l3.grid(row=3, column=1)

        name_text = StringVar()
        e1 = Entry(signup_window, textvariable=name_text, font=('Times', 16, 'bold'))
        e1.grid(row=1, column=2)
        email_text = StringVar()
        e2 = Entry(signup_window, textvariable=email_text, font=('Times', 16, 'bold'))
        e2.grid(row=2, column=2)
        password_text = StringVar()
        e3 = Entry(signup_window, textvariable=password_text, font=('Times', 16, 'bold'))
        e3.grid(row=3, column=2)

        b1 = Button(signup_window, text="login", width=20, font=('Times', 16, 'bold'), bg="yellow",
                    command=signup_database)
        b1.grid(row=4, column=1)
        window.mainloop()

    def contact():
        root = Tk()
        root.geometry("500x400")
        root.title("Login")
        root.resizable(0, 0)
        h1 = Label(root, text="Contact Us", fg="Light Blue", font=('arial', 30, "bold"), bd=15).pack(side=TOP)
        h1 = Label(root, text="Name:", fg="black", font=('arial', 20, "bold"), bd=15).place(x=130, y=130, anchor=CENTER)
        h2 = Label(root, text="Vibhuti raj", fg="yellow", font=('arial', 20, "bold"), bd=15).place(x=240, y=130,
                                                                                                anchor=CENTER)
        h2 = Label(root, text="Mobile No:", fg="black", font=('arial', 20, "bold"), bd=15).place(x=130, y=190,
                                                                                                 anchor=CENTER)
        h3 = Label(root, text="9092290329", fg="yellow", font=('arial', 20, "bold"), bd=15).place(x=290, y=190,
                                                                                                     anchor=CENTER)
        h3 = Label(root, text="Email:", fg="black", font=('arial', 20, "bold"), bd=15).place(x=70, y=250, anchor=CENTER)
        h4 = Label(root, text="vibse@gmail.com", fg="yellow", font=('arial', 20, "bold"), bd=15).place(
            x=310, y=250, anchor=CENTER)
        root.mainloop()

    l1 = Label(window, text="User login", font="times 30")
    l1.grid(row=1, column=2, columnspan=2)

    b1 = Button(window, text="LOGIN", width=20, font=('Times', 16, 'bold'), command=login, bg="yellow")
    b1.grid(row=5, column=2)

    b2 = Button(window, text="SIGNUP", width=20, font=('Times', 16, 'bold'), command=signup, bg="yellow")
    b2.grid(row=5, column=3)
    b3 = Button(window, text="Contact us", width=20, font=('Times', 16, 'bold'), command=contact, bg="yellow")
    b3.grid(row=6, column=2)
    b4 = Button(window, text="EXIT", width=20, font=('Times', 16, 'bold'), command=window.destroy, bg="yellow")
    b4.grid(row=6, column=3)

    window.mainloop()


new()
root = Tk()
root.geometry("1600x8000")
root.title("shop")
root.configure(bg='Light Blue')
Tops = Frame(root, width=1600)
Tops.pack()

f1 = Frame(root, width=800, height=700, relief=SUNKEN, bg="Light Blue")
f1.pack()

lblInfo = Label(Tops, font=('Times', 50, 'bold'), text="Shop in a dash !", fg="Black", bg="bisque2", bd=15,
                anchor='w')
lblInfo.grid(row=0, column=0)




def Ref():
    x = random.randint(10908, 500876)
    randomRef = str(x)
    rand.set(randomRef)
    print(x)

    if (Mob1.get() == ""):
        CoMob1 = 0
    else:
        CoMob1 = float(Mob1.get())

    if (Mob2.get() == ""):
        CoMob2 = 0
    else:
        CoMob2 = float(Mob2.get())

    if (Mob3.get() == ""):
        CoMob3 = 0
    else:
        CoMob3 = float(Mob3.get())

    if (Mob5.get() == ""):
        CoMob5 = 0
    else:
        CoMob5 = float(Mob5.get())

    if (t1.get() == ""):
        Cot1 = 0
    else:
        Cot1 = float(t1.get())

    if (t2.get() == ""):
        Cot2 = 0
    else:
        Cot2 = float(t2.get())

    if (Mob4.get() == ""):
        CoD = 0
    else:
        CoD = float(Mob4.get())

    if (t3.get() == ""):
        Cot3 = 0
    else:
        Cot3 = float(t3.get())

    if (t4.get() == ""):
        Cot4 = 0
    else:
        Cot4 = float(t4.get())

    if (t5.get() == ""):
        Cot5 = 0
    else:
        Cot5 = float(t5.get())

    if (t6.get() == ""):
        Cot6 = 0
    else:
        Cot6 = float(t6.get())

    if (w2.get() == ""):
        Cow2 = 0
    else:
        Cow2 = float(w2.get())

    if (w3.get() == ""):
        Cow3 = 0
    else:
        Cow3 = float(w3.get())

    if (w4.get() == ""):
        Cow4 = 0
    else:
        Cow4 = float(w4.get())

    if (w5.get() == ""):
        Cow5 = 0
    else:
        Cow5 = float(w5.get())

    CostofMob1 = CoMob1 * 40000
    CostofMob4 = CoD * 130000
    CostofMob2 = CoMob2 * 23999
    CostofMob3 = CoMob3 * 14999
    CostMob5 = CoMob5 * 17999
    Costt1 = Cot1 * 900
    Costoft2 = Cot2 * 999
    Costoft3 = Cot3 * 3990
    Costoft4 = Cot4 * 4999
    Costoft5 = Cot5 * 399
    Costoft6 = Cot6 * 998
    Costofw2 = Cow2 * 16990
    Costofw3 = Cow3 * 54099
    Costofw4 = Cow4 * 21999
    Costofw5 = Cow5 * 7999

    CostofItem = "Rs", str('%.2f' % (
                CostofMob1 + CostofMob4 + CostofMob2 + CostofMob3 + CostMob5 + Costt1 + Costoft2 + Costoft3 + Costoft4 + Costoft5 + Costoft6 + Costofw2 + Costofw3 + Costofw4 + Costofw5))

    PayTax = ((
                          CostofMob1 + CostofMob4 + CostofMob2 + CostofMob3 + CostMob5 + Costt1 + Costoft2 + Costoft3 + Costoft4 + Costoft5 + Costoft6 + Costofw2 + Costofw3 + Costofw4 + Costofw5) * 0.05)

    TotalCost = (
                CostofMob1 + CostofMob4 + CostofMob2 + CostofMob3 + CostMob5 + Costt1 + Costoft2 + Costoft3 + Costoft4 + Costoft5 + Costoft6 + Costofw2 + Costofw3 + Costofw4 + Costofw5)

    OverAllCost = "Rs", str('%.2f' % (PayTax + TotalCost))

    PaidTax = "Rs", str('%.2f' % PayTax)

    Cost.set(CostofItem)
    Tax.set(PaidTax)
    Total.set(OverAllCost)


def qExit():
    root.destroy()


def Reset():
    rand.set("")
    Mob1.set("")
    Mob2.set("")
    Mob3.set("")
    Total.set("")
    Mob4.set("")
    Tax.set("")
    Cost.set("")
    Mob5.set("")
    t1.set("")
    t2.set("")
    t3.set("")
    t4.set("")
    t5.set("")
    t6.set("")
    w2.set("")
    w3.set("")
    w4.set("")
    w5.set("")


rand = StringVar()
Mob1 = StringVar()
Mob2 = StringVar()
Mob3 = StringVar()
Total = StringVar()
Mob4 = StringVar()
Tax = StringVar()
Cost = StringVar()
Mob5 = StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()
t6 = StringVar()
w2 = StringVar()
w3 = StringVar()
w4 = StringVar()
w5 = StringVar()

import sqlite3


def database():
    n1 = rand.get()
    n2 = Mob1.get()
    n3 = Mob2.get()
    n4 = Mob3.get()
    n5 = Mob4.get()
    n6 = Mob5.get()
    n7 = t1.get()
    n8 = t2.get()
    n9 = t3.get()
    n10 = t4.get()
    n11 = t5.get()
    n12 = t6.get()
    n13 = w2.get()
    n14 = w3.get()
    n15 = w4.get()
    n16 = w5.get()
    conn = sqlite3.connect("re2.db")
    # conn.execute("create table Lis(rand varchar(50), Mob1 varchar(50), Mob2  varchar(50), Mob3 varchar(50), Mob4  varchar(50),Mob5  varchar(50),t1  varchar(50),t2 varchar(50),t3 varchar(50),t4 varchar(50),t5 varchar(50),t6 varchar(50),w2 varchar(50),w3 varchar(50),w4 varchar(50),w5 varchar(50));")
    conn.execute(
        "insert into Lis(rand,Mob1,Mob2,Mob3,Mob4,Mob5,t1,t2,t3,t4,t5,t6,w2,w3,w4,w5)values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16,))
    c = conn.execute("select * from Lis ")
    for i in c:
        print("n1", i[0])
        print("n2", i[1])
        print("n3", i[2])
        print("n4", i[3])
        print("n5", i[4])
        print("n6", i[5])
        print("n7", i[6])
        print("n8", i[7])
        print("n9", i[8])
        print("n10", i[9])
        print("n11", i[10])
        print("n12", i[11])
        print("n13", i[12])
        print("n14", i[13])
        print("n15", i[14])
        print("n16", i[15])
        conn.commit()


def wish():
    def qui():
        allwin.destroy()

    allwin = Tk()
    allwin.title("CART")
    allwin.geometry("1000x550")
    allwin.configure(bg='Light Blue')
    Label(allwin, text="PAYMENT DONE!", bg="Light Blue", font=('Times', 40, 'bold')).place(x=200, y=0)
    t = Text(allwin)
    conn = sqlite3.connect("re2.db")
    for i in conn.execute('SELECT * FROM Lis'):
        t.insert(INSERT, i)
        t.insert(INSERT, '\n')

    t.pack()
    Button(allwin, padx=16, pady=8, bd=16, fg="black", font=('Times', 16, 'bold'), width=10, text="PAY", bg="yellow",
           command=paymnt).place(x=280, y=430)
    Button(allwin, padx=16, pady=8, bd=16, fg="black", font=('Times', 16, 'bold'), width=10, text="EXIT",
           bg="yellow", command=qui).place(x=600, y=430)


def paymnt():
    window = Tk()
    window.geometry("1100x800")
    window.configure(bg='Light Blue')



    def pay():
        messagebox.showinfo("PAYMENT DONE", "Payment Successfull")
        window.destroy()


    Label(window, text="PAYMENT", bg="Light Blue", font=('Times', 40, 'bold')).place(x=200, y=0)
    Label(window, font=('Times', 16, 'bold'), text="NAME", bd=16, bg="Light Blue", anchor="w").place(x=0, y=100)

    Entry(window, font=('Times', 10, 'bold'), bd=10, insertwidth=2, bg="Light Green", justify='right').place(x=250, y=100)

    Label(window, font=('Times', 16, 'bold'), text="ADDRESS", bd=16, bg="Light Blue", anchor="w").place(x=0, y=200)

    Entry(window, font=('Times', 10, 'bold'), bd=10, insertwidth=2, bg="Light Green", justify='right').place(x=250, y=200)

    Label(window, font=('Times', 16, 'bold'), text="MOBILE NUMBER", bd=16, bg="Light Blue", anchor="w").place(x=0,
                                                                                                               y=300)

    Entry(window, font=('Times', 10, 'bold'), bd=10, insertwidth=2, bg="Light Green", justify='right').place(x=250, y=300)
    Label(window, font=('Times', 16, 'bold'), text="UPI ID", bd=16, bg="Light Blue", anchor="w").place(x=0, y=400)

    Entry(window, font=('Times', 10, 'bold'), bd=10, insertwidth=2, bg="Light Green", justify='right').place(x=250, y=400)
    Button(window, padx=16, pady=8, bd=16, fg="black", font=('Times', 16, 'bold'), width=10, text="PAY", bg="yellow",
           command=pay).place(x=500, y=200)

    Button(window, padx=16, pady=8, bd=16, fg="black", font=('Times', 16, 'bold'), width=10, text="EXIT",
           bg="yellow", command=exit).place(x=500, y=300)



lblReference = Label(f1, font=('Times', 16, 'bold'), text="ORDER ID", bd=16, bg="Light Blue", anchor="w")
lblReference.grid(row=0, column=0)
txtReference = Entry(f1, font=('Times', 10, 'bold'), textvariable=rand, bd=10, insertwidth=2, bg="Light Green",
                     justify='right')
txtReference.grid(row=0, column=1)

lblMob1 = Label(f1, font=('Times', 16, 'bold'), text="Oneplus 7t", bd=16, bg="Light Blue", anchor="w")
lblMob1.grid(row=1, column=0)
txtMob1 = Entry(f1, font=('Times', 10, 'bold'), textvariable=Mob1, bd=10, insertwidth=2, bg="Light Green", justify='right')
txtMob1.grid(row=1, column=1)

lblMob2 = Label(f1, font=('Times', 16, 'bold'), text="iphone 13 ", bd=16, bg="Light Blue", anchor="w")
lblMob2.grid(row=2, column=0)
txtMob2 = Entry(f1, font=('Times', 10, 'bold'), textvariable=Mob2, bd=10, insertwidth=2, bg="Light Green",
                   justify='right')
txtMob2.grid(row=2, column=1)

lblMob3 = Label(f1, font=('Times', 16, 'bold'), text="poco X2", bd=16, bg="Light Blue", anchor="w")
lblMob3.grid(row=3, column=0)
txtMob3 = Entry(f1, font=('Times', 10, 'bold'), textvariable=Mob3, bd=10, insertwidth=2, bg="Light Green", justify='right')
txtMob3.grid(row=3, column=1)

lblMob5 = Label(f1, font=('Times', 16, 'bold'), text="Redmi Note 10 ", bd=16, bg="Light Blue", anchor="w")
lblMob5.grid(row=4, column=0)
txtMob5 = Entry(f1, font=('Times', 10, 'bold'), textvariable=Mob5, bd=10, insertwidth=2, bg="Light Green", justify='right')
txtMob5.grid(row=4, column=1)

lblt1 = Label(f1, font=('Times', 16, 'bold'), text="Samsung S21", bd=16, bg="Light Blue", anchor="w")
lblt1.grid(row=5, column=0)
txtt1 = Entry(f1, font=('Times', 10, 'bold'), textvariable=t1, bd=10, insertwidth=2, bg="Light Green",
                    justify='right')
txtt1.grid(row=5, column=1)

lblMob4 = Label(f1, font=('Times', 16, 'bold'), text="adidas tshirt", bd=16, bg="Light Blue", anchor="w")
lblMob4.grid(row=0, column=2)
txtMob4 = Entry(f1, font=('Times', 10, 'bold'), textvariable=Mob4, bd=10, insertwidth=2, bg="Light Green", justify='right')
txtMob4.grid(row=0, column=3)

lblt2 = Label(f1, font=('Times', 16, 'bold'), text="puma tshirt", bd=16, bg="Light Blue", anchor="w")
lblt2.grid(row=1, column=2)
txtt2 = Entry(f1, font=('Times', 10, 'bold'), textvariable=t2, bd=10, insertwidth=2, bg="Light Green", justify='right')
txtt2.grid(row=1, column=3)

lblt3 = Label(f1, font=('Times', 16, 'bold'), text="Reebok tshirt", bd=16, bg="Light Blue", anchor="w")
lblt3.grid(row=2, column=2)
txtt3 = Entry(f1, font=('Times', 10, 'bold'), textvariable=t3, bd=10, insertwidth=2, bg="Light Green", justify='right')
txtt3.grid(row=2, column=3)

lblt4 = Label(f1, font=('Times', 16, 'bold'), text="Gant tshirt", bd=16, bg="Light Blue", anchor="w")
lblt4.grid(row=3, column=2)
txtt4 = Entry(f1, font=('Times', 10, 'bold'), textvariable=t4, bd=10, insertwidth=2, bg="Light Green", justify='right')
txtt4.grid(row=3, column=3)

lblt5 = Label(f1, font=('Times', 16, 'bold'), text="uspa thsirt", bd=16, bg="Light Blue", anchor="w")
lblt5.grid(row=4, column=2)
txtt5 = Entry(f1, font=('Times', 10, 'bold'), textvariable=t5, bd=10, insertwidth=2, bg="Light Green",
                   justify='right')
txtt5.grid(row=4, column=3)

lblt6 = Label(f1, font=('Times', 16, 'bold'), text="wrangler tshirt", bd=16, bg="Light Blue", anchor="w")
lblt6.grid(row=5, column=2)
txtt6 = Entry(f1, font=('Times', 10, 'bold'), textvariable=t6, bd=10, insertwidth=2, bg="Light Green",
                   justify='right')
txtt6.grid(row=5, column=3)

lblw2 = Label(f1, font=('Times', 16, 'bold'), text="samsung washingm", bd=16, bg="Light Blue", anchor="w")
lblw2.grid(row=0, column=4)
txtw2 = Entry(f1, font=('Times', 10, 'bold'), textvariable=w2, bd=10, insertwidth=2, bg="Light Green",
                     justify='right')
txtw2.grid(row=0, column=5)

lblw3 = Label(f1, font=('Times', 16, 'bold'), text="lg washingm", bd=16, bg="Light Blue", anchor="w")
lblw3.grid(row=1, column=4)
txtw3 = Entry(f1, font=('Times', 10, 'bold'), textvariable=w3, bd=10, insertwidth=2, bg="Light Green", justify='right')
txtw3.grid(row=1, column=5)

lblw4 = Label(f1, font=('Times', 16, 'bold'), text="whirpool washingm", bd=16, bg="Light Blue", anchor="w")
lblw4.grid(row=2, column=4)
txtw4 = Entry(f1, font=('Times', 10, 'bold'), textvariable=w4, bd=10, insertwidth=2, bg="Light Green",
                   justify='right')
txtw4.grid(row=2, column=5)

lblw5 = Label(f1, font=('Times', 16, 'bold'), text="amaz washingm", bd=16, bg="Light Blue", anchor="w")
lblw5.grid(row=3, column=4)
txtw5 = Entry(f1, font=('arial', 10, 'bold'), textvariable=w5, bd=10, insertwidth=2, bg="Light Green",
                     justify='right')
txtw5.grid(row=3, column=5)

lblCost = Label(f1, font=('Times', 16, 'bold'), text="COST OF ITEMS", bd=16, bg="Light Blue", anchor="w")
lblCost.grid(row=6, column=0)
txtCost = Entry(f1, font=('Times', 16, 'bold'), textvariable=Cost, bd=10, insertwidth=2, bg="Light Green", justify='right')
txtCost.grid(row=6, column=1)

lblStateTax = Label(f1, font=('Times', 16, 'bold'), text="GST", bd=16, bg="Light Blue", anchor="w")
lblStateTax.grid(row=6, column=2)
txtStateTax = Entry(f1, font=('Times', 16, 'bold'), textvariable=Tax, bd=10, insertwidth=2, bg="Light Green", justify='right')
txtStateTax.grid(row=6, column=3)

lblTotalCost = Label(f1, font=('Times', 16, 'bold'), text="TOTAL COST", bd=16, bg="Light Blue", anchor="w")
lblTotalCost.grid(row=6, column=4)
txtTotalCost = Entry(f1, font=('Times', 16, 'bold'), textvariable=Total, bd=10, insertwidth=2, bg="Light Green",
                     justify='right')
txtTotalCost.grid(row=6, column=5)

btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('Times', 16, 'bold'), width=10, text="TOTAL",
                  bg="yellow", command=Ref).grid(row=9, column=0, padx=5, pady=30)
btnTally = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('Times', 16, 'bold'), width=10, text="CART",
                  bg="yellow", command=database).grid(row=9, column=1, padx=5, pady=30)
btnReset = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('Times', 16, 'bold'), width=10, text="RESET",
                  bg="yellow", command=Reset).grid(row=9, column=2, padx=5, pady=30)

btnmv = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('Times', 16, 'bold'), width=13, text="PAY",
                 bg="yellow", command=wish).grid(row=9, column=3, padx=5, pady=30)
btnExit = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('Times', 16, 'bold'), width=11, text="EXIT",
                 bg="yellow", command=qExit).grid(row=9, column=4, padx=5, pady=30)


root.mainloop()