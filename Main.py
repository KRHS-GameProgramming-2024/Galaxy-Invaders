import pygame, sys, math, random
from Enemy import *
from Player import *
from Ship import *

pygame.init()
clock = pygame.time.Clock();
size= [1500, 800]
screen = pygame.display.set_mode(size)



mode="play"

while True:
    bg=pygame.image.load('Screens/space.png')

    counter = 0;
    player = PlayerShip(4, [1450/2, 1250/2])
    ships = [player]
    bullets =[]

    shootOdds = 225

    while mode=="play":
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.goKey("left")
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.goKey("right")
                elif event.key == pygame.K_w:
                    player.goKey("up")
                elif event.key == pygame.K_s:
                    player.goKey("down")
                elif event.key == pygame.K_f:
                    bullets += [player.shoot("player", "up")]
                
                

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.goKey("sleft")
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.goKey("sright")
                elif event.key == pygame.K_f:
                    player.goKey("sup")

                
        counter += 1
        if counter >= 30:
            counter = 0;
            shipImiges =["Enemy/Enemyship.png",
                         "Enemy/Enemyship2.png",
                         "Enemy/Enemyship3.png"]
            image = shipImiges[random.randint(0,2)]
            ships += [Ship(image,
                     [5,0],
                     [400,25])]
                     
              
            for ship in ships: 
                if ships[-1].shipCollide(ship):
                    ships.remove(ships[-1])
                    break
        
        for ship in ships:
            ship.move()
            ship.wallCollide(size)
            if ship.kind=="enemy":
                if random.randint(0,shootOdds)==0:
                    bullets += [ship.shoot("enemy", "down")]
        
        for bullet in bullets:
            bullet.move()
            if bullet.wallCollide(size):
                bullets.remove(bullet)
                
            for ship in ships:
                if not ship == ships[0]:
                    if bullet.shipCollide(ship):
                        ships.remove(ship)
                        bullets.remove(bullet)
            
            
        for hittingplayerShip in ships:
            for hitplayerShip in ships:
               if hittingplayerShip.shipCollide(hitplayerShip):
                   if hittingplayerShip.kind == "player":
                       ships.remove(ships[0])

        if ships[0].kind!="player":
            mode="game over"

        screen.fill((97, 164, 229))
        screen.blit(bg,[0,0])
        for ship in ships:
            screen.blit(ship.image,ship.rect)
        for bullet in bullets:
            screen.blit(bullet.image,bullet.rect)
        pygame.display.flip()
        clock.tick(60)
        #print(clock.get_fps()) 

    bg=pygame.image.load('Screens/GameOver.png')

    while mode=="game over":
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mode="play"
        screen.fill((97, 164, 229))
        screen.blit(bg,[0,0])
        pygame.display.flip()
        clock.tick(60)
