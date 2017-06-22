"""
This module is used to pull individual sprites from sprite sheets.
"""
import pygame
import project.setup.constants as constants


class SpriteSheet:
    """ Class used to grab images out of a sprite sheet. """
    # This points to our sprite sheet image
    sprite_sheet = None

    def __init__(self, file_name):
        """ Constructor. Pass in the file name of the sprite sheet. """

        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert_alpha()

    def get_image(self, x, y, width, height):
        """
        Grab a single image out of a larger spritesheet
        :param x: the x-coordinate location of the sprite
        :param y: the y-coordinate location of the sprite
        :param width: the width of the sprite
        :param height: the height of the sprite
        :return image: returns the image of the sprite from the spritesheet
        """

        # Create a new blank image
        image = pygame.Surface([width, height]).convert()
        image.fill(constants.BLUE)

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Assuming blue works as the transparent color
        image.set_colorkey(constants.BLUE)

        # Returns the image
        return image
