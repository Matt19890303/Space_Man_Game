import pygame  # Imports a game library that lets you use specific functions in your program.
import random  #

# Initialize the pygame modules to get everything started.
pygame.init()

# The screen that will be created needs a width and a height.
screen_width = 600
screen_height = 700
screen = pygame.display.set_mode((screen_width,
                                  screen_height))  # This creates the screen and gives it the width and height specified as a 2 item sequence.

# Background
# Used the below link to help with this
# https://www.youtube.com/channel/UCirPbvoHzD78Lnyll6YYUpg
background = pygame.image.load("Space_man_background.png")

# This creates the player and gives it the image found in this folder (similarly with the enemy image).
# Used below link to get free images for the sprites
# https://www.flaticon.com/
player = pygame.image.load("Space_man_spaceship.png")
enemy1 = pygame.image.load("Space_man_rock.png")
enemy2 = pygame.image.load("Space_man_rock.png")
enemy3 = pygame.image.load("Space_man_rock.png")
prize = pygame.image.load("Space_man_trophy.png")

# Get the width and height of the images in order to do boundary detection
# (i.e. make sure the image stays within screen boundaries or know when the image is off the screen).
image_height = player.get_height()
image_width = player.get_width()
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()
enemy2_height = enemy1.get_height()
enemy2_width = enemy1.get_width()
enemy3_height = enemy1.get_height()
enemy3_width = enemy1.get_width()
print_height = enemy1.get_height()
prize_width = enemy1.get_width()

# Store the positions of the player and enemy as variables so that you can change them later.
playerXPosition = random.randint(0, 300)
playerYPosition = 550

# Make the enemy start off screen and at a random Y and X positions
enemy1XPosition = random.randint(0, 300)
enemy1YPosition = 0
enemy2XPosition = 600
enemy2YPosition = random.randint(0, 500)
enemy3XPosition = random.randint(0, 600)
enemy3YPosition = 0
prizeXPosition = random.randint(0, 500)
prizeYPosition = 0

# This checks if the up or down key is pressed.
# Key values are all set to False
keyUp = False
keyDown = False
keyLeft = False
keyRight = False

# This is the game loop. In games you will need to run the game logic over and over again.
# represent real time game play.
while 1:  
    # Loop structure that game(player, enemies, background, ect.)
    screen.fill((0, 0, 0))  # RGB - Red, Green, Blue
    # Background Image
    # Used the below link to help with this
    # https://www.youtube.com/channel/UCirPbvoHzD78Lnyll6YYUpg
    screen.blit(background, (0, 0))
    # Updates the game as player abd enemies move around on screen
    # This draws the player and enemies images to the screen at the postion specfied
    screen.blit(player, (playerXPosition,
                         playerYPosition))  
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    # This updates the screen.
    pygame.display.flip()  
    # Changes the name of the window
    # Adds an image next to the name that was changed
    # Used the below link to help with this
    # https://www.youtube.com/channel/UCirPbvoHzD78Lnyll6YYUpg
    pygame.display.set_caption("Space_Man")
    icon = pygame.image.load("Space_man_project.png")
    pygame.display.set_icon(icon)

    # This loops through events in the game.
    # Has a quit method so the game does not get stuck in the loop
    for event in pygame.event.get():
        # This event checks if the user quits the program, then if so it exits the program.
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
            # This event checks if the user press a key down.
        if event.type == pygame.KEYDOWN:

            # Test if the key pressed is the one we want.
            # pygame.K_UP represents a keyboard key constant.
            if event.key == pygame.K_UP:  
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True

            # This event checks if the key is up(i.e. not pressed by the user).
            # Test if the key released is the one we want.

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False

    if keyUp == True:
        # This makes sure that the user does not move the player above the window.
        if playerYPosition > 0:  
            # This suntracts 3 from the y position on the screen
            playerYPosition -= 3

    if keyDown == True:
        # This makes sure that the user does not move the player above the window.
        if playerYPosition < screen_height - image_height:
            # This adds 3 to the y position on the screen
            playerYPosition += 3

    if keyLeft == True:
        # This makes sure that the user does not move the player above the window.
        if playerXPosition > 0:
            # This subtracts 3 to the x position on the screen
            playerXPosition -= 3

    if keyRight == True:
        # This makes sure that the user does not move the player above the window.
        if playerXPosition < screen_width - image_height: 
            # This adds 3 to the x position on the screen
            playerXPosition += 3
    # Check for collision of the enemy with the player.
    # Bounding box for the player:
    playerBox = pygame.Rect(player.get_rect())
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image.
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the enemy:
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the enemy image.
    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition

    # Test collision of the boxes:
    # Game over is the player touches the any of the three enemies
    # Exits game once game is over
    if playerBox.colliderect(enemy1Box):
        # Display losing status to the user:
        print("GAME OVER!")
        # Quit game and exit window:
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemy2Box):
        # Display losing status to the user:
        print("GAME OVER!")
        # Quit game and exit window:
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemy3Box):
        # Display losing status to the user:
        print("GAME OVER!")
        # Quit game and exit window:
        pygame.quit()
        exit(0)

    # Win if the player touches the ster
    # Exits game once game is won
    if playerBox.colliderect(prizeBox):
        print("YOU WIN!!!!!")
        # Quit game and exit window:
        pygame.quit()
        exit(0)

    # Movement of the enemies on screen
    # When enemies touch the sides nothing happens
    if enemy1YPosition > 700 + enemy3_height:
        pass
    elif enemy2XPosition < 0 - enemy2_width:
        pass
    elif enemy3YPosition > 700 + enemy3_height:
        pass

    # Enemy movement speed in X and Y positions.
    enemy1YPosition += 1
    enemy2XPosition -= 1
    enemy3YPosition += 2