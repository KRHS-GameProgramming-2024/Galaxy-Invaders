import pygame, sys, math, random
from Enemy import *
from Player import *
from Ship import *

pygame.init()
clock = pygame.time.Clock();
size= [1500, 800]
screen = pygame.display.set_mode(size)



counter = 0;
player = PlayerShip(4, [1450/2, 1250/2])
ships = [player]
bullets =[]

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit();
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.goKey("left")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.goKey("right")
            elif event.key == pygame.K_w:
                bullets += [player.shoot()]
            
            

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.goKey("sleft")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.goKey("sright")

            
    counter += 1
    if counter >= 100:
        counter = 0;
        ships += [Ship("Enemy/Enemyship.png",
                 [5,0],
                 [400,25])]
          
    for ship in ships: 
            if ships[-1].shipCollide(ship):
                ships.remove(ships[-1])
                break
    
    for ship in ships:
        ship.move()
        ship.wallCollide(size)
    
    for bullet in bullets:
        bullet.move()
        bullet.wallCollide(size)
        
    for hittingplayerShip in ships:
        for hitplayerShip in ships:
            hittingplayerShip.shipCollide(hitplayerShip)

    screen.fill((97, 164, 229))
    for ship in ships:
        screen.blit(ship.image,ship.rect)
    for bullet in bullets:
        screen.blit(bullet.image,bullet.rect)
    pygame.display.flip()
    clock.tick(60)
    print(clock.get_fps()) 
