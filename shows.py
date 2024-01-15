
from tkinter import *
import random
import datetime
from tkinter import messagebox
import tkinter
import mysql.connector as mys

mys_connect = mys.connect(host="localhost", user="root", password="abcd@1234", database="movie_show_reservation")
mys_cursor = mys_connect.cursor()
query1 = "CREATE TABLE IF NOT EXISTS SHOWS (SHOW_NAME VARCHAR(50), TIME_SLOT VARCHAR(20), DATE INT(20), MONTH VARCHAR(20), SEATS INT(20), AMOUNT INT(20))"
# mys_cursor.execute(query1)

win = Tk()
win.title("Movie Ticket Reservation")
win.geometry("905x605")
win.resizable(0,0)
img = PhotoImage(file="3.png")
label1 = Label(win, image=img).place(x=0, y=0)

a=[""]
var2 = StringVar(value="Select Show")

def get_lang(show):
    show = str(var1.get())
    menu2.config(state = "normal")
    # var2 = StringVar(value="Select Show")
    eng = ["a","b","c"]
    hin = ["d","e","f"]
    if show == "English":
        var2.set(value = "Select Show")
        menu2["menu"].delete(0, "end")
        for x in eng:
            menu2["menu"].add_command(label=x, command=tkinter._setit(var2, x))
    elif show == "Hindi":
        var2.set(value = "Select Show")
        menu2["menu"].delete(0, "end")
        for x in hin:
            menu2["menu"].add_command(label=x, command=tkinter._setit(var2, x))
    menu2["menu"].config(borderwidth=0, fg="White", activeforeground="White", bg="#181d2b", activebackground="#181d2b", font=("Berlin Sans FB", 13))
    '''
    if show == "English":
        menu2 = OptionMenu(win, var2, *eng)
        menu2.config(width=30, height=2, borderwidth=0, highlightthickness=1, fg="White", activeforeground="White", bg="#181d2b", activebackground="#181d2b", font=("Berlin Sans FB", 13))
        menu2["menu"].config(borderwidth=0, fg="White", activeforeground="White", bg="#181d2b", activebackground="#181d2b", font=("Berlin Sans FB", 13))
        menu2.place(x=350, y=270)

    elif show == "Hindi":
        menu2 = OptionMenu(win, var2, *hin)
        menu2.config(width=30, height=2, borderwidth=0, highlightthickness=1, fg="White", activeforeground="White", bg="#181d2b", activebackground="#181d2b", font=("Berlin Sans FB", 13))
        menu2["menu"].config(borderwidth=0, fg="White", activeforeground="White", bg="#181d2b", activebackground="#181d2b", font=("Berlin Sans FB", 13))
        menu2.place(x=350, y=270) 
    '''

def home_screen():
    win.destroy()
    import main

def msg():
    date_user = var0.get()
    user_lang = var1.get()
    show_name = var2.get()
    time_slot = var3.get()
    no_of_seats = var4.get()
    if date_user == "Select Date" or user_lang == "Select Language" or show_name == "Select Show " or time_slot == "Time Slot" or no_of_seats == "Seats":
        messagebox.showwarning(" Warning ! ", "Incomplete Field Found")
    else:
        # amount
        slot = str(var4.get())
        if slot == "12:45 PM" or "1:30 PM":
            prize = 890
        elif slot == "3:15 PM" or "5:20 PM":
            prize = 770
        elif slot == "7:50 PM" or "9:00 PM":
            prize = 1120
        seats = var4.get()
        amt = int(seats)*prize
        gst = int(0.3*amt)
        total_amount = gst + amt
        # query2 = "INSERT INTO MOVIE VALUES("{0}", "{1}", "{2}", "{3}", "{4}", "{5}", "{6}").format(movie_name, format, time_slot, date_usr, month, seats, total_amount)"
        # mys_cursor.execute(query2)
        # mys_connect.commit()
        # print(show_name, no_of_seats,date_user,month_name,time_slot, total_amount)
        var0.set(value = "Select Date")
        var1.set(value = "Select Language")
        var2.set(value = "Select Show")
        menu2.config(state = "disable")
        time_slots = ["12:45 PM", "1:30 PM", "3:15 PM", "5:20 PM", "7:50 PM", "9:00 PM"]
        val = []
        var3.set(value = "Time Slot")
        menu3["menu"].delete(0, "end")
        for j in range(3):
            y = random.choice(time_slots)
            while y in val:
                y = random.choice(time_slots)
                val.append(y)
                val.sort()
            else:
                val.append(y)
            val.sort()
        for new_time_slots in val:
            menu3["menu"].add_command(label=new_time_slots, command=tkinter._setit(var3, new_time_slots))
        menu3["menu"].config(borderwidth=0, fg="White", activeforeground="White", bg="#181d2b", activebackground="#181d2b", font=("Berlin Sans FB", 13))
        var4.set(value = "Seats")
        messagebox.showinfo("Message", "Your Show is Booked")

# date

x = datetime.datetime.now()
year = x.strftime('%Y') # "%Y" getting year like 2022 as string.
month = x.strftime('%m') # "%m" getting month of the year like 02 as string.
current_date = x.strftime('%d') # "%d" getting current date like 01 as string.
month_name = x.strftime('%B') # "%B" getting month name like March.

# inserting the next four days dates in a list so as the user can select one from those dates only.

dates = []
for i in range(1,5):
    next_date = datetime.date.today() + datetime.timedelta(i)
    date = next_date.strftime('%d')
    dates.append(int(date))
var0 = StringVar(value="Select Date")
menu0 = OptionMenu(win, var0, *dates)
menu0.config(width=30, height=2, borderwidth=0, highlightthickness=1, fg="White", activeforeground="White", bg="#181d2b", activebackground="#181d2b", font=("Berlin Sans FB", 13))
menu0["menu"].config(borderwidth=0, fg="White", activeforeground="White", bg="#181d2b", activebackground="#181d2b", font=("Berlin Sans FB", 13))
menu0.place(x=350, y=110)

# language 

val1 = ["English", "Hindi"]
var1 = StringVar(value="Select Language")
menu1 = OptionMenu(win, var1, *val1, command=get_lang)
menu1.config(width=30, height=2, borderwidth=0, highlightthickness=1, fg="White", activeforeground="White", bg="#181d2b", activebackground="#181d2b", font=("Berlin Sans FB", 13))
menu1["menu"].config(borderwidth=0, fg="White", activeforeground="White", bg="#181d2b", activebackground="#181d2b", font=("Berlin Sans FB", 13))
menu1.place(x=350, y=190)

# show

menu2 = OptionMenu(win, var2, *a)
menu2.config(width=30, height=2, borderwidth=0, highlightthickness=1, fg="White", activeforeground="White", bg="#181d2b", activebackground="#181d2b", font=("Berlin Sans FB", 13), state="disable")
menu2["menu"].config(borderwidth=0, fg="White", activeforeground="White", bg="#181d2b", activebackground="#181d2b", font=("Berlin Sans FB", 13))
menu2.place(x=350, y=270)

# time slot

time_slots = ["12:45 PM", "1:30 PM", "3:15 PM", "5:20 PM", "7:50 PM", "9:00 PM"]
val3=[]
for i in range(3):
    x = random.choice(time_slots)
    while x in val3:
        x= random.choice(time_slots)
        val3.append(x)
        val3.sort()
    else:
        val3.append(x)
    val3.sort()
var3 = StringVar(value="Time Slot")
menu3 = OptionMenu(win, var3, *val3)
menu3.config(width=30, height=2, borderwidth=0, highlightthickness=1, fg="White", activeforeground="White", bg="#181d2b", activebackground="#181d2b", font=("Berlin Sans FB", 13))
menu3["menu"].config(borderwidth=0, fg="White", activeforeground="White", bg="#181d2b", activebackground="#181d2b", font=("Berlin Sans FB", 13))
menu3.place(x=350, y=350)

# seats

val4 = ["1","2","3","4"]
var4 = StringVar(value="Seats")
menu4 = OptionMenu(win, var4, *val4)
menu4.config(width=30, height=2, borderwidth=0, highlightthickness=1, fg="White", activeforeground="White", bg="#181d2b", activebackground="#181d2b", font=("Berlin Sans FB", 13))
menu4["menu"].config(borderwidth=0, fg="White", activeforeground="White", bg="#181d2b", activebackground="#181d2b", font=("Berlin Sans FB", 13))
menu4.place(x=350, y=430)

# buttons

btn1 = Button(win, text="< Prev ", fg="white", activeforeground="white", bg="#181d2b", activebackground="#181d2b", relief=FLAT, bd=0, borderwidth=0, highlightthickness=1, font=("Berlin Sans FB", 15), command=home_screen, cursor="hand2").place(x=80, y=550)
btn2 = Button(win, text=" Submit >", fg="white", activeforeground="white", bg="#181d2b", activebackground="#181d2b", relief=FLAT, bd=0, borderwidth=0, highlightthickness=1, font=("Berlin Sans FB", 15), command=msg, cursor="hand2").place(x=750, y=550)

win.mainloop()