import pygame


class Wall(pygame.sprite.Sprite):
    """
    This class represents the walls that make up each room.
    """

    def __init__(self, x, y, width, height, color):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Make a wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        """
        Get the height and width of the image and assign them
        to the parameters x and y.
        """

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
