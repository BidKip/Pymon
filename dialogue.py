import pygame

class DialogBox():
    X_POSITION = 60
    Y_POSITION = 470
    def __init__(self):
        self.box = pygame.image.load('dialog_box.png')
        self.box= pygame.transform.scale(self.box,(700,100))
        self.txts = []
        self.text_index = 0
        self.letter_index = 0
        self.font = pygame.font.Font('dialog_font.ttf',18)
        self.reading = False

    def execute(self,dialog=[]):
        if self.reading:
            self.next_txt()
        else:
            self.reading = True
            self.text_index = 0
            self.txts = dialog
    
    def render(self,screen):
        if self.reading:
            self.letter_index += 1
            if self.letter_index >= len(self.txts[self.text_index]):
                self.letter_index = self.letter_index
            screen.blit(self.box,(self.X_POSITION,self.Y_POSITION))
            txt = self.font.render(self.txts[self.text_index][0:self.letter_index],False,(0,0,0))
            screen.blit(txt,(self.X_POSITION+60,self.Y_POSITION+30))
    
    def next_txt(self):
        self.text_index += 1
        self.letter_index = 0
        
        if self.text_index >= len(self.txts):
            # ferme le dialogue
            self.reading = False