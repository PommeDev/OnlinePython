import socket
from tkinter import *
from morpion import *
from actualiseActionList import *

host = '192.168.1.94'
port = 8000

screen = Tk()
screen.geometry("500x500")
screen.title("client1")

zoneDeFrappe = Entry(screen)
txt = "client1 + "

actionAfaire = []
indiceAction = -2


class MorpionBis(Morpion):
    def gauche(self):
        global zoneDeFrappe
        global indiceAction
        global txt
        txt += 'gauche'
        indiceAction += 7
        sendMessageB()
        self.gauche2()

    def droite(self):
        global zoneDeFrappe
        global indiceAction
        global txt
        txt += 'droite'
        indiceAction += 7
        sendMessageB()
        self.droite2()

    def gauche2(self):
        self.posX = -1
        self.movement()

    def droite2(self):
        self.posX = 1
        self.movement()


morpion = MorpionBis(screen)


def getEntry():
    """Fonction qui récupère ce qui est inscrit dans zoneDeFrappe: tkinter.Entry"""
    global zoneDeFrappe
    global txt
    txt += zoneDeFrappe.get()
    if txt[10:] == 'gauche':
        morpion.gauche2()
    if txt[10:] == 'droite':
        morpion.droite2()


def sendMessage():
    """Fonction qui envoie le message dans zoneDeFrappe: tkinter.Entry au serveur"""
    global txt
    global zoneDeFrappe
    global actionAfaire
    getEntry()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(txt.encode('utf-8'))
        messageServ = s.recv(512).decode('utf-8')
        actionAfaire = actualise(indiceAction, messageServ)[0]

    for i in actionAfaire:
        if i == 'gauche':
            morpion.gauche2()
        else:
            morpion.droite2()

    zoneDeFrappe.delete(0, len(txt))
    txt = "client1 + "


def sendMessageB():
    global txt
    global zoneDeFrappe
    global actionAfaire
    global indiceAction
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(txt.encode('utf-8'))
        messageServ = s.recv(512).decode('utf-8')
    actionAfaire = actualise(indiceAction, messageServ)[0]
    indiceAction = actualise(indiceAction, messageServ)[1]

    for i in actionAfaire:
        if i == 'gauche':
            morpion.gauche2()
        else:
            morpion.droite2()

    zoneDeFrappe.delete(0, len(txt))
    txt = "client1 + "


def endConv():
    """FOnction exécuter qui envoi le message de fin au serveur"""
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
boutonSend.pack()  # Le bouton pour envoyer un message au serveur

boutonEnd = Button(screen, text="End Conversation", command=endConv)
boutonEnd.pack()  # Le bouton pour envoyer un message au serveur ( ce message est le message de fin de conversation :
# voir code.txt)

zoneDeFrappe.pack()


try:
    mainloop()
except AttributeError:
    pass




