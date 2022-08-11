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

titre = Label(screen, text="Serveur")
titre.pack()

host = 'localhost'
port = 8000

alwaysInConv = True

serveurOn = True

txt = ""
affichage = StringVar()


def runServ():
    global txt
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
                if not message == "aZ72Re32A66EfF45":
                    txt += " " + message
            if message == "aZ72Re32A66EfF45":
                serveurOn = False
            affichage.set(txt)
            screen.update()


def stopServ():
    global serveurOn
    serveurOn = False


affichageLabel = Label(screen, textvariable=affichage)
affichageLabel.pack()

boutonRun = Button(screen, text='Run', command=runServ)
boutonRun.pack()

boutonStop = Button(screen, text='Stop', command=stopServ)
boutonStop.pack()

mainloop()
