import pyshorteners
from tkinter import *
mw = Tk()
mw.title('URL Shortener')

def shortened():
    x = inpu.get()
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(x)
    print(short_url)
    out.insert(string=short_url,index=0)


head = Label(mw,text="SYNCINTERN'S",font=('Arail',20))
task = Label(mw,text='TASK-3 | URL SHORTENER',font=('Arail',20))
enter = Label(mw,text='Enter your long URL here :',font=('Arial',16))
inpu = Entry(mw,font=('Arail',18),width=30)
get = Button(mw,text="GET SHORT URL",width=15,command = shortened)
short = Label(mw,text="Your Shortened URL is :",font=('Arail',16))
out = Entry(mw,font=('Arial',18),width=30)

head.grid(row=0,column=0,columnspan=3,pady=10)
task.grid(row=1,column=0,columnspan=3,pady=10,padx=15)
enter.grid(row=2,column=0,pady=15,padx=15)
inpu.grid(row=3,column=0,columnspan=3,pady=15)
get.grid(row=4,column=0,pady=10,columnspan=3)
short.grid(row=5,column=0,pady=10)
out.grid(row=6,column=0,columnspan=3,pady=15,padx=15)



mw.mainloop()