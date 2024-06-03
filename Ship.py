import pygame, sys, math
from Bullet import *
from Wall import *

class Ship():
    def __init__(self, image, speed = [0,0], startPos=[0,0]):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.size = (self.rect.height/10 + self.rect.width/10)/2
    
        self.rect = self.rect.move(startPos)
        
        self.didBounceX = False
        self.didBounceY = False
        
        self.kind="enemy"

    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)

    def wallCollide(self, size):
        width = size[0]
        height = size[1]
        if self.rect.left < 0:
            self.speedx = -self.speedx
            self.rect.move_ip([self.speedx,75])
            
        if self.rect.right > width:
            self.speedx = -self.speedx
            self.rect.move_ip([self.speedx,75])
        
        if self.rect.bottom > height:
            self.die()
            
    def die(self):
        pass
        
    def shoot(self, owner, direction):
        speed=[0,0]
        if direction =="up":
            speed=[0, -20]
        elif direction == "down":
            speed=[0, 20]
        return Bullet(owner, speed, self.rect.center)

    def shipCollide(self, other):
        if self != other:
            if self.rect.right>other.rect.left:
                if self.rect.left<other.rect.right:
                    if self.rect.bottom>other.rect.top:
                        if self.rect.top<other.rect.bottom:
                            if self.getDist(other) < self.size + other.size:
                                if not self.didBounceX:
                                    self.speedx = -self.speedx
                                    self.didBounceX = True
                                if not self.didBounceY:
                                    self.speedy = -self.speedy
                                    self.didBounceY = True
                                return True
        return False
                                
    def getDist(self, other):
        x1 = self.rect.centerx
        x2 = other.rect.centerx
        y1 = self.rect.centery
        y2 = other.rect.centery
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)

