from tkinter import *
import pygame
class fin_jeux(Tk):
    def __init__(self):
        pygame.mixer.init()
        Tk.__init__(self)
        bag = PhotoImage(file = "imagebg.gif")
        self.lab = Label(self,image=bag)
        self.lab.pack()
        self.lab = Label(self , text = "Merci d'avoir jouer a mon jeux, passe une bonne journée/nuit")
        self.lab.pack()


        pygame.mixer.music.load('generique.mp3')
        pygame.mixer.music.play(loops=0)
        self.but1 = Button(self, text='fermer le jeux',command=self.detruire)

        self.but1.pack(side=TOP) 

        self.mainloop()
    def detruire(self):
        self.but1.destroy()
        self.destroy()
    


        
