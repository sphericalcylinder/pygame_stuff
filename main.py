import pygame
#from letter_switcher import Letter_Switcher as ls
from check_key import Check
from animate import Animate
import string
import random


while True:
	try:
		mode = int(input("What mode would you like? (1, 2, or 3) "))
		if mode < 4 and mode > 0:
			break
		else:
			raise ValueError
	except:
		print("Invalid input. Try again.\n")
		continue

if mode == 1:
	KEY_INPUT = False
	AUTO_INPUT = False
if mode == 2:
	KEY_INPUT = True
	AUTO_INPUT = False
if mode == 3:
	KEY_INPUT = False
	AUTO_INPUT = True
	WORD = input("What word would you like to display? ").lower()

pygame.init()

SCREEN_DIM = WIDTH, HEIGHT = 500, 500
SCREEN = pygame.display.set_mode(SCREEN_DIM)
pygame.display.set_caption("Testing")

if KEY_INPUT:
	pygame.event.set_allowed([pygame.KEYDOWN, pygame.QUIT])
else:
	pygame.event.set_allowed([pygame.QUIT])


anim = Animate(SCREEN)
check = Check()

if not KEY_INPUT and not AUTO_INPUT:

	flip_list = [
		[Check(), (0, 0)],
		[Check(), (50, 0)],
		[Check(), (100, 0)],
		[Check(), (150, 0)],
		[Check(), (200, 0)],
	]

	for x in flip_list:
		x[0].check_key(''.join(random.choices(string.ascii_lowercase,k=1)), KEY_INPUT)
		SCREEN.blit(x[0].BLIT_IMG, x[1])

	count = 0

if AUTO_INPUT and not KEY_INPUT:
	letter_list = []
	count2 = 0

	word_len = len(WORD)
	if word_len > 10:
		raise Exception("Too long a word!")
	coord1 = 0
	for g in range(word_len):
		letter_list.append([Check(), (coord1, 0), WORD[g]])
		coord1 += 50

	for m in letter_list:
		m[0].check_key(m[2], KEY_INPUT)



while True:
	pygame.display.update()
	#SCREEN.fill((255, 255, 255))

	if not KEY_INPUT and not AUTO_INPUT:

		if count <= 5:
			for x in flip_list:
				x[0].check_key(''.join(random.choices(string.ascii_lowercase,k=1)), KEY_INPUT)
				anim.main(x[1], x[0].BLIT_IMG)
				SCREEN.blit(x[0].BLIT_IMG, x[1])

		else:
			flip_list[0][0].check_key('h', KEY_INPUT)
			anim.main(flip_list[0][1], flip_list[0][0].BLIT_IMG)
			flip_list[1][0].check_key('e', KEY_INPUT)
			anim.main(flip_list[1][1], flip_list[1][0].BLIT_IMG)
			flip_list[2][0].check_key('l', KEY_INPUT)
			anim.main(flip_list[2][1], flip_list[2][0].BLIT_IMG)
			flip_list[3][0].check_key('l', KEY_INPUT)
			anim.main(flip_list[3][1], flip_list[3][0].BLIT_IMG)
			flip_list[4][0].check_key('o', KEY_INPUT)
			anim.main(flip_list[4][1], flip_list[4][0].BLIT_IMG)
			break
			#SCREEN.blit(x[0].BLIT_IMG, x[1])

		pygame.display.update()
		count += 1
			

	if AUTO_INPUT and not KEY_INPUT:
		if count2 <= 5:
			for e in letter_list:
				e[0].check_key(''.join(random.choices(string.ascii_lowercase,k=1)), KEY_INPUT)
				anim.main(e[1], e[0].BLIT_IMG)
				SCREEN.blit(e[0].BLIT_IMG, e[1])

		else:
			for y in letter_list:
				y[0].check_key(y[2], KEY_INPUT)
				anim.main(y[1], y[0].BLIT_IMG)
				SCREEN.blit(y[0].BLIT_IMG, y[1])
			break
			
		pygame.display.update()
		count2 += 1

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		elif KEY_INPUT and not AUTO_INPUT and event.type == pygame.KEYDOWN:
			check.check_key(event.key, KEY_INPUT)
			anim.main((0, 0), check.BLIT_IMG)

	pygame.display.update()

while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

	pygame.display.flip()
