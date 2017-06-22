import pygame
import project.setup.constants as constants


class Pane(object):
    def __init__(self):
        pygame.init()
        # Sets the font to Arial size 16
        self.font = pygame.font.SysFont('Arial', 12 , True)

        # Sets the image of the dialogue box
        self.image = pygame.image.load("images/dialogue_box.png").convert()

    def draw(self, screen):
        """
        Draws the dialogue box that text will be on top of.

        :param screen: the screen the dialogue box will be drawn on
        """
        screen.blit(self.image, (30, 480))

    def add_text(self, x, y, status, room, screen):
        """
        Displays the correct text depending on the item's coordinates,
        the status of the game, and the current room.

        :param x: the x-coordinate location of the item
        :param y: the y-coordinate location of the item
        :param status: the current status of the game
        :param room: the current room
        :param screen: the screen the text will be displayed on
        """

        message = ""

        """
        ALL THE MESSAGES MEANT FOR ROOM 1
        """
        if room == 0:
            if x == 420 and y == 155:  # CHEST
                message = "34.0928° N, 118.3287° W"

            if x == 155 and y == 165:  # CANDY
                message = "\"........................\""

            if x == 11 and y == 150:
                message = "A regular dresser. It doesn't seem to budge open."

            if x == 34 and y == 150:
                message = "A long dresser. You noticed a lock in the top middle drawer."

            if x == 80 and y == 143:
                message = "A small stuffed panda lays on top of the dresser."

            if (x == 300 and y == 250) or (x == 185 and y == 170):
                message = "A small, white bone. It must belong to Candy."

            if x == 290 and y == 120:
                message = "Two first-place music awards sit still on the stand."

            if x == 365 and y == 127:
                message = "Three hats of the same style sits comfortably on the rack."

            if (x == 210 or x == 235 or x == 260) and y == 135:
                    message = "Stacks of books are placed neatly on the bookshelf."

            if ((x == 450 or x == 530) and y == 155) or ((x == 450 or x == 530) and y == 310):
                    message = "A comfy bed. An image of you and someone flashes in your mind."

            if x == 110 and y == 155:
                    message = "A big luggage. Seems to be lock at the moment."

            if (x == 325 or x == 495) and y == 112:
                    message = "An image of you stares straight back at you on the mirror, winking."

            if (x == 240 or x == 340) and y == 300:
                    message = "A pair of sunglasses lays on the table undisturbed."

            if (x == 462 or x == 513 or x == 563) and y == 360:
                message = "A panda sits comfortably on the floor, staring deep into your soul."

            if x == 447 and y == 230:
                message = "You flip the rug and the numbers 930502 are shown underneath."

            if x == 525 and y == 230:
                message = "You flip the rug and the numbers 150723 are shown underneath."

            #  Status when player has interacted with the chest/box
            if status == 1:
                if x == 155 and y == 165:
                    message = "\"Where do you think those coordinates lead to?\""
                elif x == 210 and y == 135:
                    message = "A book fell out and a page about Cabrillo Beach appears before you."
                elif x == 235 and y == 135:
                    message = "A book fell out and a page about Hollywood appears before you."
                elif x == 260 and y == 135:
                    message = "A book fell out and a page about Bradbury Building appears before you."

            #  Status for the luggage
            if status == 2:
                if x == 155 and y == 165:
                    message = "< - - - - - -"
                if x == 110 and y == 155:
                    message = "Looking closely you can see a combo lock on the luggage."
                if x == 11 and y == 150:
                    message = "You carefully open the drawer and the numbers 111226 are embedded."

            #  Status when the luggage is opened
            if status >= 3:
                if x == 110 and y == 155:
                    message = "The luggage open and inside you see a sharp knife. You take it."

            #  Status to choose eyes to bring for Candy to open the door
            if status == 4:
                if x == 155 and y == 165:
                    message = "\"Choose your eyes carefully and bring them to me.\""
                if x == 110 and y == 155:
                    message = "The luggage open and inside you see a sharp knife. You take it."
                if x == 80 and y == 143:
                    message = "The beady eyes of the the panda turned blue. Slash it? (Y/N)"
                if x == 462 and y == 360:
                    message = "The beady eyes of the the panda turned green. Slash it? (Y/N)"
                if x == 513 and y == 360:
                    message = "The beady eyes of the the panda turned yellow. Slash it? (Y/N)"
                if x == 563 and y == 360:
                    message = "The beady eyes of the the panda turned red. Slash it? (Y/N)"

            # Bad Ending #1: Brought the wrong eyes
            if status == 4.1:
                if x == 155 and y == 165:
                    message = "\"You brought me the wrong eyes and now you must pay the price.\""
                if (x == 80 and y == 143) or ((x == 462 or x == 513 or x == 563) and y == 360):
                    message = "The eyes that used to stare at you have been savagely ripped out."

            # Status for confirming to go to the next room
            if status == 5:
                if x == 155 and y == 165:
                    message = "\"It's either go or die. Are you ready for this?\" (Y/N)"
                if (x == 80 and y == 143) or ((x == 462 or x == 513 or x == 563) and y == 360):
                    message = "The eyes that used to stare at you have been savagely ripped out."

            # Status for Candy after completing the first room
            if status >= 6:
                if x == 155 and y == 165:
                    message = "\"You shouldn't stay here. Go to the next room quickly.\""
                if (x == 80 and y == 143) or ((x == 462 or x == 513 or x == 563) and y == 360):
                    message = "The eyes that used to stare at you have been savagely ripped out."

            # Status when finding the code to the 'HELP' monitor
            if status == 14:
                if x == 420 and y == 155:  # CHEST
                    message = "1105"

            # Status when finding food for Candy
            if status == 18:
                if x == 185 and y == 170:
                    message = "A bone lays near Candy as she stares holes into you. Take it anyway? (Y/N)"
                if x == 300 and y == 250:
                    message = "You can feel a pair of eyes as you look at the bone. Take it anyway? (Y/N)"

            # Status when finding a hat based on the radio's words
            if status == 22:
                if x == 365 and y == 127:
                    message = "You think about what the cassette said. Take a hat? (Y/N)"

        """
          ALL THE MESSAGES FOR ROOM 2
        """
        if room == 1:
            if x == 280 and y == 405:
                message = "\"....................\""
            if x == 510 and y == 320:
                message = "_  _  _  _  _  _  _"
            if (x == 250 or x == 275 or x == 300) and y == 300:
                message = "Stacks of books are placed neatly on the bookshelf."
            if (x == 110 or x == 160 or x == 390 or x == 440) and y == 390:
                message = "The simple portrait looks like it's smiling eerily back at you."
            if x == 70 and y == 310:
                message = "A regular dresser. It doesn't seem to budge open."
            if (x == 30 or x == 210 or x == 340 or x == 552) and y == 300:
                message = "Two music awards stand still on display. They seemed recently polished."
            if (x == 240 or x == 300) and y == 470:
                message = "A beach-themed table with a pair of sunglasses at its corner."

            # Status when searching for the first letter of hangman
            if status == 7:
                if x == 280 and y == 405:  # CANDY
                    message = "\"The answer is a lot closer than you think.\""
                if x == 250 and y == 300:
                    message = "A book fell out and the letter 'H' is written in big font on a page."
                if x == 275 and y == 300:
                    message = "A book fell out and the letter 'E' is written in big font on a page."
                if x == 300 and y == 300:
                    message = "A book fell out and the letter 'Y' is written in big font on a page."

            # Status when searching for second and fifth letter of hangman
            if status == 8:
                if x == 280 and y == 405:
                    message = "\"The answer is simple yet complicated if you don't know the right word.\""
                if x == 510 and y == 320:
                    message = "H  _  _  _  _  _  _"
                if x == 110 and y == 390:
                    message = "Black ink seeps out of the portrait and the letter 'W' is formed."
                if x == 160 and y == 390:
                    message = "Black ink seeps out of the portrait and the letter 'A' is formed."
                if x == 390 and y == 390:
                    message = "Black ink seeps out of the portrait and the letter 'V' is formed."
                if x == 440 and y == 390:
                    message = "Black ink seeps out of the portrait and the letter 'E' is formed."

            # Status when searching for the third letter of hangman
            if status == 9:
                if x == 280 and y == 405:
                    message = "\"Look and listen closer, the answer is right there.\""
                if x == 510 and y == 320:
                    message = "H  A  _  _  A  _  _"
                if x == 70 and y == 310:
                    message = "Panda: 'D', First drawer: 'I', Second drawer: 'E'"

            # Status when searching for the fourth letter of hangman
            if status == 10:
                if x == 280 and y == 405:
                    message = "\"Have you figured it out yet?\""
                if x == 510 and y == 320:
                    message = "H  A  I  _  A  _  _"
                if x == 30 and y == 300:
                    message = "Looking closely, you see the letter 'L' reflected on the awards."
                if x == 210 and y == 300:
                    message = "Looking closely, you see the letter 'O' reflected on the awards."
                if x == 340 and y == 300:
                    message = "Looking closely, you see the letter 'V' reflected on the awards."
                if x == 552 and y == 300:
                    message = "Looking closely, you see the letter 'E' reflected on the awards."

            # Status when searching for the last two letters of hangman
            if status == 11:
                if x == 280 and y == 405:
                    message = "\"Couldn't it have been any more obvious?\""
                if x == 510 and y == 320:
                    message = "H  A  I  L  A  _  _"
                if x == 240 and y == 470:
                    message = "You noticed the letter 'KI' traced on the sand of the table."
                if x == 300 and y == 470:
                    message = "You noticed the letter 'NG' traced on the sand of the table."

            # Status when hangman is complete
            if status >= 12:
                if x == 510 and y == 320:
                    message = "H  A  I  L  A  N  G  will always be with you......"

            # Status when talking to Candy after completing hangman
            if status >= 13:
                if x == 280 and y == 405:
                    message = "\"Hailang. It means ocean waves in Chinese. Do you see the pattern here?\""

            # Status when finding the code for the 'HELP' monitor
            if status == 14:
                if x == 420 and y == 155:  # CHEST
                    message = "The drawer opens and in it you see the numbers 11037."

            #  Status when finding a hat based on the radio's words
            if status == 22:
                if x == 70 and y == 310:
                    message = "Opening the drawer, you see a worn out black hat. Take it? (Y/N)"

        """
        ALL THE MESSAGES MEANT FOR ROOM 3
        """
        if room == 2:
            if x == 350 and y == 145:
                message = "\"You are so close to the end of the game.\""
            if x == 200 and y == 115:
                message = "The radio doesn't seem like it could play something anytime soon."
            if x == 83 and y == 110:
                message = "The simple portrait looks like it's smiling eerily back at you."
            if ((x == 220 or x == 260 or x == 305) and y == 265) or \
                    (x == 260 or x == 305 or x == 350) and y == 335:
                message = "For some reason, you can't sit on the chair. It's like someone is already on it."
            if x == 200 and y == 280:
                message = "So............ much.......... food........."
            if ((x == 49 or x == 254 or x == 315 or x == 530) and y == 120) or \
                    ((x == 49 or x == 530) and y == 465):
                message = "Tulips seem to be growing nicely in the vase. Who is watering them?"
            if x == 125 and y == 115:
                message = "A regular monitor. You feel anxious if you stare at it for too long."
            if x == 420 and y == 115:
                message = "A monitor with the word 'HELP' displayed. Looks very concerning."
            if x == 485 and y == 110:
                message = "You wonder if the owner would mind you taking a hat or two from the rack."
            if x == 380 and y == 102:
                message = "The image in the mirror reflects the tiredness in your eyes."

            # Status when being able to enter the code for the 'HELP' monitor.
            if status == 13:
                if x == 420 and y == 115:
                    message = "Enter the code."

            # Candy's hint for the 'HELP' monitor
            if status == 14:
                if x == 350 and y == 145:
                    message = "\"It might not even be in this room.\""
                if x == 420 and y == 115:
                    message = "Enter the code."

            # Candy's hint, monitor after entering the code, and hollow mirror
            if status == 15:
                if x == 350 and y == 145:
                    message = "\"Look beyond your reflection.\""
                if x == 420 and y == 115:
                    message = "\"...I...........cA....N..............S...e...3.......... yO....u.............\""
                if x == 380 and y == 102:
                    message = "The mirror appears to be hollow. Break it? (Y/N)"

            # Getting the cassette after breaking the mirror
            if status == 16:
                if x == 380 and y == 102:
                    message = "A cassette labeled 'Origins' was hidden beneath the shards. You took it."

            # Next status being to feed Candy
            if status == 17:
                if x == 380 and y == 102:
                    message = "A cassette labeled 'Origins' was hidden beneath the shards. You took it."
                if x == 350 and y == 145:
                    message = "\"I'm hungry. Feed me.\""

            # Status when finding food for Candy
            if status == 18:
                if x == 350 and y == 145:
                    message = "\"I'm hungry. Feed me.\""
                if x == 200 and y == 280:
                    message = "Food doesn't seem appropriate for Candy to eat. Take it anyway? (Y/N)"
                if x == 530 and y == 465:
                    message = "You see a bone buried beneath the flower pot. Dig it up anyway? (Y/N)"

            # Bad Ending #2: Getting the wrong bone
            if status == 18.1:
                if x == 350 and y == 145:
                    message = "\"This is...... unacceptable.\""

            # Status when Candy accepts the bone and gives you the cassette
            if status == 19:
                if x == 350 and y == 145:
                    message = "Candy seems appeased by the bone and gives you a cassette labeled 'Paths.'"

            # Status of radio giving the option to play either cassettes
            if status == "20":
                if x == 350 and y == 145:
                    message = "Candy seems appeased by the bone and gives you a cassette labeled 'Paths.'"
                if x == 200 and y == 115:
                    message = "The radio looks like it could only play one cassette. Play 'Origins' or 'Paths'?"

            # Bad Ending #3: Played the wrong cassette
            if status == 20.1:
                if x == 200 and y == 115:
                    message = "\"B....zz..........z...........t.......ttt.................go die.\""

            # Playing the correct cassette and hint for the next step
            if status >= 21:
                if x == 200 and y == 115:
                    message = "Among the noise you hear a whisper: gi...ve….BaA...ckkk... mYy....HaATaT...."

            # Status when finding a hat based on the radio's words
            if status == 22:
                if x == 485 and y == 110:
                    message = "You think about what the cassette said. Take a hat? (Y/N)"

            # Status when finding a hat based on the radio's words
            if status == 23:
                if x == 260 and y == 335:
                    message = "A sobbing noise can be heard from the seat. Give them the hat? (Y/N)"

            # Bad Ending #4: Failing to give the hat
            if status == "23.1":
                if x == 260 and y == 335:
                    message = "\"How.... da...re...you..... not GIVE ME BACK MY HAT!!!!!!!!\""

            # Success in giving the hat
            if status == 24:
                if x == 260 and y == 335:
                    message = "\" T.....h.....an......k................. you.............\""

        """
        ALL MESSAGES MEANT FOR THE FINAL ROOM
        """
        if room == 3:
            if x == 285 and y == 95:
                message = "\"Hello, Taomei. I am you. The other you.\""
            if x == 70 and y == 305:
                message = "\"H......uhuhuh.......uh.........uhuuuu......h..huhuhu................\""
            if x == 520 and y == 305:
                message = "\"Curiosity kills the cat.\""

        # Blits the text onto the screen
        screen.blit(self.font.render(message, True, constants.WHITE), (60, 515))
