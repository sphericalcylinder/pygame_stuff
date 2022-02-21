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

    def main(self, coords, other_blit):
        for i in range(14):
            for j in other_blit:
                self.screen.blit(j, coords)
            Animate.BLIT_IMG = Animate.ANIM_FILES[i]
            self.screen.blit(Animate.BLIT_IMG, coords)
            pygame.display.flip()
            time.sleep(0.01)
        return
