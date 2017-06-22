#!/usr/bin/env python3.5

import pygame
from pygame.locals import *
import random
import sys
import time
import project.setup.constants as constants
from project.players.player import Player
import project.room as rooms
from project.players.ghost import Ghost
from project.setup.message_box import Pane
import project.setup.time_left as countdown
from project.setup.end_game import EndGame
import project.setup.check_answer as utilities
from project.setup.wall import Wall


def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    font = pygame.font.Font(None, 20)
    pygame.display.set_caption("Rooms of Horror")

    game_end = EndGame()
    textbox = Pane()
    status = 0
    answer = ""
    talk = False
    answer_time = False
    remove = False
    go = False

    # All initial lists
    active_sprite_list = pygame.sprite.Group()
    all_rooms = []
    current_room_no = 0

    # Create rooms
    all_rooms.append(rooms.Room1())
    all_rooms.append(rooms.Room2())
    all_rooms.append(rooms.Room3())
    all_rooms.append(rooms.Room4())
    current_room = all_rooms[current_room_no]

    # Create player
    player = Player()
    player.rect.x = 410
    player.rect.y = 180
    player.room = current_room
    active_sprite_list.add(player)

    # Create enemy
    enemy = Ghost()
    enemy.rect.x = random.randint(10, 590)
    enemy.rect.y = random.randint(10, 590)

    # Create trailing enemy
    enemy2 = Ghost()
    enemy2.rect.x = 275
    enemy2.rect.y = 535

    # Doors that block the next room
    door = Wall(0, 400, 10, 50, constants.BLUE)    # FIRST ROOM
    door2 = Wall(0, 325, 10, 55, constants.RED)    # SECOND ROOM
    door3 = Wall(270, 0, 50, 10, constants.GREEN)  # THIRD ROOM

    pygame.mixer.music.load('sounds/the_road.ogg')
    pygame.mixer.music.set_endevent(USEREVENT)
    pygame.mixer.music.play()

    # TIME COUNTDOWNS
    initial_time = 300
    time_left = 100
    COUNT_DOWN = USEREVENT + 1
    countdown.display_time(screen, time_left)
    countdown.display_time(screen, initial_time)
    pygame.time.set_timer(COUNT_DOWN, 1000)

    # Loop until the user clicks the close button.
    game_over = False
    game_win = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # QUITS THE GAME
                sys.exit()

            # Gives the user the ability to move their player
            if game_over is False and game_win is False and talk is False:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.go_left()
                    if event.key == pygame.K_RIGHT:
                        player.go_right()
                    if event.key == pygame.K_UP:
                        player.go_up()
                    if event.key == pygame.K_DOWN:
                        player.go_down()
                    if event.key == pygame.K_F3 and current_room_no != 3:
                        player.rect.x = 100
                        player.rect.y = 330
            else:
                # Restarts the entire game after a game over or game win
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and (game_over is True or game_win is True):
                            main()

            # List of all the furniture the player can interact with
            item_lists = current_room.item_list.sprites()

            # Allows the user to give their input and have it checked for correctness
            if talk is True and answer_time is True:
                if event.type == pygame.KEYDOWN:
                    if event.key == K_BACKSPACE:  # Deletes the last letter of user input
                        answer = answer[:-1]
                    elif event.key == K_RETURN:   # Submits user's answer for checking
                        talk = False
                        answer_time = False

                        # Checks the input user gave and changes the status accordingly
                        for c in item_lists:
                            if player.rect.colliderect(c):
                                if utilities.check_answer(status, answer, c.rect.x, c.rect.y) is True:
                                        initial_time = 300
                                        time_left = 100
                                        print(answer)
                                        status += 1
                                        break
                                elif utilities.check_answer(status, answer, c.rect.x, c.rect.y) is False:
                                    if (status == 4 or status == 5 or status == 15 or
                                            status == 18):
                                        if answer != "y":
                                            status = status
                                            break
                                        else:
                                            status += .1
                                            break
                                    elif status == 20:
                                        if answer != "origins":
                                            status = status
                                            break
                                        else:
                                            status += .1
                                            break
                                    elif status == 23:
                                        if answer != "y":
                                            status += .1
                                            break
                                    else:
                                        print(answer)
                                        time_left = 0
                        answer = ""
                    elif event.key == K_F2:  # Prevent F2 char from showing upon exiting dialogue
                        pass
                    else:  # Write user input to answer and displays it while typing
                        chars = event.key
                        answer += chr(chars)

            """
            STOPS THE PLAYER FROM WALKING FURTHER.
            """
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
                if event.key == pygame.K_UP and player.change_y < 0:
                    player.stop()
                if event.key == pygame.K_DOWN and player.change_y > 0:
                    player.stop()

            """
            RESTARTS THE MUSIC WHEN IT ENDS.
            """
            if event.type == USEREVENT:
                if current_room_no != 1:
                    pygame.mixer.music.load('sounds/the_road.ogg')
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load('sounds/crown_intro.ogg')
                    pygame.mixer.music.play()

            # Starts the count down
            if event.type == COUNT_DOWN:
                if initial_time != 0:
                    initial_time -= 1
                elif initial_time == 0:
                    if time_left != 0:
                        time_left -= 1

            """
            ALLOWS THE PLAYER TO MOVE ROOM TO ROOM.
            """
            if player.rect.x < -15:
                pygame.mixer.music.stop()
                if current_room_no == 0:
                    current_room_no = 1
                    current_room = all_rooms[current_room_no]
                    player.rect.y = 410
                    player.rect.x = 570
                    remove = False
                    door = door2

                elif current_room_no == 1:
                    current_room_no = 2
                    current_room = all_rooms[current_room_no]
                    player.rect.x = 570
                    player.rect.y = 410
                    remove = False
                    door = door3

            if player.rect.x > 615:
                pygame.mixer.music.stop()
                if current_room_no == 1:
                    current_room_no = 0
                    current_room = all_rooms[current_room_no]
                    player.rect.x = 10

                elif current_room_no == 2:
                    current_room_no = 1
                    current_room = all_rooms[current_room_no]
                    player.rect.x = 10
                    player.rect.y = 335

            if player.rect.y < -15:
                pygame.mixer.music.stop()
                current_room_no = 3
                current_room = all_rooms[current_room_no]
                player.rect.x = 285
                player.rect.y = 560

            if player.rect.y > 615:
                pygame.mixer.music.stop()
                current_room_no = 2
                current_room = all_rooms[current_room_no]
                player.rect.x = 285
                player.rect.y = 10

        #######################################################################
        # Update the player.
        player.update(current_room.wall_list, current_room.item_list)

        # Draw all the game items.
        current_room.draw(screen)
        active_sprite_list.draw(screen)
        #######################################################################

        # Displays the ghost to chase the player
        if time_left == 0:
            screen.blit(enemy.image, enemy.rect)
            if talk is False:
                if (status == 4.1 or status == 18.1 or status == 20.1 or
                        status == 23.1) and game_over is True:
                    enemy.speed = 20
                enemy.move_to_player(player)
            if player.rect.colliderect(enemy.rect):
                game_over = True
                game_end.draw_lose(screen)

        # Displays the countdown of how much time player has left
        if initial_time == 0:
            countdown.display_time(screen, time_left)

        """
        HANDLES THE DOORS OF EACH ROOM.
        """
        if current_room_no == 0:
            if status > 5:
                remove = True
        elif current_room_no == 1:
            if status > 12:
                remove = True
        elif current_room_no == 2:
            if status > 23:
                remove = True

        # Trailing ghost stage
        elif current_room_no == 3:
            if player.rect.y <= 500:
                go = True

            if go is True and game_over is False:
                screen.blit(enemy2.image, enemy2.rect)
                enemy2.auto_move(player)

                if event.type == pygame.KEYDOWN:
                    if event.key == K_DOWN and talk is False and game_win is False:
                        go = False
                        game_over = True

            if game_over is True:
                    screen.blit(enemy2.image, enemy2.rect)
                    enemy2.move_to_player(player)
                    game_end.draw_lose(screen)

        # Removes the door that blocks to the next room
        if remove is False:
            if player.rect.colliderect(door.rect):
                if player.change_x < 0:
                    player.rect.left = door.rect.right
                if player.change_y < 0:
                    player.rect.top = door.rect.bottom

            screen.blit(door.image, door.rect)

        #################################################################################

        # Handles all the status changing that doesn't require user input
        for c in item_lists:
            if player.rect.colliderect(c):
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_F1:    # Displays textbox
                        talk = True

                    elif event.key == pygame.K_F2:  # Removes textbox
                        talk = False
                        if answer_time is True:
                            answer_time = False
                        answer = ""

                if talk is True:  # Allows textbox to be displayed
                    textbox.draw(screen)
                    textbox.add_text(c.rect.x, c.rect.y, status, current_room_no, screen)
                    print(c.rect)

                if status == 0:
                    if c.rect.x == 420 and c.rect.y == 155:
                        if talk is True:
                            status = 1
                if status == 1:
                    if talk is True:
                        if c.rect.x == 155 and c.rect.y == 165:
                            answer_time = True
                if status == 2:
                    if talk is True:
                        if c.rect.x == 110 and c.rect.y == 155:
                            answer_time = True
                if status == 3:
                    if c.rect.x == 110 and c.rect.y == 155:
                        if talk is True:
                            status = 4
                if status == 4:
                    if talk is True:
                        if (c.rect.x == 80 and c.rect.y == 143) or \
                                ((c.rect.x == 462 or c.rect.x == 513 or c.rect.x == 563) and
                                 c.rect.y == 360):
                            answer_time = True

                if status == 4.1:
                    if c.rect.x == 155 and c.rect.y == 165:
                        if talk is True:
                            time_left = 0
                            game_over = True

                if status == 5:
                    if c.rect.x == 155 and c.rect.y == 165:
                        if talk is True:
                            answer_time = True

                if status == 6:
                    if c.rect.x == 510 and c.rect.y == 320:
                        if talk is True:
                            status = 7

                if 7 <= status <= 11:  # BED
                    if c.rect.x == 510 and c.rect.y == 320:
                        if talk is True:
                            answer_time = True

                if status == 12:
                    if c.rect.x == 280 and c.rect.y == 405:
                        if talk is True:
                            status = 13

                if status == 13:
                        if c.rect.x == 420 and c.rect.y == 115:
                            status = 14

                if 13 <= status <= 14:
                    if talk is True:
                        if c.rect.x == 420 and c.rect.y == 115:
                            answer_time = True
                if status == 15:
                    if talk is True:
                        if c.rect.x == 380 and c.rect.y == 102:
                            answer_time = True

                if status == 16:
                    if talk is True:
                        if c.rect.x == 380 and c.rect.y == 102:
                            status = 17

                if status == 17:
                    if talk is True:
                        if c.rect.x == 350 and c.rect.y == 145:
                            status = 18

                if status == 18:
                    if talk is True:
                        if (c.rect.x == 200 and c.rect.y == 280) or \
                                (c.rect.x == 185 and c.rect.y == 170) or \
                                (c.rect.x == 300 and c.rect.y == 250) or \
                                (c.rect.x == 530 and c.rect.y == 465):
                            answer_time = True

                if status == 18.1:
                    if c.rect.x == 350 and c.rect.y == 145:
                        if talk is True:
                            time_left = 0
                            game_over = True

                if status == 19:
                    if talk is True:
                        if c.rect.x == 350 and c.rect.y == 145:
                            status = 20

                if status == 20:
                    if talk is True:
                        if c.rect.x == 200 and c.rect.y == 115:
                            answer_time = True

                if status == 20.1:
                    if c.rect.x == 200 and c.rect.y == 115:
                        if talk is True:
                            time_left = 0
                            game_over = True

                if status == 21:
                    if talk is True:
                        if c.rect.x == 200 and c.rect.y == 115:
                            status = 22

                if status == 22:
                    if talk is True:
                        if (c.rect.x == 485 and c.rect.y == 110) or \
                                (c.rect.x == 365 and c.rect.y == 127) or \
                                (c.rect.x == 70 and c.rect.y == 310):
                            answer_time = True

                if status == 23:
                    if talk is True:
                        if c.rect.x == 260 and c.rect.y == 335:
                            answer_time = True

                if status == 23.1:
                    if c.rect.x == 260 and c.rect.y == 335:
                        if talk is True:
                            time_left = 0
                            game_over = True

                if status == 24:
                    if c.rect.x == 285 and c.rect.y == 95:
                        if talk is True:
                            game_win = True

                if game_win is True:
                    game_end.draw_win(screen)

                if current_room_no == 3:
                    if talk is True:
                        if (c.rect.x == 70 and c.rect.y == 305) or \
                                (c.rect.x == 520 and c.rect.y == 305):
                            game_over = True

        ################################################################################

        if answer_time is True and talk is True:
            block = font.render("Enter your answer: ", False, (255, 255, 255))
            block2 = font.render(answer, False, (255, 255, 255))
            screen.blit(block, (20, 82))
            screen.blit(block2, (150, 82))

        print("STATUS: ", status)

        clock.tick(20)  # Limit to 20 frames per second

        # Updates the changes
        pygame.display.flip()

pygame.quit()

if __name__ == "__main__":
    main()
