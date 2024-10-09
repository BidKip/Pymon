import pygame

class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self,name):
        super().__init__()
        self.sprite_sheet = pygame.image.load(f'{name}.png')
        self.animation_index = 0
        self.montre= 0
        self.images = {'bas':self.get_animation(0), 'gauche':self.get_animation(32), 
                       'droite':self.get_animation(64), 'haut':self.get_animation(96)}
        self.speed = 2
    
    def get_animation(self,y):
        images = []
        for i in range(0,3):
            x = i*32
            image = self.get_image(x,y)
            images.append(image)
        return images
    def change_anime(self,name): # pour changer l'animation du perso
        self.image = self.images[name][self.animation_index]
        self.image.set_colorkey([0,0,0])
        self.montre += self.speed*8
        
        if self.montre >= 100:

            self.animation_index += 1 # passer a l'animation suivante
            if self.animation_index >= len(self.images[name]):
                self.animation_index = 0
            self.montre = 0

    def get_image(self,x,y):
        image = pygame.Surface([32,32])
        image.blit(self.sprite_sheet,(0, 0),(x,y,32,32)) #taille de l'image (32,32)
        return image
    
