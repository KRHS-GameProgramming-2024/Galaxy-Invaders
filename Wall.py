import pygame, sys, math
from Bullet import *

class Wall(Bullet):
     def __init__(self,owner, speed, startPos=[0,0]):
        Bullet.__init__(self,owner, speed, startPos)
        self.image = pygame.image.load( "Bullet/wall.gif")
        self.rect = self.image.get_rect(center=startPos)
        self.size = (self.rect.height/10 + self.rect.width/10)/2
    
        self.rad = (self.rect.height/50 + self.rect.width/50)/50
        self.kind="wall"
