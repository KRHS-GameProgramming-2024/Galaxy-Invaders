import pygame, sys, math, random
from Enemy import *
from Player import *
from Player2 import *

pygame.init()
clock = pygame.time.Clock();

size= [1500, 800]
screen = pygame.display.set_mode(size)



counter = 0;
player = PlayerShip(4, [1450/2, 1250/2])
ship = [player]

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit();
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.goKey("left")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.goKey("right")

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.goKey("sleft")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.goKey("sright")

            
    counter += 1
    if counter >= 100:
        counter = 0;
        Ships += [Ship("Enemyship.png", 
                [random.randint(-7,7), random.randint(-7,7)],
                [random.randint(100,700), random.randint(100, 500)])
          ]
        for ship in ships: 
            if ships[-1].shipCollide(ship):
                ships.remove(ships[-1])
                break
    
    for playerShip in Ship:
        playerShip.move()
        playerShip.wallCollide(size)
        
    for hittingplayerShip in Ship:
        for hitplayerShip in Ship:
            hittingplayerShip.shipCollide(hitplayerShip)

    screen.fill((97, 164, 229))
    for playerShip in Ships:
        screen.blit(player.image, ship.rect)
    pygame.display.flip()
    clock.tick(60)
    print(clock.get_fps()) 
