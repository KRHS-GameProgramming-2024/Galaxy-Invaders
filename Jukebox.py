import pygame
pygame.init()
pygame.mixer.init()

SONGEND = pygame.USEREVENT

print("Space Theme")

while True:
	number = input("Press a number: ")


	if number == "1":
		print("Space")
		pygame.mixer.music.load("Sounds/Space.mp3")
		pygame.mixer.music.queue("Sounds/Space.mp3", "mp3", -1)
		pygame.mixer.music.play()	
