from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
def main_account_screen(usrname, pwd):
    try:
        flag = 0            # to check if the database is already present
        con = mysql.connector.connect(host='localhost', user=usrname, password=pwd) # connect to the mySql server
        cur = con.cursor(buffered = True)
        cur.execute("SHOW DATABASES")                 # get a list of all the databases present in the server
        for x in cur.fetchall():
            for y in x:
                if y == 'gas_booking':             # check if the required the database is present
                    flag = 1
                    break
        if flag != 1:                                   # if not present then create database and table and make a connection and cursor to it
            cur.execute("CREATE DATABASE gas_booking")
            con = mysql.connector.connect(host='localhost', user=usrname, password=pwd, database='gas_booking')
            cur = con.cursor(buffered = True)
            cur.execute("CREATE TABLE user_detail(phone_number INT, user_name varchar(50), user_pass varchar(50));")
        else:                               # otherwise just connect to that database and create a cursor
            con = mysql.connector.connect(host='localhost', user=usrname, password=pwd, database='gas_booking')
            cur = con.cursor(buffered = True)

        main_screen=Tk()# create a GUI window
        main_screen.geometry("300x250") # set the configuration of GUI window
        main_screen.config(bg="pink")
        main_screen.title("Account Login") # set the title of GUI window
        Label(text="WELCOME TO GAS BOOKING SYSTEM", bg="blue",fg="black", width="300", height="2", font=("Calibri", 13)).pack()
        Label(text="").pack()
        def correctdig(inp):
            if inp.isdigit():
                return True
            elif inp=="":
                return True
            else:
                return False
        def home():
                global home_screen
                home_screen = Toplevel()
                home_screen.title("HOME")
                home_screen.geometry("500x450")
                home_screen.config(bg="green")

                Label(home_screen, text="HOME SCREEN",bg="lightblue",fg="green", font=("Times new roman", 16)).pack()

                def stove_connection():
                    screen = Toplevel()
                    screen.title("stove connection")
                    screen.geometry("500x450")
                    screen.config(bg="yellow")
                    Label(screen,text="Book your Gas stove",fg="black",bg="blue" ,width="300", height="2", font=("Calibri", 13)).pack()

                    consumer=StringVar()

                    consumer_lable= Label(screen, text="consumer code",bg="yellow",fg="blue").pack()

                    consumer_entry = Entry(screen,textvariable= consumer)
                    consumer_entry.pack()
                    geg= screen.register(correctdig)
                    consumer_entry.config(validate="key",validatecommand=(geg,'%P'))
                    def action():
                        username = username_verify.get()
                        if consumer_c_entry.get() == '':
                            return
                        entered_num = int(consumer_c_entry.get())
                        query = "SELECT phone_number FROM user_detail WHERE user_name = %s"
                        val = (username,)
                        cur.execute(query, val)
                        result = cur.fetchone()
                        if result[0] == entered_num:
                            Label(screen,text="stove connection booked successfully").pack()
                        else:
                            Label(screen1, text="Invalid code").pack()

                    Button(screen,text="submit",bg="white",width=7,height=1,command=action).pack()
                    Label(screen, text="").pack()


                Button(home_screen, text="stove Connection",bg="red", width=13, height=1, command=stove_connection).place(x=200,y=50)

                def refill():
                    screen1 = Toplevel()
                    screen1.title("Refilling")
                    screen1.geometry("500x450")
                    screen1.config(bg="yellow")
                    Label(screen1,text="Book your Gas cylinder",fg="black", width="300", height="2", font=("Calibri", 13)).pack()

                    consumer_c=StringVar()

                    consumer_c_lable= Label(screen1, text="consumer code",bg="yellow",fg="blue").pack()

                    consumer_c_entry = Entry(screen1,textvariable= consumer_c)
                    consumer_c_entry.pack()
                    heg= screen1.register(correctdig)
                    consumer_c_entry.config(validate="key",validatecommand=(heg,'%P'))
                    def reaction():
                        username = username_verify.get()
                        if consumer_c_entry.get() == '':
                            return
                        entered_num = int(consumer_c_entry.get())
                        query = "SELECT phone_number FROM user_detail WHERE user_name = %s"
                        val = (username,)
                        cur.execute(query, val)
                        result = cur.fetchone()
                        if result[0] == entered_num:
                            Label(screen1, text="refill request recorded").pack()
                        else:
                            Label(screen1, text="Invalid code").pack()

                    Button(screen1,text="submit",bg="white",width=7,height=1,command=reaction).pack()
                    Label(screen1, text="").pack()



                Button(home_screen, text="Refill",bg="red", width=13, height=1, command=refill).place(x=200,y=100)

        def correctnam(inp):
            if inp.isalpha():
                return True
            elif inp=="":
                return True
            else:
                return False


        def register():
            register_screen = Toplevel()
            register_screen.title("Register")
            register_screen.geometry("500x450")
            register_screen.config(bg="purple")
            username = StringVar()
            password = StringVar()
            name = StringVar()
            phone_no = StringVar()
            address = StringVar()


            Label(register_screen, text="Please enter details below", bg="blue").pack()
            Label(register_screen, text="").pack()


            name_lable = Label(register_screen, text= "Name",bg="lightgreen",fg="blue")
            name_lable.pack()


            name_entry = Entry(register_screen, textvariable=name)
            name_entry.pack()
            beg= register_screen.register(correctnam)
            name_entry.config(validate="key",validatecommand=(beg,'%P'))

            phone_no_lable = Label(register_screen, text="Phone no.",bg="lightgreen",fg="blue")
            phone_no_lable.pack()
            phone_no.get()

            phone_no_entry = Entry(register_screen, textvariable=phone_no)
            phone_no_entry.pack()
            reg= register_screen.register(correctdig)
            phone_no_entry.config(validate="key",validatecommand=(reg,'%P'))

            address_lable = Label(register_screen, text="Address",bg="lightgreen",fg="blue")
            address_lable.pack()
            address.get()

            address_entry = Entry(register_screen, textvariable=address)
            address_entry.pack()


            username_lable = Label(register_screen, text="Username * ",bg="lightgreen",fg="blue")
            username_lable.pack()
            username.get()

            username_entry = Entry(register_screen, textvariable=username)
            username_entry.pack()


            password_lable = Label(register_screen, text="Password * ",bg="lightgreen",fg="blue")
            password_lable.pack()
            password.get()


            password_entry = Entry(register_screen, textvariable=password, show='*')
            password_entry.pack()


            Label(register_screen, text="").pack()

            def register_user():
                username_info = username.get()
                password_info = password.get()
                name_info = name.get()
                phone_no_info = phone_no.get()
                address_info = address.get()

                if (name_info=="" or phone_no_info=="" or address_info==""or username_info==""or password_info==""):
                    Label(register_screen, text="All Fields are required", fg="green", font=("calibri", 11)).pack()
                else:
                    query = "INSERT INTO user_detail values(%s, %s, %s)"
                    values = (phone_no_info, username_info, password_info)
                    cur.execute(query, values)
                    con.commit()
                    success_screen = Toplevel()
                    success_screen.title("success")
                    success_screen.geometry("500x450")
                    success_screen.config(bg="orange")
                    Label(success_screen, text="registered successfully", fg="green", font=("calibri", 11)).pack()
                    Button(success_screen, text="OK", width=10, height=1, bg="blue", command =home).pack()



            Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()

        Button(text="New Customer", height="2", width="30",bg="yellow",fg="red",command=register).pack()
        Label(text="").pack()

        def login():
            login_screen = Toplevel()
            login_screen.title("Login")
            login_screen.geometry("400x350")
            login_screen.config(bg="red")

            Label(login_screen, text="Please enter details below to login").pack()
            Label(login_screen, text="").pack()

            global username_verify
            global password_verify

            username_verify = StringVar()
            password_verify = StringVar()


            Label(login_screen, text="Username * ",bg="lightgreen",fg="blue").pack()

            username_login_entry = Entry(login_screen, textvariable=username_verify)
            username_login_entry.pack()


            Label(login_screen, text="").pack()
            Label(login_screen, text="Password * ",bg="lightgreen",fg="blue").pack()

            password__login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
            password__login_entry.pack()

            Label(login_screen, text="").pack()

            def login_user():
                username_verify_info = username_verify.get()
                password_verify_info = password_verify.get()

                if(username_verify_info=="" or password_verify_info==""):
                    Label(login_screen, text="All Fields are mandatory",bg="lightblue",fg="green").pack()
                else:
                    query = "SELECT user_name, user_pass FROM user_detail WHERE user_name = %s"
                    values = (username_verify_info,)
                    cur.execute(query, values)

                    result = cur.fetchall()
                    if not result or result[0][1] != password_verify_info:
                        Label(login_screen, text="Please check username/password",bg="lightblue",fg="green").pack()
                    else:
                        login_success_screen = Toplevel()
                        login_success_screen.title("Success")
                        login_success_screen.geometry("250x200")
                        login_success_screen.config(bg="lightpink")
                        Label(login_success_screen, text="Login Success",fg="green").pack()
                        Button(login_success_screen, text="OK", width=10, height=1, bg="blue", command =home).pack()

            Button(login_screen, text="Login",bg="blue", width=10, height=1, command=login_user).pack()



        Button(text="Existing Customer", height="2", width="30",bg="yellow",fg="red", command= login).pack()
        main_screen.mainloop()

    except Error as err:
        print(err)
    finally:
        if con.is_connected():  # close the connection after the task is done
            cur.close()
            con.close()
            print('connection is closed')

def getStarted():       # on user click submit in admin windows this function will be called
    pwd = pswd.get()    # get the username and password entered by the user
    usrname = usrnm.get()
    if not usrname:     # use root as username if user doesnt enter username
        usrname = 'root'
    login.destroy()     # destroy the admin window
    main_account_screen(usrname, pwd)

# create a window for logging in
login= Tk(className="Login")
login.configure(bg='green')
login.geometry('370x90')
Label(login, text='Username (default:root) ', font ='time 10 bold', width = 20, anchor='w', bg='yellow').grid(row=1, column=2)
Label(login, text='Password of your sql', font ='time 10 bold', width = 20, anchor='w', bg='yellow').grid(row=2, column=2)
usrnm=Entry(login, width=30)
usrnm.grid(row=1, column=3, padx=10, pady=5)
pswd=Entry(login, width=30)
pswd.grid(row=2, column=3, padx=10, pady=5)
Button(login, text = 'submit', command = getStarted, width = 10, bg='orange').place(x=140, y=60)        # button to submit
login.mainloop()
