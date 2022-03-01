import pygame
import time


class Animate:

    ANIM_FILES = []

    for i in range(1, 15):
        ANIM_FILES.append(pygame.image.load(
            f'pygame_experimenting/images/animation/anim{i}.png'))
    BLIT_IMG = ANIM_FILES[0]

    def __init__(self, screen):
        self.screen = screen

    def main(self, coords, blit1):
        for i in range(14):
            self.screen.blit(blit1, coords)
            self.screen.blit(Animate.ANIM_FILES[i], coords)
            pygame.display.flip()
            time.sleep(0.01)
        return
