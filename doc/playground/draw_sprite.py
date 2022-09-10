
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
        # SUPER ? ? ? why does this return a non iterable error
        pg.sprite.Sprite.__init__(self, self.containers)
        # need self.image & self.rect as minimum instance variables for any 
        #   sprite
        self.image = self.images[0]
        self.rect = self.image.get_rect()

    def set_position(self, x, y) -> None:
        width = self.rect.width
        height = self.rect.height
        self.rect.update(x, y, width, height)

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
    King.images = [load_image("doc/playground/kingy.png")]
    # containers are all lists that are 
    #   supposed to contain every instance 
    #   of king
    # so we are setting self.containers to 
    #   kings, but it doesn't get used until
    King.containers = kings
    #   here
    king1 = King()
    king2 = King()
    king2.set_position(50, 30)
    # dirty means something has been changed but the changes haven't been 
    #   applied/saved yet
    # draw the sprites in the kings group to the background
    dirty = kings.draw(background)
    # update the screen
    pg.display.update(dirty)
    # create clock object to set up the number of frames per second
    clock = pg.time.Clock()
    # create infinite loop until the escape key is pressed
    going = True
    while going:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                going = False
            # turn the screen blue
            elif event.type == pg.KEYDOWN and event.key == pg.K_b:
                background.fill((0, 127, 255))
        # display initial background
        screen.blit(background, (0, 0))
        # takes screen & shows it to the player
        pg.display.flip()
    # quit the game
    pg.quit() 