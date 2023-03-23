import pygame
import pytmx
import pyscroll
from player import Player


class Game:
    def __init__(self):  
        self.screen = pygame.display.set_mode((800,630)) # taille de la fenétre
        pygame.display.set_caption("Pokemon") # nom de la fenétre 

        #chargement carte
        tmx_data = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data,self.screen.get_size())
        map_layer.zoom = 2

        #generer le joueur
        player_position = tmx_data.get_object_by_name("Spawn")
        self.player = Player(player_position.x,player_position.y)

        #Collision
        self.mur = []
        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.mur.append(pygame.Rect(obj.x,obj.y, obj.width, obj.height))
                print('MURRRRRRRRR')

        #dessiner le groupe de calque
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer,default_layer=3)
        self.group.add(self.player)
    def touche(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.bouge_haut()
            self.player.change_anime("haut")

        elif pressed[pygame.K_DOWN]:
            self.player.bouge_bas()
            self.player.change_anime("bas")

        elif pressed[pygame.K_LEFT]:
            self.player.bouge_gauche()
            self.player.change_anime("gauche")

        elif pressed[pygame.K_RIGHT]:
            self.player.bouge_droite()
            self.player.change_anime("droite")

    def update(self):
        self.group.update()

        # verif colli
        for sprite in self.group.sprites():
            if sprite.pied.collidelist(self.mur) > -1:
                sprite.move_back()

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:

            self.player.sauvegarde_location()
            self.touche()
            self.update()
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)
            pygame.display.flip()

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            clock.tick(60)
        pygame.quit()
        
        

