"""
This module is responsible for setting up all the rooms. Each have different wall and 
item placements that will be used accordingly throughout the game.
"""

import pygame

import project.setup.constants as colors
from project.setup.wall import Wall
import project.setup.items as items
import project.setup.constants as constants


class Room:
    """ Base class for all rooms. """

    """
    Each room has a list of walls, items, background items,
    and a background.
    """
    wall_list = None
    background = None
    item_list = None
    bg_list = None

    def __init__(self):
        """ Constructor, create the lists. """
        self.wall_list = pygame.sprite.Group()
        self.item_list = pygame.sprite.Group()
        self.bg_list = pygame.sprite.Group()

    def update(self):
        """ Update everything in this room."""
        self.wall_list.update()
        self.bg_list.upate()
        self.item_list.update()

    def draw(self, screen):
        """
        This function draws everything from the bg_list, wall_list,
        item_list, and background.

        :param screen: The screen the items will be drawn on.
        """
        screen.fill(constants.DARK_GRAY)

        if self.background is not None:
            screen.blit(self.background, (0,0))

        self.bg_list.draw(screen)
        self.wall_list.draw(screen)
        self.item_list.draw(screen)


class Room1(Room):
    """This creates all the walls  and items in Room 1"""
    def __init__(self):
        Room.__init__(self)
        # Makes the walls. (x_pos, y_pos, width, height)

        """
        This is a list of walls. Each is in the form [x, y, width, height, color]
        Each of the walls' arguments are put according to a Wall Class and
        is added to the wall list.
        """
        walls = [[0, 150, 10, 250, colors.BLACK],    # left
                 [0, 450, 10, 60, colors.BLACK],     # bottom left
                 [590, 150, 10, 350, colors.BLACK],  # right
                 [0, 500, 615, 10, colors.BLACK],    # bottom

                 [200, 155, 10, 75, colors.BLACK],   # TOP RIGHT
                 [400, 155, 10, 75, colors.BLACK],   # TOP RIGHT #2
                 [400, 270, 10, 80, colors.BLACK],   # BOTTOM RIGHT
                 [200, 350, 400, 10, colors.BLACK],  # LONG BOTTOM

                 [200, 270, 10, 190, colors.BLACK],  # DOWN MIDDLE ENTRANCE
                 [240, 400, 10, 100, colors.BLACK],  # DOWN
                 [280, 360, 10, 100, colors.BLACK],  # UP
                 [320, 400, 10, 100, colors.BLACK],  # DOWN
                 [360, 360, 10, 100, colors.BLACK],  # UP
                 [400, 400, 10, 100, colors.BLACK],  # DOWN
                 [440, 360, 10, 100, colors.BLACK],  # UP ITEM #1
                 [490, 360, 10, 100, colors.BLACK],  # UP ITEM #2
                 [540, 360, 10, 100, colors.BLACK],  # UP ITEM #3

                 [0, 0, 600, 110, colors.BLACK],
                 [0, 510, 600, 110, colors.BLACK],]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        """
        These are all the background items that the player can go over
        and are simply for aesthetics to the room. They are then each
        added to the bg_list.
        """
        bg_items = [[items.MAIN_WALL, 0, 110],
                    [items.RED_CARPET, 449, 361],
                    [items.RED_CARPET, 499, 361],
                    [items.RED_CARPET, 549, 361],
                    [items.CHAIR, 275, 310],  # RIGHT CHAIR
                    [items.CHAIR, 220, 310],  # LEFT CHAIR
                    [items.CHAIR, 248, 285],  # TOP CHAIR
                    [items.CHAIR, 248, 330],  # BOTTOM CHAIR
                    [items.CHAIR, 375, 310],  # RIGHT CHAIR
                    [items.CHAIR, 320, 310],  # LEFT CHAIR
                    [items.CHAIR, 348, 285],  # TOP CHAIR
                    [items.CHAIR, 348, 330],  # BOTTOM CHAIR
                    ]

        for furniture in bg_items:
            block = items.Item(furniture[0])
            block.rect.x = furniture[1]
            block.rect.y = furniture[2]
            self.bg_list.add(block)

        """
        These are all the furniture that the player can approach and interact with.
        These items are added to the item_list.
        """
        level = [
                  [items.CHEST, 420, 155],
                  [items.DESK, 11, 150],
                  [items.DESK, 565, 135],
                  [items.LONG_DESK, 34, 150],
                  [items.PANDA_DESK, 80, 143],
                  [items.PANDA, 462, 360],
                  [items.PANDA, 513, 360],
                  [items.PANDA, 563, 360],

                  [items.TABLE, 240, 300],
                  [items.TABLE, 340, 300],

                  [items.MIRROR, 495, 112],
                  [items.MIRROR, 325, 112],
                  [items.HAT_RACK, 365, 127],

                  [items.AWARDS, 44, 120],
                  [items.AWARDS, 290, 120],
                  [items.BOOKSHELF, 210, 135],
                  [items.BOOKSHELF, 235, 135],
                  [items.BOOKSHELF, 260, 135],
                  [items.BAGGAGE, 110, 155],

                  [items.BED, 450, 155],
                  [items.BED_DOWN, 450, 310],
                  [items.BED, 530, 155],
                  [items.BED_DOWN, 530, 310],

                  [items.CARPET, 525, 230],
                  [items.CARPET_DOWN, 447, 230],

                  [items.CANDY, 155, 165],
                  [items.BONE, 185, 170],
                  [items.BONE, 300, 250]
                  ]

        for furniture in level:
            block = items.Item(furniture[0])
            block.rect.x = furniture[1]
            block.rect.y = furniture[2]
            self.item_list.add(block)


class Room2(Room):
    """This creates all the walls, background items, and furniture in Room 2"""
    def __init__(self):
        Room.__init__(self)
        # Uses the checkerboard.png image as the background
        self.background = pygame.image.load("images/checkerboard.png").convert()

        """
        This is a list of walls. Each is in the form [x, y, width, height]
        Each of the walls' arguments are put according to a Wall Class and
        is added to the wall list.
        """
        walls = [[0, 0, 10, 250, colors.BLACK],
                 [0, 300, 10, 25, colors.BLACK],
                 [0, 380, 10, 250, colors.BLACK],
                 [0, 0, 600, 300, colors.BLACK],
                 [10, 590, 760, 10, colors.BLACK],
                 [10, 500, 580, 100, colors.BLACK],
                 [590, 0, 10, 400, colors.BLACK],
                 [590, 450, 10, 170, colors.BLACK],

                 [100, 200, 100, 180, colors.BLACK],
                 [380, 200, 100, 180, colors.BLACK],

                 [100, 380, 1, 45, colors.BLACK],
                 [199, 380, 1, 45, colors.BLACK],
                 [380, 380, 1, 45, colors.BLACK],
                 [479, 380, 1, 45, colors.BLACK]]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        """
        These are all the background items that the player can go over
        and are simply for aesthetics to the room. Each are added to
        the bg_list.
        """
        bg_items = [[items.MAIN_WALL, 0, 280],
                    [items.WALL, 100, 380],
                    [items.WALL, 380, 380],
                    [items.CHAIR, 330, 480],
                    [items.CHAIR, 227, 480]
                    ]

        for furniture in bg_items:
            block = items.Item(furniture[0])
            block.rect.x = furniture[1]
            block.rect.y = furniture[2]
            self.bg_list.add(block)

        """
        These are all the furniture that the player can approach and interact with.
        These items are added to the item_list.
        """
        level = [[items.CANDY, 280, 405],
                 [items.BED, 510, 320],
                 [items.BOOKSHELF, 250, 300],
                 [items.BOOKSHELF, 275, 300],
                 [items.BOOKSHELF, 300, 300],

                 [items.PHOTO, 110, 390],
                 [items.PHOTO, 160, 390],
                 [items.PHOTO, 390, 390],
                 [items.PHOTO, 440, 390],
                 [items.PANDA_DESK, 70, 310],

                 [items.AWARDS, 30, 300],
                 [items.AWARDS, 210, 300],
                 [items.AWARDS, 340, 300],
                 [items.AWARDS, 552, 300],

                 [items.TABLE, 240, 470],
                 [items.TABLE, 300, 470]]

        for furniture in level:
            block = items.Item(furniture[0])
            block.rect.x = furniture[1]
            block.rect.y = furniture[2]
            self.item_list.add(block)


class Room3(Room):
    """This creates all the walls, background items, and furniture in Room 3"""
    def __init__(self):
        Room.__init__(self)

        """
        This is a list of walls. Each is in the form [x, y, width, height]
        Each of the walls' arguments are put according to a Wall Class and
        is added to the wall list.
        """

        walls = [[0, 0, 50, 600, colors.BLACK],     # LEFT WALL
                 [0, 590, 600, 10, colors.BLACK],   # BOTTOM WALL
                 [550, 0, 50, 400, colors.BLACK],   # RIGHT UPPER WALL
                 [550, 450, 50, 400, colors.BLACK],

                 [0, 0, 270, 100, colors.BLACK],    # LEFT UPPER WALL
                 [320, 0, 270, 100, colors.BLACK],  # RIGHT UPPER WALL
                 [0, 500, 600, 140, colors.BLACK],

                 [269, 100, 1, 45, colors.BLACK],
                 [320, 100, 1, 45, colors.BLACK]]
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        """
        These are all the background items that the player can go over
        and are simply for aesthetics to the room. They are then each
        added to the bg_list.
        """
        bg_items = [[items.WALL, 50, 100],
                    [items.WALL, 150, 100],
                    [items.WALL, 170, 100],

                    [items.WALL, 320, 100],
                    [items.WALL, 420, 100],
                    [items.WALL, 500, 100],

                    [items.FULL_CARPET, 160, 250],
                    ]
        for furniture in bg_items:
            block = items.Item(furniture[0])
            block.rect.x = furniture[1]
            block.rect.y = furniture[2]
            self.bg_list.add(block)

        """
        These are all the furniture that the player can approach and interact with.
        These items are added to the item_list.
        """
        level = [[items.DINNER_TABLE, 200, 280],
                 [items.CHAIR, 220, 265],
                 [items.CHAIR, 350, 335],
                 [items.CHAIR, 260, 265],
                 [items.CHAIR, 305, 265],
                 [items.CHAIR, 260, 335],
                 [items.CHAIR, 305, 335],

                 [items.PHOTO, 83, 110],
                 [items.TV, 125, 115],
                 [items.TV_HELP, 420, 115],
                 [items.RADIO, 200, 115],
                 [items.HAT_RACK, 485, 110],
                 [items.MIRROR, 380, 102],
                 [items.CANDY, 350, 145],

                 [items.VASE, 254, 120],
                 [items.VASE, 315, 120],
                 [items.VASE, 49, 120],
                 [items.VASE, 530, 120],
                 [items.VASE, 49, 465],
                 [items.VASE, 530, 465]]

        for furniture in level:
            block = items.Item(furniture[0])
            block.rect.x = furniture[1]
            block.rect.y = furniture[2]
            self.item_list.add(block)


class Room4(Room):
    """This creates all the walls, background items, and furniture in Room 4"""
    def __init__(self):
        Room.__init__(self)

        # Uses the checkerboard.png image as the background
        self.background = pygame.image.load("images/checkers.png").convert()

        """
        This is a list of walls. Each is in the form [x, y, width, height]
        Each of the walls' arguments are put according to a Wall Class and
        is added to the wall list.
        """
        walls = [[0, 0, 50, 600, colors.BLACK],    # LEFT WALL
                 [0, 0, 600, 50, colors.BLACK],  # TOP WALL
                 [550, 0, 50, 600, colors.BLACK],  # RIGHT UPPER WALL

                 [0, 550, 270, 50, colors.BLACK],    # LEFT LOWER WALL
                 [320, 550, 250, 50, colors.BLACK],  # RIGHT LOWER WALL

                 [269, 95, 1, 195, colors.BLACK],
                 [269, 340, 1, 210, colors.BLACK],
                 [320, 95, 1, 195, colors.BLACK],
                 [320, 340, 1, 195, colors.BLACK],

                 [50, 290, 220, 1, colors.BLACK],
                 [50, 340, 220, 1, colors.BLACK],
                 [320, 290, 228, 1, colors.BLACK],
                 [320, 340, 228, 1, colors.BLACK]]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        """
        These are all the background items that the player can go over
        and are simply for aesthetics to the room. They are then each
        added to the bg_list.
        """
        bg_items = [[items.MAIN_WALL, 0, 50],
                    [items.CARPET_HORIZON, 270, 566],
                    [items.CARPET_VERTICAL, 236, 290],
                    [items.CARPET_MIDDLE, 270, 290],
                    [items.CARPET_VERTICAL, 320, 290],
                    [items.CARPET_HORIZON, 270, 256]
                    ]

        #  Responsible for all the carpet patterns
        y_offset = 566
        while y_offset >= 362:
            bg_items.append([items.CARPET_HORIZON, 270, y_offset-34])
            y_offset -= 32

        x_offset = 240
        while x_offset >= 36:
            bg_items.append([items.CARPET_VERTICAL, x_offset-32, 290])
            x_offset -= 32

        x_offset = 320
        while x_offset <= 550:
            bg_items.append([items.CARPET_VERTICAL, x_offset+32, 290])
            x_offset += 32

        y_offset = 256
        while y_offset >= 100:
            bg_items.append([items.CARPET_HORIZON, 270, y_offset-34])
            y_offset -= 32

        for furniture in bg_items:
            block = items.Item(furniture[0])
            block.rect.x = furniture[1]
            block.rect.y = furniture[2]
            self.bg_list.add(block)

        """
        These are all the furniture that the player can approach and interact with.
        These items are added to the item_list.
        """
        level = [
                 [items.VASE, 49, 70],
                 [items.VASE, 530, 70],
                 [items.VASE, 49, 515],
                 [items.VASE, 530, 515],

                 [items.TAO, 285, 95],
                 [items.PANDA, 70, 305],
                 [items.CANDY, 520, 305]
                  ]

        for furniture in level:
            block = items.Item(furniture[0])
            block.rect.x = furniture[1]
            block.rect.y = furniture[2]
            self.item_list.add(block)
