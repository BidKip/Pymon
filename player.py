import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self,x,y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('player.png')
        self.image = self.get_image(0,0)
        self.image.set_colorkey([0,0,0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.images = {'bas':self.get_image(0,0), 'haut':self.get_image(0,19), 'gauche':self.get_image(0,37), 'droite':self.get_image(0,55)}

        self.pied = pygame.Rect(0,0, self.rect.width*0.5,25)
        self.old_position = self.position.copy()
        self.speed = 2
    
    def sauvegarde_location(self): 
        self.old_position = self.position.copy()
    
    def change_anime(self,name): # pour changer l'animation du perso
        self.image = self.images[name]
        self.image.set_colorkey([0,0,0])

    def bouge_droite(self): # Pour bouger le perso a droite
        self.position[0]+= self.speed

    def bouge_gauche(self): # Pour bouger le perso a gauche
        self.position[0]-= self.speed

    def bouge_haut(self): # Pour bouger le perso en haut
        self.position[1]-= self.speed

    def bouge_bas(self): # Pour bouger le perso en bas
        self.position[1]+= self.speed

    def update(self):
        self.rect.topleft = self.position
        self.pied.midbottom = self.rect.midbottom
    
    def move_back(self): # pour replacer le perso si il touche un mur
        self.position = self.old_position
        self.rect.topleft = self.position
        self.pied.midbottom = self.rect.midbottom

    def get_image(self,x,y):
        image = pygame.Surface([32,32])
        image.blit(self.sprite_sheet,(0, 0),(x,y,16,16))
        return image