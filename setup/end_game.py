"""
Module that is responsible for displaying 'Game Over' or 'You Win'
"""

import pygame
import project.setup.constants as constants


class EndGame(object):
    def __init__(self):
        pygame.init()

        # Sets the font to None
        self.font = pygame.font.SysFont(None, 50)
        self.font2 = pygame.font.SysFont(None, 20)

    def draw_lose(self, screen):
        """
        Draws 'Game Over'

        :param screen: the window 'Game Over' will be displayed on
        """
        text = self.font.render("GAME OVER", True, constants.RED)
        text_rect = text.get_rect()

        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2

        play_again = self.font2.render("Play again? Press SPACEBAR.", True, constants.RED)
        play_rect = play_again.get_rect()

        play_x = screen.get_width() / 2 - play_rect.width / 2
        play_y = (screen.get_height() / 2 - play_rect.height / 2) + 30

        screen.blit(text, [text_x, text_y])
        screen.blit(play_again, [play_x, play_y])

    def draw_win(self, screen):
        """
        Draws 'You Win'

        :param screen: the window 'You Win' will be displayed on
        """
        text = self.font.render("YOU WIN", True, constants.GREEN)
        text_rect = text.get_rect()

        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2

        play_again = self.font2.render("Play again? Press SPACEBAR.", True, constants.GREEN)
        play_rect = play_again.get_rect()

        play_x = screen.get_width() / 2 - play_rect.width / 2
        play_y = (screen.get_height() / 2 - play_rect.height / 2) + 30

        screen.blit(text, [text_x, text_y])
        screen.blit(play_again, [play_x, play_y])
