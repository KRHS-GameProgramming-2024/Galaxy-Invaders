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
            
  
    class Player:
        def __init__(self):
            self.position = [0,0]
            self.direction = [1,
    0]
            self.shoot_cooldown = 0.5
            self.last_shot_time = 0
            
    def shoot(self):
        current.time() == time.time()
    if current_time - self.last_shot_time > self.shoot_cooldown:
        import time
        player = Player()
    while True:
        user_input = input("Press 'W' to shoot")
    if user_input.lower() == "w":
        player.shoot()
