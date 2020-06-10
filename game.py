import pygame, sys
from pygame.locals import *


window_width, window_height = 800, 700

def main():
    global FPSCLOCK, window
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('FUckY Sudoku')

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()



if __name__ == "__main__":
    main()
