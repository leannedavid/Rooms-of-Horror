"""
The enemy module
"""
import pygame
import math


class Ghost(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/ghost_emoji.png")
        self.rect = self.image.get_rect()
        self.speed = 3

    def move_to_player(self, player):
        """
        Function will take account of the player's coordinates and will move
        closer to them at the speed set.

        :param player: the player the ghost will chase
        """
        dx, dy = self.rect.x - player.rect.x, self.rect.y - player.rect.y

        dist = math.hypot(dx, dy)

        if dist == 0:
            dist = 1
        else:
            dx, dy = dx / dist, dy / dist

        self.rect.x -= dx * self.speed
        self.rect.y -= dy * self.speed

    def auto_move(self, player):
        self.rect.x = player.rect.x - 8
        self.rect.y = player.rect.bottom + 5
