import pygame
from check_key import check_key


class Letter_Switcher():

    IMG_LIST = []
    NUM_IMG_LIST = []
    for i in range(1, 6):
        NUM_IMG_LIST.append(pygame.image.load(f'pygame_experimenting/images/tile{i}.png'))
    for i in range(1, 28):
        IMG_LIST.append(pygame.image.load(f'pygame_experimenting/images/tiles/tilex{i}.png'))
    BLIT_IMG = NUM_IMG_LIST[0]
    SCREEN_DIM = 500, 500
    SIZE = (30, 60)

    def __init__(self, keyboard: bool):
        self.keyboard = keyboard

    def switch_to(self, letter):
        check_key(Letter_Switcher, letter, self.keyboard)
