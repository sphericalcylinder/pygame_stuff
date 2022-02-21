import pygame
#from letter_switcher import Letter_Switcher as ls
from check_key import Check
from animate import Animate
import string
import random
import time

pygame.init()

KEY_INPUT = False

SCREEN_DIM = WIDTH, HEIGHT = 500, 500
SCREEN = pygame.display.set_mode(SCREEN_DIM)
pygame.display.set_caption("Testing")

if KEY_INPUT:
	pygame.event.set_allowed([pygame.KEYDOWN, pygame.QUIT])
else:
	pygame.event.set_allowed([pygame.QUIT])


anim = Animate(SCREEN)

check = Check()

letter_list = []
flip_list = [
	[Check(), (0, 0)],
	[Check(), (50, 0)],
	[Check(), (100, 0)],
	[Check(), (150, 0)],
	[Check(), (200, 0)],
]



while True:
	SCREEN.fill((255, 255, 255))

	if not KEY_INPUT:

		for x in flip_list:
			x[0].check_key(''.join(random.choices(string.ascii_letters+string.digits,k=1)), KEY_INPUT)


		SCREEN.blit(flip_list[0][0].BLIT_IMG, flip_list[0][1])
		SCREEN.blit(flip_list[1][0].BLIT_IMG, flip_list[1][1])
		SCREEN.blit(flip_list[2][0].BLIT_IMG, flip_list[2][1])
		SCREEN.blit(flip_list[3][0].BLIT_IMG, flip_list[3][1])
		SCREEN.blit(flip_list[4][0].BLIT_IMG, flip_list[4][1])
	elif KEY_INPUT:
		SCREEN.blit(check.BLIT_IMG, (0, 0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		elif KEY_INPUT and event.type == pygame.KEYDOWN:
			check.check_key(event.key, KEY_INPUT)
			anim.main((0, 0), [check.BLIT_IMG])

	pygame.display.flip()
