from tkinter import *

win = Tk()
win.title("Theatre")
win.geometry("905x605")
win.resizable(0,0)
img=PhotoImage(file="1.png")
label1 = Label(win, image=img)
label1.place(x=0,y=0)

def movie():
    win.destroy()
    import movie

def show():
    win.destroy()
    import shows

def offer():
    import offers    

button1 = Button(win, text="MOVIE TICKETS", width=25, fg="#79d1c3", activeforeground="#fce578", bg="#181d2b", activebackground="#181d2b", relief="flat", borderwidth="0", font=("Gabriola",22), cursor="hand2", command=movie)
button1.place(x=290, y=140)
button2 = Button(win, text="SHOW TICKETS", width=25, fg="#79d1c3", activeforeground="#fce578", bg="#181d2b", activebackground="#181d2b", relief="flat", borderwidth="0", font=("Gabriola",22), cursor="hand2", command=show)
button2.place(x=290, y=250)
button3 = Button(win, text="OFFERS", width=25, fg="#79d1c3", activeforeground="#fce578", bg="#181d2b", activebackground="#181d2b", relief="flat", borderwidth="0", font=("Gabriola",22), cursor="hand2", command=offer)
button3.place(x=290, y=360)
win.mainloop()