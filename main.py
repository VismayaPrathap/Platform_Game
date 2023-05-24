import pygame
import sys
from levelmap import *
from level import Level
# from tiles import Tile


pygame.init()

win = pygame.display.set_mode((700, sHeight))
pygame.display.set_caption("Mario")
level = Level(level_map, win)

# tile_group = pygame.sprite.Group(Tile((250,250),100))


def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
        win.fill('black')
        level.run()
        # tile_group.draw(win)
        pygame.display.update()


main()