import pygame, sys, math
from Player2 import *

class PlayerShip(Ship):
    def __init__(self,maxSpeed=15, startPos=[0,0]):
        Ship.__init__(self, "player.png", [0,0], startPos)
        self.maxSpeed = maxSpeed

    def goKey(self, direction):
        if direction == "left":
            self.speedx = -self.maxSpeed
        elif direction == "right":
            self.speedx = self.maxSpeed
        elif direction == "sleft":
            self.speedx = 0
        elif direction == "sright":
            self.speedx = 0
            
  
