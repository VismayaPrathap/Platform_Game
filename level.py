import pygame
from tiles import Tile
from levelmap import tileSize

class Level:
    def __init__(self,level_data,surface):
        self.world_shift = -1
        self.display_surface =surface
        self.setup_level(level_data)

    
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                if cell == 'x':
                    x = col_index * tileSize
                    y = row_index * tileSize
                    tile = Tile((x,y),tileSize)
                    self.tiles.add(tile)



    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        