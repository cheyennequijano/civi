
import pygame as pg
import os

def load_image(file):
    """loads an image, prepares it for play"""
    try:
        surface = pg.image.load(file)
    except pg.error:
        raise SystemExit(f'Could not load image "{file}" {pg.get_error()}')
    return surface.convert()

class King(pg.sprite.Sprite):

    def __init__(self) -> None:
        # super returns the parent class
        # so this returns the same constructor
        #   as Sprite
        super().__init__(self, self.containers)

if __name__ == "__main__":
    # initialize pygame
    pg.init()
    # create the screen
    screen = pg.display.set_mode((400, 400), pg.SCALED)
    # create a background
    #   the same size as screen
    background = pg.Surface(screen.get_size())
    # have background be the same format as screen
    background = background.convert()
    # color fill
    background.fill((255, 200, 0))
    # create group for King class
    kings = pg.sprite.RenderUpdates()
    King.images = [load_image("kingy.png")]
    # containers are all lists that are 
    #   supposed to contain every instance 
    #   of king
    # so we are setting self.containers to 
    #   kings, but it doesn't get used until
    King.containers = kings
    #   here
    king = King()

    smelly = 