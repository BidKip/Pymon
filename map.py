from dataclasses import dataclass
from player import Player
import pygame
import pytmx
import pyscroll
from player import PNJ
from dialogue import DialogBox
from random import randrange
from combat import Combat
from finJeux import fin_jeux

@dataclass
class Portal():
    from_world: str
    origin_point: str
    target_world: str
    teleport_point: str



@dataclass
class Map():
    name: str
    walls: list[pygame.Rect]
    herbes: list[pygame.Rect]
    group: pyscroll.PyscrollGroup
    tmx_data: pytmx.TiledMap
    portal: list[Portal]
    pnjs: list[PNJ]


class MapManager():

    def __init__(self,screen,player):
        pygame.mixer.init()
        pygame.mixer.music.load('little_route.mp3')
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.set_volume(0.3)
        self.map = dict() #'maison' --> map('house',walls,group)
        self.screen = screen
        self.player = player
        self.current_map = 'carte'
        self.montre = 0
        self.speed = 2
        self.battu = 0

        self.enre_map("carte", portal=[
            Portal(from_world="carte",origin_point="enter_house",target_world='maison',teleport_point='spawn_house'),
            Portal(from_world="carte",origin_point="enter_house2",target_world='maison2',teleport_point='spawn_house'),
            Portal(from_world='carte',origin_point='chemin_1',target_world="chemin_1",teleport_point="spawn_chemin_from_map1")
        ], pnjs=[
            PNJ("robin",nb_points=4,dialog=["quel belle journée."])
        ])
        self.enre_map('maison', portal=[
            Portal(from_world="maison",origin_point="exit_house",target_world='carte',teleport_point='exit_house')
        ],pnjs=[
            PNJ('paul',nb_points=2,dialog =['Bonne aventure'])
        ]
        )
        self.enre_map('maison2', portal=[
            Portal(from_world="maison2",origin_point="exit_house",target_world='carte',teleport_point='exit_house2')
        ])
        self.enre_map("chemin_1",portal=[
            Portal(from_world = 'chemin_1',origin_point="exit_chemin1_1",target_world='carte',teleport_point='exit_chemin1')
        ])


        self.teleport_player("Spawn")
        self.teleports_pnjs()
    
    def check_pnj_collisions(self,dialog_box):
        for sprite in self.get_group().sprites():
            if sprite.pied.colliderect(self.player.rect) and type(sprite) is PNJ:
                dialog_box.execute(sprite.dialog)
    def check_collision(self):
        #portail
        for portal in self.get_map().portal:
            if portal.from_world == self.current_map:
                point = self.get_objet(portal.origin_point)
                rect = pygame.Rect(point.x,point.y,point.width,point.height)


                if self.player.pied.colliderect(rect):
                    copy_portal = portal
                    self.current_map = portal.target_world
                    self.teleport_player(copy_portal.teleport_point)
        #mur
        for sprite in self.get_group().sprites():
            if type(sprite) is PNJ:
                if sprite.pied.colliderect(self.player.rect):
                    sprite.speed = 0
                else:
                    sprite.speed = 1
            if sprite.pied.collidelist(self.get_mur()) > -1:
                sprite.move_back()
    def check_herbe(self):
        self.montre += self.speed*8
        ok = 0
        if self.montre >= 100:
            for sprite in self.get_group().sprites():
                if ok == 0:
                    ok = 1
                    if sprite.pied.collidelist(self.get_herbe()) > -1:
                        nb = randrange(1,20)
                        if nb == 4:
                            pygame.mixer.music.pause()
                            i = Combat.__call__()
                            pygame.mixer.music.play()
                            if i == 0:
                                self.battu = 0
                            elif i == 1:
                                self.battu +=1
                            if self.battu== 5:
                                pygame.quit()
                                fin_jeux()
                                
                        self.montre = 0

        

    def teleport_player(self, name):
        point = self.get_objet(name)
        self.player.position[0] = point.x
        self.player.position[1] = point.y
        
    def enre_map(self,name,portal=[],pnjs=[]):
        #chargement carte
        tmx_data = pytmx.util_pygame.load_pygame(f"{name}.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data,self.screen.get_size())
        map_layer.zoom = 2
        
        #Collision
        mur = []
        for obj in tmx_data.objects:
            if obj.name == "collision":
                mur.append(pygame.Rect(obj.x,obj.y, obj.width, obj.height))

        #les haute herbes
        herbes = []
        for obj in tmx_data.objects:
            if obj.name == 'herbes':
                herbes.append(pygame.Rect(obj.x,obj.y, obj.width, obj.height))

        #dessiner le groupe de calque
        group = pyscroll.PyscrollGroup(map_layer=map_layer,default_layer=5)
        group.add(self.player)

        #ajouter les pnj
        for pnj in pnjs:
            group.add(pnj)

        # créer un objet map
        
        self.map[name] = Map(name,mur,herbes,group,tmx_data, portal,pnjs)
    
    def get_map(self):
        return self.map[self.current_map]
    
    def get_group(self):
        return self.get_map().group
    
    def get_mur(self):
        return self.get_map().walls
    def get_herbe(self):
        return self.get_map().herbes
    
    def get_objet(self,name):
        return self.get_map().tmx_data.get_object_by_name(name)
    
    def teleports_pnjs(self):
        for maps in self.map :
            map_data = self.map[maps]
            pnjs = map_data.pnjs
            
            for pnj in pnjs:
                pnj.charge_points(map_data.tmx_data)
                pnj.teleport_spawn()


    def draw(self):
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)

    
    def update(self):
        self.get_group().update()
        self.check_collision()
        

        for pnj in self.get_map().pnjs:
            pnj.move()