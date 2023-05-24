""" from os import walk
import pygame


pygame.init()
def import_folder(path):
    surface_list = []
        
    for _, _,img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    print(surface_list)

    return surface_list """

import pygame
import os

def import_folder(path):
    surface_list = []
        
    for _, _, img_files in os.walk(path):
        for image in img_files:
            full_path = os.path.join(path, image)
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list

# Example usage
pygame.init()
path = '../graphics/character/run'
surfaces = import_folder(path)
print(surfaces)
