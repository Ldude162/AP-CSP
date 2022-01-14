'''
Made by Linus Reynolds
Sem 1 Create task
'''

#--- Import modules ---
import math
import random as rand
import pygame as game

#--- Start display ---
game.init()
surface = game.display.set_mode((400,300))

#--- colors ---
colors = []
colors.append((170,170,170))
colors.append((100,100,100))
colors.append((0,255,0))
colors.append((255,0,0))
colors.append((0,0,255))
colors.append((0,100,0))

#--- Texts ---
startFont = game.font.SysFont('Corbel', 30)
quitFont = game.font.SysFont('Corbel', 15)
quitText = quitFont.render('quit', True, colors[5])
instructions = quitFont.render('Press space to flip gravity, dont get hit by red!', True, colors[2])
mainMenu = quitFont.render('Main Menu', True, colors[5])
startText = startFont.render('Click to start', True, colors[2])
gameOver = startFont.render('Game Over!', True, colors[3])

#--- classes ---
'''
Creates a ground object, which is on the bottom of the screen
'''
class Ground(game.sprite.Sprite):
    # initialize
    def __init__(self):
        super().__init__()
        self.image = game.Surface((400,80))
        self.image.fill(colors[5])
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 250

    # draw on screen
    def draw(self):
        surface.blit(self.image, self.rect)

'''
Creates a ceiling object, which is on the top of the screen
'''
class Ceiling(game.sprite.Sprite):
    # initialize
    def __init__(self):
        super().__init__()
        self.image = game.Surface((400,50))
        self.image.fill(colors[5])
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
    
    # draw on screen
    def draw(self):
        surface.blit(self.image, self.rect)

'''
Creates the player, which can switch from the top and bottom.
'''
class Player(game.sprite.Sprite):
    # initialize
    def __init__(self):
        super().__init__()
        self.image = game.Surface((50,50))
        self.image.fill(colors[2])

        self.rect = self.image.get_rect()
        self.image = game.image.load("player.png")
        self.rect.x = 0
        self.rect.y = 150
        self.onground = True

  # Draws the player on the screen and updates it
    def draw(self):
        if self.onground == True:
            self.rect.bottom = ground.rect.top
        else:
            self.rect.top = ceiling.rect.bottom
        surface.blit(self.image, self.rect)

  # Function for switching gravity
    def gravitySwitch(self):
        if self.onground == False:
            self.onground = True
        elif self.onground == True:
            self.onground = False


'''
Creates the enemy, which is randomly on either the top or bottom.
'''
class Redbox(game.sprite.Sprite):
    # initialize
    def __init__(self):
        super().__init__()
        self.image = game.Surface((50,50))
        self.image.fill(colors[3])
        self.rect = self.image.get_rect()
        self.image = game.image.load("enemy.png")
        self.rect.x = 400
        self.rect.y = 0
        self.lap = 2
        self.location = 1

    # draws on screen, updates speed, updates lap, chooses top or bottom
    def draw(self):

        # moves to go on top or bottom
        if self.location == 1:
            self.rect.bottom = ground.rect.top
        else:
            self.rect.top = ceiling.rect.bottom

        # draws on screen
        surface.blit(self.image, self.rect)

        #sets speed
        self.rect.x -= math.log(self.lap,1.2)

        #when it gets to the end, choose to go on top or bottom
        if self.rect.x <= 0:
            self.rect.x = 400
            self.location = rand.randrange(0,2)
            self.lap += 1

#--- sprites and objects ---
# create objects
ground = Ground()
player = Player()
redBox = Redbox()
ceiling = Ceiling()
ticktock = game.time.Clock()


#--- Game Functions ---

# Most of the game happens here, gets triggered when start button is pressed.
def start():
    # Brings in variables related to pressing the quit button.
    global keepGoing
    global quit

    # Loops the game until the game is exited.
    while keepGoing:

        #sets fps
        ticktock.tick(30)

        # Checks if space or quit button is pressed
        for event in game.event.get():

            #checks if quit button is pressed
            if event.type == game.MOUSEBUTTONDOWN:

                # if it is, quit game.
                if 0 <= mouse[0] <= 30 and 0 <= mouse[1] <= 20:
                    quit = True
                    keepGoing = False

            # checks if space is pressed.
            elif event.type == game.KEYDOWN:

                # if it is, switch gravity.
                if event.key == game.K_SPACE:
                    player.gravitySwitch()


        # gets mouse pos
        mouse = game.mouse.get_pos()

        # sets background color
        surface.fill(colors[4])

        # Checks if they player collided with the enemy.
        collide = player.rect.colliderect(redBox.rect)

        # If they did, show game over screen.
        if collide:
            endGame()

        # Draw ceiling.
        ceiling.draw()

        # draw quit button, and if it is being hovered over make it lighter.
        if 0 <= mouse[0] <= 30 and 0 <= mouse[1] <= 20:
            game.draw.rect(surface,colors[0],[0,0,30,20])
        else:
            game.draw.rect(surface,colors[1],[0,0,30,20])

        # draw various things on the screen
        surface.blit(startFont.render("Score: " + str(redBox.lap - 2), True, colors[3]),(175,10))
        surface.blit(quitText,(0,0))
        surface.blit(player.image, player.rect)
        surface.blit(redBox.image, redBox.rect)
        player.draw()
        redBox.draw()
        ground.draw()

        # update the screen to show the frame.
        game.display.update()


# Game over screen, triggers when the player touches an enemy.
def endGame():
    
    # brings in the variables related to pressing the quit button.
    global keepGoing
    global quit

    # high score system, opens high score file to see the current high score.
    f = open('leaderboard.txt', 'r')
    highscore = f.read()
    f.close()

    # Checks if the player has the new high score.
    if redBox.lap - 2 > int(highscore):

        # if they do, change the high score.
        highscore = redBox.lap - 2
        f = open('leaderboard.txt', 'w')
        f.write(str(redBox.lap - 2))
        f.close()

    # main loop for the end screen
    while keepGoing:

        # gets mouse pos
        mouse = game.mouse.get_pos()

        # checks if any of the buttons are pressed
        for event in game.event.get():
            
            # is mouse pressed?
            if event.type == game.MOUSEBUTTONDOWN:

                # is mouse over the quit button?
                if 0 <= mouse[0] <= 30 and 0 <= mouse[1] <= 20:

                    # if so, quit game.
                    quit = True
                    keepGoing = False
                
                # is mouse over the main menu button?
                elif 175 <= mouse[0] <= 255 and 200 <= mouse[1] <= 220:

                    # if so, go to the main menu.
                    keepGoing = False


        # If the mouse is hovering over any of the buttons, make them lighter.
        if 0 <= mouse[0] <= 30 and 0 <= mouse[1] <= 20:
            game.draw.rect(surface,colors[0],[0,0,30,20])
            game.draw.rect(surface,colors[1],[175,200,80,20])
        elif 175 <= mouse[0] <= 255 and 200 <= mouse[1] <= 220:
            game.draw.rect(surface,colors[1],[0,0,30,20])
            game.draw.rect(surface,colors[0],[175,200,80,20])
        else:
            game.draw.rect(surface,colors[1],[0,0,30,20])
            game.draw.rect(surface,colors[1],[175,200,80,20])


        # draw various stuff on the screen.
        surface.blit(gameOver, (150,150))
        surface.blit(mainMenu, (175,205))
        surface.blit(startFont.render('High Score: ' + str(highscore), True, colors[3]), (150, 120))
        surface.blit(startFont.render("Score: " + str(redBox.lap - 2), True, colors[3]),(175,175))
        surface.blit(quitText,(0,0))

        # update the screen, so it shows the new frame.
        game.display.update()

#--- start loop ---

# sets variables related to the quit button. quitting is done this way to reduce errors.
quit = False
keepGoing = True

# has the quit button been pressed?
while quit != True:

    # game starts here
    while keepGoing:

        # set fps
        ticktock.tick(60)

        # get mouse pos
        mouse = game.mouse.get_pos()

        # checks if buttons are pressed
        for event in game.event.get():

            # is mouse pressed?
            if event.type == game.MOUSEBUTTONDOWN:

                #is mouse hovering over start button?
                if 115 <= mouse[0] <= 255 and 130 <= mouse[1] <= 170:

                    # if so, start game.
                    start()

                # is mouse hovering over quit button?
                elif 0 <= mouse[0] <= 30 and 0 <= mouse[1] <= 20:

                    # if so, quit game.
                    quit = True
                    keepGoing = False

        # set background.
        surface.fill((0,0,255))

        # makes buttons lighter if mouse is over them.
        if 115 <= mouse[0] <= 255 and 130 <= mouse[1] <= 170:
            game.draw.rect(surface,colors[0],[115,130,155,40])
            game.draw.rect(surface,colors[1],[0,0,30,20])
        elif 0 <= mouse[0] <= 30 and 0 <= mouse[1] <= 20:
            game.draw.rect(surface,colors[0],[0,0,30,20])
            game.draw.rect(surface,colors[1],[115,130,155,40])
        else:
            game.draw.rect(surface,colors[1],[115,130,155,40])
            game.draw.rect(surface,colors[1],[0,0,30,20])


        # write various texts on the screen
        surface.blit(startText, (120,135))
        surface.blit(quitText, (0,0))
        surface.blit(instructions, (100,200))

        # update the screen to show the new frame.
        game.display.update()

    # if main menu button is pressed on game over screen, this is activated to reset to the main menu.
    keepGoing = True