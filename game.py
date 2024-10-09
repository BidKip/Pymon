import pygame
import pytmx
import pyscroll
from player import Player
from map import MapManager
from dialogue import DialogBox


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800,630)) # taille de la fenétre
        pygame.display.set_caption("Pokemon") # nom de la fenétre 

    
        #generer le joueur
        self.player = Player()
        self.map_manager = MapManager(self.screen, self.player)
        self.dialogue_box = DialogBox()


    def touche(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_z]:
            self.player.bouge_haut()
            self.map_manager.check_herbe()

        elif pressed[pygame.K_s]:
            self.player.bouge_bas()
            self.map_manager.check_herbe()

        elif pressed[pygame.K_q]:
            self.player.bouge_gauche()
            self.map_manager.check_herbe()

        elif pressed[pygame.K_d]:
            self.player.bouge_droite()
            self.map_manager.check_herbe()


    def update(self):
        self.map_manager.update()


    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:

            self.player.sauvegarde_location()
            self.touche()
            self.update()
            self.map_manager.draw()
            self.dialogue_box.render(self.screen)
            pygame.display.flip()

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.map_manager.check_pnj_collisions(self.dialogue_box)
            clock.tick(60)
        pygame.quit()
        
        

