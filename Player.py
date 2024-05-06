import pygame, sys, math
from Ship import *


class PlayerShip(Ship):
    def __init__(self,maxSpeed=20, startPos=[0,0]):
        Ship.__init__(self, "Player/player.png", [0,0], startPos)
        self.maxSpeed = maxSpeed
        
        self.kind="player"

    def goKey(self, direction):
        if direction == "left":
            self.speedx = -self.maxSpeed
        elif direction == "right":
            self.speedx = self.maxSpeed
        elif direction == "up":
            self.speedy = -self.maxSpeed
        elif direction == "down":
            self.speedy = +self.maxSpeed
        elif direction == "sleft":
            self.speedx = 0
        elif direction == "sright":
            self.speedx = 0
            
    def wallCollide(self, size):
        width = size[0]
        height = size[1]
        if self.rect.left < 0:
            self.speedx = -self.speedx
        if self.rect.top < 0:
            self.speedy = -self.speedy
        if self.rect.right > width:
            self.speedx = -self.speedx
        if self.rect.bottom > height:
            self.speedy = -self.speedy
            
  
