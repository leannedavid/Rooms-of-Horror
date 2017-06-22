"""
This module is used to hold the Player class that the user controls
"""
import pygame
from project.setup.spritesheet_functions import SpriteSheet


class Player(pygame.sprite.Sprite):
    """
    This class represents the character
    """

    # Sets speed vector of player
    change_x = 0
    change_y = 0

    # Holds all the images for the walking animation of the player
    walking_frames_l = []
    walking_frames_r = []
    walking_frames_u = []
    walking_frames_d = []

    # Direction the player is facing
    direction = "D"

    # List of sprites we can bump against
    room = None

    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Calls the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("images/taomei_spritesheet.png")

        # Loads all the LEFT facing images into a list
        image = sprite_sheet.get_image(0, 99, 21, 30)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(26, 99, 21, 30)
        self.walking_frames_l.append(image)

        # Loads all the RIGHT facing images into a list
        image = sprite_sheet.get_image(0, 66, 21, 30)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(26, 66, 21, 30)
        self.walking_frames_r.append(image)

        # Loads all the BACK facing images into a list
        image = sprite_sheet.get_image(0, 33, 24, 30)
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_image(26, 33, 24, 30)
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_image(0, 33, 24, 30)
        self.walking_frames_u.append(image)
        image = sprite_sheet.get_image(52, 33, 24, 30)
        self.walking_frames_u.append(image)

        # Loads all the FRONT facing images into a list
        image = sprite_sheet.get_image(0, 0, 24, 30)
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_image(26, 0, 24, 30)
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_image(0, 0, 24, 30)
        self.walking_frames_d.append(image)
        image = sprite_sheet.get_image(52, 0, 24, 30)
        self.walking_frames_d.append(image)

        # Sets the initial image of the player
        self.image = self.walking_frames_d[0]

        # Sets a reference to the image rectangle
        self.rect = self.image.get_rect()
        self.walls = None

    def update(self, walls, items):
        """
        Function to update the player when walking and running into certain
        walls and furniture.

        :param walls: the walls of the current room
        :param items: the furniture in the current room
        """

        # Move left/right
        self.rect.x += self.change_x
        pos_x = self.rect.x
        pos_y = self.rect.y

        if self.direction == "R":
            frame = (pos_x // 30) % len(self.walking_frames_r)
            print(frame)
            self.image = self.walking_frames_r[frame]
        elif self.direction == "L":
            frame = (pos_x // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
        elif self.direction == "U":
            frame = (pos_y // 30) % len(self.walking_frames_u)
            print(frame)
            self.image = self.walking_frames_u[frame]
        else:
            frame = (pos_y // 30) % len(self.walking_frames_u)
            print(frame)
            self.image = self.walking_frames_d[frame]

        """
        WALL X-DIRECTION
        """
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # If moving right, set player's right side to the left side of
            # the item they hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise, if moving left, do the opposite
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        """
        ITEMS X-DIRECTION
        """
        # Check for collision
        block_hit_list = pygame.sprite.spritecollide(self, items, False)

        for block in block_hit_list:
            # print("HIT! X-DIRECTION")

            # If moving right, set player's right side to the left side of the item they hit
            if self.change_x > 0:
                self.rect.right = block.rect.left + 1
            elif self.change_x < 0:
                # Otherwise, if moving left, do the opposite
                self.rect.left = block.rect.right - 1

        """
        WALLS Y-DIRECTION
        """
        # Check for collision
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)

        for block in block_hit_list:
            # Reset player's position based on the top/bottom of the object
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

        """
        ITEMS Y-DIRECTION
        """
        block_hit_list = pygame.sprite.spritecollide(self, items, False, pygame.sprite.collide_mask)
        for block in block_hit_list:
            # print("HIT! Y-DIRECTION")

            # Reset player's position based on the top/bottom of the object
            if self.change_y > 0:
                self.rect.bottom = block.rect.top + 1
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom - 1

    """
    PLAYER-CONTROL MOVEMENT:
    """
    def go_left(self):
        """ Called when user presses the left arrow key """
        self.change_x = -5
        self.direction = "L"

    def go_right(self):
        """ Called when user presses the right arrow key """
        self.change_x = 5
        self.direction = "R"

    def go_up(self):
        """ Called when user presses the up arrow key """
        self.change_y = -5
        self.direction = "U"

    def go_down(self):
        """ Called when user presses the down arrow key """
        self.change_y = 5
        self.direction = "D"

    def stop(self):
        """ Called when user doesn't press any of the arrow keys """
        self.change_x = 0
        self.change_y = 0
