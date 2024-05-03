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
            
    
            
  
