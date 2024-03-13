import pygame, sys, math
from Ship import *

class Bullet(Ship):
    def __init__(self,speed, startPos=[0,0]):
        Ship.__init__(self, "Bullet/Bullet.png", speed, startPos)
        self.rad = (self.rect.height/50 + self.rect.width/50)/50
