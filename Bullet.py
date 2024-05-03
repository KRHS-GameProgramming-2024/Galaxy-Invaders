import pygame, sys, math
from Ship import *

class Bullet(Ship):
    def __init__(self,speed, startPos=[0,0]):
        Ship.__init__(self, "Bullet/Bullet.png", speed, startPos)
        self.rad = (self.rect.height/50 + self.rect.width/50)/50
    

    
    def shipCollide(self,ship):
        if ship.rect.left <= self.rect.right:
            if ship.rect.right >= self.rect.left:
                if ship.rect.top <= self.rect.bottom:
                    if ship.rect.bottom >= self.rect.top:
                        print('collishon')
                        return True
        return False
