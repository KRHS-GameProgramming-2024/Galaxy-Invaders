import pygame, sys, math

class HUD():
    def __init__(self,basetext, startvalue, startPos=[0,0]):
        self.font = pygame.font.Font(None, 64)
        self.value=startvalue
        self.basetext=basetext
        self.image = self.font.render(self.basetext+" "+str(self.value), True, (255, 255, 255))
        self.rect = self.image.get_rect(topleft=startPos)

    def increase(self):
        self.value+=1
        self.image = self.font.render(self.basetext+" "+str(self.value), True, (255, 255, 255))
        self.rect = self.image.get_rect(topleft  = self.rect.topleft)


   
