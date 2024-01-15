
import datetime
from tkinter import *
from tkinter import messagebox
import tkinter
import mysql.connector as mys

mys_connect = mys.connect(host="localhost", user="root", password="abcd@1234", database="movie_show_reservation")
mys_cursor = mys_connect.cursor()
query1 = "CREATE TABLE IF NOT EXISTS MOVIE (MOVIE_NAME VARCHAR(50), MOVIE_FORMAT VARCHAR(20), TIME_SLOT VARCHAR(20), DATE INT(20), MONTH VARCHAR(20), SEATS INT(20), AMOUNT INT(20))"
# mys_cursor.execute(query1)

win = Tk()
win.title("Movie Ticket Reservation")
win.geometry("905x605")
win.resizable(0,0)
img = PhotoImage(file="2.png")
label1 = Label(win, image=img).place(x=0, y=0)

a=[""]
var2 = StringVar(value="Select Movie")

def get_lang(movie):
    movie = str(var1.get())
    menu2.config(state="normal")
    eng = ["a","b","c"]
    hin = ["d","e","f"]
    if movie == "English":
        var2.set(value = "Select Movie")
        menu2["menu"].delete(0, "end")
        for x in eng:
            menu2["menu"].add_command(label=x, command=tkinter._setit(var2, x))
    elif movie == "Hindi":
        var2.set(value = "Select Movie")
        menu2["menu"].delete(0, "end")
        for x in hin:
            menu2["menu"].add_command(label=x, command=tkinter._setit(var2, x))
    menu2["menu"].config(borderwidth=0, fg="White", activeforeground="White", bg="#181d2b", activebackground="#181d2b", font=("Berlin Sans FB", 13))
    '''    
    if movie == "English":
        menu2 = OptionMenu(win, var2, *eng)
        menu2.config(width=30, height=2, borderwidth=0, highlightthickness=1, fg="White", activeforeground="White", bg="#181d2b", activebackground="#181d2b", font=("Berlin Sans FB", 13))
        menu2["menu"].config(borderwidth=0, fg="White", activeforeground="White", bg="#181d2b", activebackground="#181d2b", font=("Berlin Sans FB", 13))
        menu2.place(x=350, y=230)

    elif movie == "Hindi":
        menu2 = OptionMenu(win, var2, *hin)
        menu2.config(width=30, height=2, borderwidth=0, highlightthickness=1, fg="White", activeforeground="White", bg="#181d2b", activebackground="#181d2b", font=("Berlin Sans FB", 13))
        menu2["menu"].config(borderwidth=0, fg="White", activeforeground="White", bg="#181d2b", activebackground="#181d2b", font=("Berlin Sans FB", 13))
        menu2.place(x=350, y=230) 
    '''

def get_seat(seat):
    seat = str(var5.get())
    while seat == "Custom":
        ent = Entry(win, width=7, borderwidth=0, highlightthickness=1, fg="white", bg="#181d2b", font=("Berlin Sans FB", 17), justify="center")
        ent.place(x=700, y=485)
    else:
        ent.destroy()

def get_seat_custom(seat):
    def delete():
        ent1.after(00000, lambda: win.destroy())
    x = 0 
    seat = str(var5.get())
    while x == 0:
        ent1 = Entry(win)
        if seat == "Custom":
            ent1.place(x=700, y=485)
        elif seat == "1" or seat == "2" or seat == "3" or seat == "4" or seat == "5":
            delete
            # ent1.delete(0, "end")
        x += 1


def home_screen():
    win.destroy()
    import main

def msg():
    # movie_name = var2.get()
    date_user = var0.get()
    user_lang = var1.get()
    movie_name = var2.get()
    format = str(var3.get())
    time_slot = var4.get()
    no_of_seats = var5.get()
    if date_user == "Select Date" or format == "Select Format" or time_slot == "Time Slot" or no_of_seats == "Seats":
        messagebox.showwarning(" Warning !", "Incomplete Field Found")
    else:
        # amount
        if format == "IMAX":
            prize = 350
        elif format == "2D":
            prize = 400
        elif format == "3D":
            prize = 450
        elif format == "IMAX 3D":
            prize = 550
        date_usr = int(date_user)
        seats = int(var5.get())
        amt = seats*prize
        gst = int(0.3*amt)
        total_amount = amt + gst
        # query2 = "INSERT INTO MOVIE VALUES("{0}", "{1}", "{2}", "{3}", "{4}", "{5}", "{6}").format(movie_name, format, time_slot, date_usr, month, seats, total_amount)"
        # mys_cursor.execute(query2)
        # mys_connect.commit()
        # print(no_of_seats,date_user,month_name,time_slot,format, total_amount)
        var0.set(value = "Select Date")
        var1.set(value = "Selet Language")
        var2.set(value = "Select Movie")
        menu2.config(state="disable")
        var3.set(value = "Select Format")
        var4.set(value = "Time Slot")
        var5.set(value = "Seats")

        messagebox.showinfo("Message", "Your Show is Booked")

# date

x = datetime.datetime.now()
year = x.strftime('%Y') # "%Y" getting year like 2022 as string.
month = x.strftime('%m') # "%m" getting month of the year like 02 as string.
current_date = x.strftime('%d') # "%d" getting current date like 01 as string.
month_name = x.strftime('%B') # "%B" getting month name like March.

# inserting the next seven days dates in a list so as the user can select one from those dates only.

dates = []
for i in range(1,7):
    next_date = datetime.date.today() + datetime.timedelta(i)
    date = next_date.strftime('%d')
    dates.append(int(date))
var0 = StringVar(value="Select Date")
menu0 = OptionMenu(win, var0, *dates)
menu0.config(width=30, height=2, borderwidth=0, highlightthickness=1, fg="White", activeforeground="White", bg="#181d2b", activebackground="#181d2b", font=("Berlin Sans FB", 13))
menu0["menu"].config(borderwidth=0, fg="White", activeforeground="White", bg="#181d2b", activebackground="#181d2b", font=("Berlin Sans FB", 13))
menu0.place(x=350, y=70)

# language 

val1 = ["English", "Hindi"]
var1 = StringVar(value="Select Language")
menu1 = OptionMenu(win, var1, *val1, command=get_lang)
menu1.config(width=30, height=2, borderwidth=0, highlightthickness=1, fg="White", activeforeground="White", bg="#181d2b", activebackground="#181d2b", font=("Berlin Sans FB", 13))
menu1.children["menu"].config(borderwidth=0, fg="White", activeforeground="White", bg="#181d2b", activebackground="#181d2b", font=("Berlin Sans FB", 13))
menu1.place(x=350, y=150)

# movie

menu2 = OptionMenu(win, var2, *a)
menu2.config(width=30, height=2, borderwidth=0, highlightthickness=1, fg="White", activeforeground="White", bg="#181d2b", activebackground="#181d2b", font=("Berlin Sans FB", 13), state="disable")
menu2.place(x=350, y=230)

# movie_format

val3 = ["IMAX", "2D", "3D", "IMAX 3D"]
var3 = StringVar(value="Select Format")
menu3 = OptionMenu(win, var3, *val3)
menu3.config(width=30, height=2, borderwidth=0, highlightthickness=1, fg="White", activeforeground="White", bg="#181d2b", activebackground="#181d2b", font=("Berlin Sans FB", 13))
menu3["menu"].config(borderwidth=0, fg="White", activeforeground="White", bg="#181d2b", activebackground="#181d2b", font=("Berlin Sans FB", 13))
menu3.place(x=350, y=310)

# time slot

val4 = ["9:10 AM", "12:45 PM", "4:15 PM", "7:50 PM", "11:10 PM"]
var4 = StringVar(value="Time Slot")
menu4 = OptionMenu(win, var4, *val4)
menu4.config(width=30, height=2, borderwidth=0, highlightthickness=1, fg="White", activeforeground="White", bg="#181d2b", activebackground="#181d2b", font=("Berlin Sans FB", 13))
menu4["menu"].config(borderwidth=0, fg="White", activeforeground="White", bg="#181d2b", activebackground="#181d2b", font=("Berlin Sans FB", 13))
menu4.place(x=350, y=390)

# seats

val5 = ["1","2","3","4","5","Custom"]
var5 = StringVar(value="Seats")
menu5 = OptionMenu(win, var5, *val5, command = get_seat_custom)
menu5.config(width=30, height=2, borderwidth=0, highlightthickness=1, fg="White", activeforeground="White", bg="#181d2b", activebackground="#181d2b", font=("Berlin Sans FB", 13))
menu5["menu"].config(borderwidth=0, fg="White", activeforeground="White", bg="#181d2b", activebackground="#181d2b", font=("Berlin Sans FB", 13))
menu5.place(x=350, y=470)

# Buttons

btn1 = Button(win, text="< Prev ", fg="white", activeforeground="white", bg="#181d2b", activebackground="#181d2b", relief=FLAT, bd=0, borderwidth=0, highlightthickness=1, font=("Berlin Sans FB", 15), command=home_screen, cursor="hand2").place(x=80, y=550)
btn2 = Button(win, text=" Submit >", fg="white", activeforeground="white", bg="#181d2b", activebackground="#181d2b", relief=FLAT, bd=0, borderwidth=0, highlightthickness=1, font=("Berlin Sans FB", 15), command=msg, cursor="hand2").place(x=750, y=550)

win.mainloop()