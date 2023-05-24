import pygame
from tiles import Tile
from levelmap import tileSize, sWidth
from player import Player

class Level:
    def __init__(self, level_data,surface):
        self.world_shift = 0
        self.display_surface = surface
        self.setup_level(level_data)

    
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                x = col_index * tileSize
                y = row_index * tileSize
                if  cell == 'x':
                    tile = Tile((x,y),tileSize)
                    self.tiles.add(tile)
                if  cell == 'P':
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if(player_x < sWidth/4 and direction_x < 0):
            self.world_shift = 8
            player.speed = 0
        elif(player_x > (sWidth -(sWidth/2)) and direction_x > 0):
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 7

    def horz_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if(sprite.rect.colliderect(player.rect)):
                if(player.direction.x < 0):
                    player.rect.left = sprite.rect.right
                elif(player.direction.x > 0):
                    player.rect.right = sprite.rect.left
    
    def vert_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        
        for sprite in self.tiles.sprites():
            if(sprite.rect.colliderect(player.rect)):
                if(player.direction.y > 0):
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif(player.direction.y < 0):
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
    

    
    
    def run(self):
        #tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()
        
        #players
        self.player.update()
        self.player.draw(self.display_surface)
        self.vert_movement_collision()
        self.horz_movement_collision()
        
        