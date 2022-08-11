import socket
from tkinter import *
"""  Serveur De Base


host = 'localhost'
port = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serveur:
    serveur.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serveur.bind((host, port))
    serveur.listen(1)
    while True:
        connexion, adresse = serveur.accept()
        with connexion:
            buff = connexion.recv(512)
            message = buff.decode('utf-8')
            connexion.sendall(f'echo {message}'.encode('utf-8'))
            
"""

screen = Tk()
screen.geometry('500x500')
screen.title("serveur")

titre = Label(screen, text="Serveur")
titre.pack()

host = 'localhost'
port = 8000

alwaysInConv = True

serveurOn = True

txtClient1 = "CLient1 dit : "
txtClient2 = "CLient2 dit : "
affichageCLient1 = StringVar()
affichageCLient2 = StringVar()


def runServ():
    global txtClient1
    global txtClient2
    global serveurOn
    serveurOn = True
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serveur:
        serveur.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serveur.bind((host, port))
        serveur.listen(1)
        while serveurOn:
            connexion, adresse = serveur.accept()
            with connexion:
                buff = connexion.recv(512)
                message = buff.decode('utf-8')
                if not message == "aZ72Re32A66EfF45" or not message == "aZ72Re32A66EfF46":
                    if message[:10] == "client1 + ":
                        txtClient1 += " " + message[10:]
                    else:
                        txtClient2 += " " + message[10:]

            if message == "aZ72Re32A66EfF45":
                serveurOn = False
                Label(screen, text="Client1 has been leave the conversation").pack()

            elif message == "aZ72Re32A66EfF46":
                Label(screen, text="Client1 has been leave the conversation").pack()

            if message[:10] == "client1 + ":
                affichageCLient1.set(txtClient1)
            else:
                affichageCLient2.set(txtClient2)

            screen.update()


def stopServ():
    global serveurOn
    serveurOn = False


affichageLabelClient1 = Label(screen, textvariable=affichageCLient1)
affichageLabelClient1.pack()

affichageLabelClient2 = Label(screen, textvariable=affichageCLient2)
affichageLabelClient2.pack()

boutonRun = Button(screen, text='Run', command=runServ)
boutonRun.pack()

boutonStop = Button(screen, text='Stop', command=stopServ)
boutonStop.pack()

mainloop()
