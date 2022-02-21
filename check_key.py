import pygame


class Check():

    def __init__(self):
        self.IMG_LIST = []
        self.NUM_IMG_LIST = []
        for i in range(1, 6):
            self.NUM_IMG_LIST.append(pygame.image.load(
                f'pygame_experimenting/images/tile{i}.png'))
        for i in range(1, 28):
            self.IMG_LIST.append(pygame.image.load(
                f'pygame_experimenting/images/tiles/tilex{i}.png'))

        self.BLIT_IMG = self.NUM_IMG_LIST[0]

    def check_key(self, key, mode):
        if mode:
            match key:
                case pygame.K_1:
                    self.BLIT_IMG = self.NUM_IMG_LIST[0]
                case pygame.K_2:
                    self.BLIT_IMG = self.NUM_IMG_LIST[1]
                case pygame.K_3:
                    self.BLIT_IMG = self.NUM_IMG_LIST[2]
                case pygame.K_4:
                    self.BLIT_IMG = self.NUM_IMG_LIST[3]
                case pygame.K_5:
                    self.BLIT_IMG = self.NUM_IMG_LIST[4]
                case pygame.K_a:
                    self.BLIT_IMG = self.IMG_LIST[0]
                case pygame.K_b:
                    self.BLIT_IMG = self.IMG_LIST[1]
                case pygame.K_c:
                    self.BLIT_IMG = self.IMG_LIST[2]
                case pygame.K_d:
                    self.BLIT_IMG = self.IMG_LIST[3]
                case pygame.K_e:
                    self.BLIT_IMG = self.IMG_LIST[4]
                case pygame.K_f:
                    self.BLIT_IMG = self.IMG_LIST[5]
                case pygame.K_g:
                    self.BLIT_IMG = self.IMG_LIST[6]
                case pygame.K_h:
                    self.BLIT_IMG = self.IMG_LIST[7]
                case pygame.K_i:
                    self.BLIT_IMG = self.IMG_LIST[8]
                case pygame.K_j:
                    self.BLIT_IMG = self.IMG_LIST[9]
                case pygame.K_k:
                    self.BLIT_IMG = self.IMG_LIST[10]
                case pygame.K_l:
                    self.BLIT_IMG = self.IMG_LIST[11]
                case pygame.K_m:
                    self.BLIT_IMG = self.IMG_LIST[12]
                case pygame.K_n:
                    self.BLIT_IMG = self.IMG_LIST[13]
                case pygame.K_o:
                    self.BLIT_IMG = self.IMG_LIST[14]
                case pygame.K_p:
                    self.BLIT_IMG = self.IMG_LIST[15]
                case pygame.K_q:
                    self.BLIT_IMG = self.IMG_LIST[16]
                case pygame.K_r:
                    self.BLIT_IMG = self.IMG_LIST[17]
                case pygame.K_s:
                    self.BLIT_IMG = self.IMG_LIST[18]
                case pygame.K_t:
                    self.BLIT_IMG = self.IMG_LIST[19]
                case pygame.K_u:
                    self.BLIT_IMG = self.IMG_LIST[20]
                case pygame.K_v:
                    self.BLIT_IMG = self.IMG_LIST[21]
                case pygame.K_w:
                    self.BLIT_IMG = self.IMG_LIST[22]
                case pygame.K_x:
                    self.BLIT_IMG = self.IMG_LIST[23]
                case pygame.K_y:
                    self.BLIT_IMG = self.IMG_LIST[24]
                case pygame.K_z:
                    self.BLIT_IMG = self.IMG_LIST[25]
                case _:
                    self.BLIT_IMG = self.IMG_LIST[26]
        elif not mode:
            match key:
                case 1:
                    self.BLIT_IMG = self.NUM_IMG_LIST[0]
                case 2:
                    self.BLIT_IMG = self.NUM_IMG_LIST[1]
                case 3:
                    self.BLIT_IMG = self.NUM_IMG_LIST[2]
                case 4:
                    self.BLIT_IMG = self.NUM_IMG_LIST[3]
                case 5:
                    self.BLIT_IMG = self.NUM_IMG_LIST[4]
                case 'a':
                    self.BLIT_IMG = self.IMG_LIST[0]
                case 'b':
                    self.BLIT_IMG = self.IMG_LIST[1]
                case 'c':
                    self.BLIT_IMG = self.IMG_LIST[2]
                case 'd':
                    self.BLIT_IMG = self.IMG_LIST[3]
                case 'e':
                    self.BLIT_IMG = self.IMG_LIST[4]
                case 'f':
                    self.BLIT_IMG = self.IMG_LIST[5]
                case 'g':
                    self.BLIT_IMG = self.IMG_LIST[6]
                case 'h':
                    self.BLIT_IMG = self.IMG_LIST[7]
                case 'i':
                    self.BLIT_IMG = self.IMG_LIST[8]
                case 'j':
                    self.BLIT_IMG = self.IMG_LIST[9]
                case 'k':
                    self.BLIT_IMG = self.IMG_LIST[10]
                case 'l':
                    self.BLIT_IMG = self.IMG_LIST[11]
                case 'm':
                    self.BLIT_IMG = self.IMG_LIST[12]
                case 'n':
                    self.BLIT_IMG = self.IMG_LIST[13]
                case 'o':
                    self.BLIT_IMG = self.IMG_LIST[14]
                case 'p':
                    self.BLIT_IMG = self.IMG_LIST[15]
                case 'q':
                    self.BLIT_IMG = self.IMG_LIST[16]
                case 'r':
                    self.BLIT_IMG = self.IMG_LIST[17]
                case 's':
                    self.BLIT_IMG = self.IMG_LIST[18]
                case 't':
                    self.BLIT_IMG = self.IMG_LIST[19]
                case 'u':
                    self.BLIT_IMG = self.IMG_LIST[20]
                case 'v':
                    self.BLIT_IMG = self.IMG_LIST[21]
                case 'w':
                    self.BLIT_IMG = self.IMG_LIST[22]
                case 'x':
                    self.BLIT_IMG = self.IMG_LIST[23]
                case 'y':
                    self.BLIT_IMG = self.IMG_LIST[24]
                case 'z':
                    self.BLIT_IMG = self.IMG_LIST[25]