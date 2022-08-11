import socket
from tkinter import *

host = 'localhost'
port = 8000

screen = Tk()
screen.geometry("500x500")
screen.title("client1")

zoneDeFrappe = Entry(screen)
txt = "client1 + "


def getEntry():
    global zoneDeFrappe
    global txt
    txt += zoneDeFrappe.get()


def sendMessage():
    global txt
    global zoneDeFrappe
    getEntry()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(txt.encode('utf-8'))
    zoneDeFrappe.delete(0, len(txt))
    txt = "client1 + "


def endConv():
    global txt
    global zoneDeFrappe
    txt = "aZ72Re32A66EfF45"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(txt.encode('utf-8'))
    zoneDeFrappe.delete(0, len(txt))
    zoneDeFrappe.insert(0, "Conversation is End")
    zoneDeFrappe.configure(state="readonly")
    txt = "client1 + "


boutonSend = Button(screen, text="Send", command=sendMessage)
boutonSend.pack()

boutonEnd = Button(screen, text="End Conversation", command=endConv)
boutonEnd.pack()

zoneDeFrappe.pack()


mainloop()



