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
            if self.speedx < 0:
                self.speedx = 0
        elif direction == "sright":
            if self.speedx > 0:
                self.speedx = 0
        elif direction == "sup":
            if self.speedy < 0:
                self.speedy = 0
        elif direction == "sdown":
            if self.speedy > 0:
                self.speedy = 0
            
    def wallCollide(self, size):
        width = size[0]
        height = size[1]
        if self.rect.left < 0:
            self.speedx = 0
        if self.rect.top < 0:
            self.speedy = 0
        if self.rect.right > width:
            self.speedx = 0
        if self.rect.bottom > height:
            self.speedy = 0
            
  
