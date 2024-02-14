import pygame, sys, math, random
from Enemy import *
from Player import *
from Player2 import *

pygame.init()
clock = pygame.time.Clock();

size= [1500, 800]
screen = pygame.display.set_mode(size)



counter = 0;
player = PlayerBall(4, [1450/2, 1250/2])
balls = [player]

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
        balls += [Ball("Enemyship.png", 
                [random.randint(-7,7), random.randint(-7,7)],
                [random.randint(100,700), random.randint(100, 500)])
          ]
        for ball in balls: 
            if balls[-1].ballCollide(ball):
                balls.remove(balls[-1])
                break
    
    
    for ball in balls:
        ball.move()
        ball.wallCollide(size)
        
    for hittingBall in balls:
        for hitBall in balls:
            hittingBall.ballCollide(hitBall)
    

    screen.fill((97, 164, 229))
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    pygame.display.flip()
    clock.tick(60)
    print(clock.get_fps()) 
