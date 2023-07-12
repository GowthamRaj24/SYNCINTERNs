import datetime
from tkinter import *

mw = Tk()
i = "a"
y = "a"

def curr_time():
    global y
    x = datetime.datetime.now()
    y = x.strftime('%H:%M:%S')
    live_time.config(text=y)
    live_time.after(1000, curr_time)
    print(y)


def clicked():
    global i
    s = input.get()
    if s:
        set = Label(mw, text=f"Alarm set at {s}")
    else:
        set = Label(mw,text="Can't be empty!!")
    set.grid(row=6, column=0, columnspan=2)
    input.delete(0, END)
    i = input.get()

def ring():
    global i
    x = datetime.datetime.now()
    z = x.strftime('%H:%M')
    print("Z : ", z)
    print("I : ", i)
    if z >= i:
        print("Wake up!!!")



mw.title("Alarm Clock")
mw.iconbitmap("data/icons8-alarm-clock-50.ico")
project = Label(mw, text="PROJECT_1", font=("Arial", 16))
live_time = Label(mw, text="TIME", font=('Arial', 30), bg='black', fg='red', border=True, borderwidth=15)
alarm_clock = Label(mw, text="ALARM CLOCK", font=('Arial', 14))
text = Label(mw, text="Enter (%H : %M) -", font=('Arial', 10))
input = Entry(mw, width=20, font=('Arial', 14))
set_alarm = Button(mw, text="Set Alarm", command=clicked)

project.grid(row=0, column=0, pady=15, columnspan=2)
live_time.grid(row=1, column=0, columnspan=2, rowspan=2, padx=32, pady=10)
alarm_clock.grid(row=3, column=0, pady=10, columnspan=2)
text.grid(row=4, column=0, pady=10, padx=20)
input.grid(row=4, column=1, pady=10)
set_alarm.grid(row=5, column=0, pady=10, columnspan=2)
curr_time()
mw.mainloop()
