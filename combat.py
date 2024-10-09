from tkinter import *
from random import randrange
from typing import Any
import pygame


class Combat(Tk):
    point_bot = 0
    point_player = 0
    ok = 0
    def __init__(self):
        Combat.ok = 1
        Tk.__init__(self)
        self.v = IntVar()
        
        self.lab1 = Label(self , text = "FAITE VOTRE CHOIX") 
        self.lab1.grid(column=2,row=2)


        self.image1 = PhotoImage(file="plante.gif")
        Radiobutton(self, image=self.image1,indicatoron = 0,variable=self.v,value=0).grid(column=1,row=3) 
        self.image2 = PhotoImage(file="eau.gif")
        Radiobutton(self, image=self.image2,indicatoron = 0,variable=self.v,value=1).grid(column=2,row=3)
        self.image3 = PhotoImage(file="feux.gif")
        Radiobutton(self, image=self.image3,indicatoron = 0,variable=self.v,value=2).grid(column=3,row=3) 

        self.but1 = Button(self,text="Appuyer ici si votre choix est fait",command=self.fight)
        self.but1.grid(column=2,row=4)
        self.mainloop()


    def fight(self):
        bot = randrange(0,3)
        self.but1.destroy()
        self.but2 = Button(self,text="apuyer ici pour continuer le combat",command=self.supp)
        self.but2.grid(column=2,row=4)   
        self.lab2 = Label(self , text = "VOTRE CHOIX") 
        self.lab2.grid(column=1,row=1)
        self.lab5 = Label(self , text = "CHOIX ENNEMI") 
        self.lab5.grid(column=3,row=1)
        self.lab1.configure(text="CONTRE")
        self.lab3 = Label(self , text = "",bg='white') 
        self.lab3.grid(column=2,row=1)
        self.lab6 = Label(self,text="Vos point(s): "+str(self.point_player))
        self.lab6.grid(column=1,row=4)
        self.lab7 = Label(self,text="Points ennemi: "+str(self.point_bot))
        self.lab7.grid(column=3,row=4)
        
        if self.v.get() == 0:
            can1 = Canvas(self,width=150,height=150,bg='white')
            item = can1.create_image(80,80,image = self.image1)
            can1.grid(column=1,row=2)
            if bot == 0:
                can2 = Canvas(self,width=150,height=150,bg='white')
                item = can2.create_image(80,80,image = self.image1)
                can2.grid(column=3,row=2)
                self.lab3.configure(text = "EGALITE") 
            elif bot == 1:
                can2 = Canvas(self,width=150,height=150,bg='white')
                item = can2.create_image(75,80,image = self.image2)
                can2.grid(column=3,row=2)
                self.lab3.configure(text = "GAGNER",bg="green")
                self.point_player += 1
                self.lab6.configure(text="Vos point(s): "+str(self.point_player))
            else:
                can2 = Canvas(self,width=150,height=150,bg='white')
                item = can2.create_image(75,80,image = self.image3)
                can2.grid(column=3,row=2)
                self.lab3.configure(text = "PERDU",bg="red")
                self.point_bot += 1
                self.lab7.configure(text="Points ennemi: "+str(self.point_bot))


        elif self.v.get() == 1:
            can1 = Canvas(self,width=150,height=150,bg='white')
            item = can1.create_image(75,80,image = self.image2)
            can1.grid(column=1,row=2)
            if bot == 0:
                can2 = Canvas(self,width=150,height=150,bg='white')
                item = can2.create_image(80,80,image = self.image1)
                can2.grid(column=3,row=2)
                self.lab3.configure(text = "PERDU",bg="red")
                self.point_bot += 1
                self.lab7.configure(text="Points ennemi: "+str(self.point_bot))
            elif bot == 1:
                can2 = Canvas(self,width=150,height=150,bg='white')
                item = can2.create_image(75,80,image = self.image2)
                can2.grid(column=3,row=2)
                self.lab3.configure(text = "EGALITE") 
            else:
                can2 = Canvas(self,width=150,height=150,bg='white')
                item = can2.create_image(75,80,image = self.image3)
                can2.grid(column=3,row=2)
                self.lab3.configure(text = "GAGNER",bg="green") 
                self.point_player += 1
                self.lab6.configure(text="Vos point(s): "+str(self.point_player))

        else:
            can1 = Canvas(self,width=150,height=150,bg='white')
            item = can1.create_image(75,80,image = self.image3)
            can1.grid(column=1,row=2)
            if bot == 0:
                can2 = Canvas(self,width=150,height=150,bg='white')
                item = can2.create_image(80,80,image = self.image1)
                can2.grid(column=3,row=2)
                self.lab3.configure(text = "GAGNER",bg="green") 
                self.point_player += 1
                self.lab6.configure(text="Vos point(s): "+str(self.point_player))
            elif bot == 1:
                can2 = Canvas(self,width=150,height=150,bg='white')
                item = can2.create_image(75,80,image = self.image2)
                can2.grid(column=3,row=2)
                self.lab3.configure(text = "PERDU",bg="red")
                self.point_bot += 1
                self.lab7.configure(text="Points ennemi: "+str(self.point_bot))
            else:
                can2 = Canvas(self,width=150,height=150,bg='white')
                item = can2.create_image(75,80,image = self.image3)
                can2.grid(column=3,row=2)
                self.lab3.configure(text = "EGALITE")
        if self.point_bot == 3:
            self.vict = 0
            self.but2.destroy()
            self.but3 = Button(text="Fini",command=self.fini)
            self.but3.grid(column=2,row=4)
            self.lab1.configure(text="Vous avez perdu",bg='red')
            
        elif self.point_player ==3:
            self.vict = 1
            self.but2.destroy()
            self.but3 = Button(text="Fini",command=self.fini)
            self.but3.grid(column=2,row=4)
            self.lab1.configure(text="Vous avez gagner",bg='green')
            
        
    

    def supp(self):
        self.lab3.destroy()
        self.lab6.destroy()
        self.lab7.destroy()
        self.but2.destroy()
        self.fight()
    
    def fini(self):
        self.destroy()
        if self.vict ==0:
            return 0
        else:
            return 1
        
    def __call__(self=None):
        pygame.mixer.init()
        son1 = pygame.mixer.Sound('music_combat.mp3')
        son1.play(loops=0)
        son1.set_volume(0.3)
        pygame.mixer.music.stop()
        self = Combat()
        son1.stop()
        return self.vict