from tkinter import *
import random
from PIL import ImageTk, Image

window = Toplevel()
window.title("OFFER'S")
window.geometry("905x605")
window.resizable(0,0)
img = ImageTk.PhotoImage(Image.open("4.png"))
label1 = Label(window, image=img).place(x=0, y=0)
x=[]
offer1 = ["10% INSTANT OF ON CARDS", "20% FOR MEMBERS ON WED", "5% ON BOOKINGS OVER 5"]
offer2 = ["FREE MEAL COMBO ON BOOKING, OVER Rs. 2000", "HAPPY SUNDAY WITH FREE POPCORN, ON BOOKING Rs.1500"]
a = random.choice(offer1)
x.append(a)
b = random.choice(offer2)
for i in b:
     c = b.split(', ')
     x.extend(c)
    # print(x)
label2 = Label(window, text=x[0], fg="#fff4bb", bg='#181d2b',font=('Berlin Sans FB', 23)).place(x=275, y=250)
label3 = Label(window, text=x[1], fg="#fff4bb", bg='#181d2b',font=('Berlin Sans FB', 23)).place(x=205, y=350)
label4 = Label(window, text=x[2], fg="#fff4bb", bg='#181d2b',font=('Berlin Sans FB', 23)).place(x=340, y=400)
window.after(20000, lambda: window.destroy()) # WINDOW WILL DESTROY AFTER 30 SEC

window.mainloop()