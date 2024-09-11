import pygame, sys, math, random
from Enemy import *
from Player import *
from Ship import *
from Wall import *
from Hud import *
from bolt import *

pygame.mixer.init()


pygame.init()
clock = pygame.time.Clock();
size= [1500, 800]
screen = pygame.display.set_mode(size)

mode="start"
pygame.mixer.music.load("Sounds/Space.mp3", "mp3")
pygame.mixer.music.play(loops = -1)

while True:
    bg=pygame.image.load('Screens/start.png')
    pygame.event.set_grab(False)
    while mode=="start":
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                     mode="play"
            
    
        screen.blit(bg,[0,0])
        pygame.display.flip()
        clock.tick(60)

    
   

    bg=pygame.image.load('Screens/space.png')

    counter = 0;
    player = PlayerShip(4, [1450/2, 1250/2])
    ships = [player]
    bullets =[]
    kills=HUD("kills: ", 0)
    
    timer=HUD("time: ", 0, [0,75])
    timeCounter=0
    
    fps=60

    shootOdds = 225
    pygame.event.set_grab(True)
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
                    bullets += [player.shootbolt("player", "up")]
               
                elif event.key == pygame.K_RETURN:
                    mode="game over"
                
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.goKey("sleft")
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.goKey("sright")
                elif event.key == pygame.K_w:
                    player.goKey("sup")
                elif event.key == pygame.K_s:
                    player.goKey("sdown")
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    bullets += [player.shoot("player", "up", event.pos)]
                elif event.button == 3:
                    bullets += [player.shootWall("player", "up")]

                
        counter += 1
        if counter >= 30:
            counter = 0;
            shipImiges =["Enemy/Enemyship.png",
                         "Enemy/Enemyship2.png",
                         "Enemy/Enemyship3.png"]
            image = shipImiges[random.randint(0,2)]
            ships += [Ship(image,
                     [5,0],
                     [40,25])]
                     
              
            for ship in ships: 
                if ships[-1].shipCollide(ship):
                    ships.remove(ships[-1])
                    break
                    
        timeCounter+=1
        if timeCounter==fps:
            timeCounter=0
            timer.increase()
        
        for ship in ships:
            ship.move()
            ship.wallCollide(size)
            if ship.kind=="enemy":
                if random.randint(0,shootOdds)==0:
                    bullets += [ship.shoot("enemy", "down")]
        
        for bullet in bullets:
            if bullet.kind=="wall":
                bullet.move(player.rect.center)
            else:
                bullet.move()
            if bullet.wallCollide(size):
                bullets.remove(bullet)
                break
            
            if bullet.kind=="bullet":
                for ship in ships:
                    if not ship == ships[0]:
                        if bullet.shipCollide(ship):
                            ships.remove(ship)
                            bullets.remove(bullet)
                            kills.increase()
                            break

                    else:
                        if bullet.shipCollide(ship):
                            bullets.remove(bullet)
                            mode="game over"
                            break       
                            
            if bullet.kind=="bolt":
                for ship in ships:
                    if not ship == ships[0]:
                        if bullet.shipCollide(ship):
                            ships.remove(ship)
                            kills.increase()                                    
                            break
                    else:
                        if bullet.shipCollide(ship):
                            bullets.remove(bullet)
                            mode="game over"
                            break
                            
            
            for b in bullets:
                if bullet.kind=="bullet" and b.kind=="wall":
                    if bullet.bulletCollide(b):
                        if bullet in bullets:
                            bullets.remove(bullet)
                            break
            
            
            
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
        screen.blit(kills.image,kills.rect)
        screen.blit(timer.image,timer.rect)
        pygame.display.flip()
        clock.tick(60)
        #print(clock.get_fps()) 

    bg=pygame.image.load('Screens/GameOver.png')
    pygame.event.set_grab(False)
    while mode=="game over":
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mode="play"
                elif event.key == pygame.K_SPACE:
                    mode="start"
        screen.fill((97, 164, 229))
        screen.blit(bg,[0,0])
        pygame.display.flip()
 
        clock.tick(fps)

        clock.tick(60)

