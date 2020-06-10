import pygame
import sys
from pygame.locals import *
from settings import Settings


def main():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((
        settings.screen_width, settings.screen_height))
    screen.fill(settings.bg_color)
    pygame.display.set_caption('FUckY Sudoku')

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


if __name__ == "__main__":
    main()
