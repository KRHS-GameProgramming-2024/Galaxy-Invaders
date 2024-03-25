import pygame
pygame.init()
pygame.mixer.init()

SONGEND = pygame.USEREVENT

print

while True:
	number = input("Press a number: ")


	if number == "1":
		print("")
		pygame.mixer.music.load("")
		pygame.mixer.music.queue( , , -1)
		pygame.mixer.music.play()	
