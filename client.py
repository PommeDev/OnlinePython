import socket
from tkinter import *

host = 'localhost'
port = 8000

screen = Tk()
screen.geometry("500x500")

zoneDeFrappe = Entry(screen)
txt = ""


def getEntry():
    global zoneDeFrappe
    global txt
    txt = zoneDeFrappe.get()


def sendMessage():
    global txt
    global zoneDeFrappe
    getEntry()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(txt.encode('utf-8'))
        buff = s.recv(512)
        print(buff.decode())
    zoneDeFrappe.delete(0, len(txt))
    txt = ""


boutonSend = Button(screen, text="Send", command=sendMessage)
boutonSend.pack()


zoneDeFrappe.pack()


mainloop()



