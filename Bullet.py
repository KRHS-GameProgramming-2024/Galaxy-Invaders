import pygame, sys, math
from Ship import *

class Bullet(Ship):
    def __init__(self,speed, startPos=[0,0]):
        Ship.__init__(self, "Bullet/Bullet.png", speed, startPos)
        
