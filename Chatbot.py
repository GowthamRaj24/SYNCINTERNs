from tkinter import *
import time
import pywhatkit
window = Tk()
window.title("SYNC CHAT BOT")
window.geometry('400x500')


def send():
    send ="you:"+messagewindow.get()

    chatarea.insert(END,"\n"+send)
    got = messagewindow.get()
    got = got.lower()

    if(got == 'hi'):
        chatarea.insert(END,"\n"+"BOT: hello")
    elif(got == "what is your name"):
        chatarea.insert(END,"\n"+"BOT: my name is Jarvis")
    elif(got == "how are you"):
        chatarea.insert(END,"\n"+"BOT: I am fime. what about you")
    elif(got == "i am fine"):
        chatarea.insert(END,"\n"+"BOT: good to hear that")
    elif ('time' in got):
        curr_time = time.strftime('%H:%M:%S')
        chatarea.insert(END,"\n"+f"BOT: {curr_time}")
    elif ('play' in got):
        search = got.split(' ')
        pywhatkit.playonyt(search[1])
    else :
        chatarea.insert(END,"\n"+"BOT: I didn't get that")

    messagewindow.delete(0,END)


#create chat area in the window

chatarea = Text(window,bg='white',width=50,height=8)
chatarea.place(x=6,y=6, height=385,width=370)


#message area in the window

messagewindow = Entry(window,bg='white',width= 30)
messagewindow.place(x=128,y=400,height=88,width=260)

#Button
send = Button(window,text="send",bg='blue',activebackground='light blue' ,width=20, height=5,font=('Arial',12),command= send)
send.place(x=6,y=400,height=81,width=120)


window.mainloop()