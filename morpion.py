from tkinter import *


class Morpion:
    """Class qui contiendra un morpion: pour le moment juste le déplacement d'un cercle"""
    def __init__(self, screen):
        self.screen = screen
        self.bouton1 = Button(self.screen, text='->', command=self.droite)
        self.bouton2 = Button(self.screen, text='<-', command=self.gauche)

        self.bouton1.pack()
        self.bouton2.pack()

        self.posX = 0
        self.posY = 0

        self.canvas = Canvas(self.screen, height=200, width=200)
        self.canvas.pack()
        self.balle = self.canvas.create_oval(10, 10, 30, 30, fill='red')


    def movement(self):
        self.canvas.move(self.balle, self.posX, self.posY)

    def gauche(self):
        self.posX = -1
        self.movement()

    def droite(self):
        self.posX = 1
        self.movement()





