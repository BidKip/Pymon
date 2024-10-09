import pygame
from animation import AnimateSprite
class Entite(AnimateSprite):

    def __init__(self,name,x,y):
        super().__init__(name)
        self.image = self.get_image(0,0)
        self.image.set_colorkey([0,0,0])
        self.rect = self.image.get_rect()
        self.position = [x, y]

        self.pied = pygame.Rect(0,0, self.rect.width*0.5,12)
        self.old_position = self.position.copy()
        
    
    def sauvegarde_location(self): 
        self.old_position = self.position.copy()
    
    def bouge_droite(self): # Pour bouger le perso a droite
        self.position[0]+= self.speed
        self.change_anime('droite')


    def bouge_gauche(self): # Pour bouger le perso a gauche
        self.position[0]-= self.speed
        self.change_anime('gauche')

    def bouge_haut(self): # Pour bouger le perso en haut
        self.position[1]-= self.speed
        self.change_anime('haut')

    def bouge_bas(self): # Pour bouger le perso en bas
        self.position[1]+= self.speed
        self.change_anime('bas')

    def update(self):
        self.rect.topleft = self.position
        self.pied.midbottom = self.rect.midbottom
    
    def move_back(self): # pour replacer le perso si il touche un mur
        self.position = self.old_position
        self.rect.topleft = self.position
        self.pied.midbottom = self.rect.midbottom

    
    
class Player(Entite):

    def __init__(self):
        super().__init__('player',0,0)


class PNJ(Entite):
    def __init__(self,name, nb_points,dialog):
        super().__init__(name, 0,0)
        self.nb_points = nb_points
        self.dialog = dialog
        self.points = []
        self.name = name
        self.current_point = 0
    
    def move(self):
        current_point = self.current_point
        target_point = self.current_point+1
        if target_point >= self.nb_points:
            target_point = 0

        current_rect = self.points[current_point]
        target_rect = self.points[target_point]

        if current_rect.y < target_rect.y and abs(current_rect.x - target_rect.x) < 2:
            self.bouge_bas()

        elif current_rect.y > target_rect.y and abs(current_rect.x - target_rect.x) < 2:
            self.bouge_haut()

        elif current_rect.x > target_rect.x and abs(current_rect.y - target_rect.y) < 2:
            self.bouge_gauche()
            
        elif current_rect.x < target_rect.x and abs(current_rect.y - target_rect.y) < 2:
            self.bouge_droite()
        
        if self.rect.colliderect(target_rect):
            self.current_point = target_point
    def teleport_spawn(self):
        location = self.points[self.current_point]
        self.position[0] = location.x
        self.position[1] = location.y
        self.sauvegarde_location()
    
    def charge_points(self,tmx_data):
        for num in range(1,self.nb_points+1):
            point = tmx_data.get_object_by_name(f"{self.name}_chemin{num}")
            rect = pygame.Rect(point.x,point.y,point.width,point.height)
            self.points.append(rect)
