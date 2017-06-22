import pygame
from project.setup.spritesheet_functions import SpriteSheet

"""
Module that contains all the room furniture and items.

These constants define our item types:
 - Name of file
 - X location of sprite
 - Y location of sprite
 - Width of sprite
 - Height of sprite
"""

MAIN_WALL       = (0, 0, 600, 45)
WALL            = (0, 0, 100, 45)
FLOOR           = (311, 47, 90, 60)

TAO             = (263, 85, 22, 33)

FULL_CARPET     = (291, 47, 271, 136)
CARPET_VERTICAL = (187, 160, 34, 50)
CARPET_HORIZON  = (185, 47, 50, 34)
CARPET_MIDDLE   = (225, 160, 50, 50)

RADIO           = (244, 47, 38, 36)
TV_HELP         = (238, 121, 51, 33)
TV              = (185, 121, 51, 33)

VASE            = (237, 84, 21, 33)
DINNER_TABLE    = (0, 158, 181, 59)

CANDY           = (84, 93, 13, 12)
BONE            = (38, 72, 8, 4)
PANDA           = (23, 71, 14, 17)
PANDA_DESK      = (0, 49, 22, 37)
DESK            = (125, 80, 22, 30)
LONG_DESK       = (125, 47, 45, 30)
BOOKSHELF       = (156, 123, 22, 32)
RED_CARPET      = (23, 54, 43, 15)
TABLE           = (55, 84, 27, 28)
CHAIR           = (38, 77, 10, 11)
AWARDS          = (25, 90, 27, 22)
BED             = (39, 114, 30, 41)
BED_DOWN        = (70, 114, 30, 41)
CARPET          = (0, 113, 38, 42)
CARPET_DOWN     = (117, 113, 38, 42)
MIRROR          = (66, 47, 24, 36)
HAT_RACK        = (91, 46, 33, 45)
BAGGAGE         = (0, 88, 24, 23)
CHEST           = (101, 98, 13, 8)
PHOTO           = (151, 83, 31, 24)


class Item(pygame.sprite.Sprite):
    """ The items that are used in each room """

    def __init__(self, sprite_sheet_data):
        # Item constructor
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("images/furniture.png")
        # Grab the image for this item using x & y coordinates along with width and height
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
        self.rect = self.image.get_rect()
