import pygame
import project.setup.constants as constants


def display_time(screen, time_left):
    """
    This function displays the time the player has left before
    the enemy sprite comes in.
    :param screen: the screen where the time will be displayed
    :param time_left: the starting time left the player has
    :return: blits the time remaining
    """
    time_left_txt = 'Remaining Time: ' + str(time_left)

    font = pygame.font.SysFont('Consolas', 20, False, False)

    screen.blit(font.render(time_left_txt, True, constants.RED), (200, 50))
