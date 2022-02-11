# import libraries
import pygame
import time
import random

snake_speed = 12

# window size
window_x = 720
window_y = 480

# define colors
sandybrown = pygame.Color(244, 164, 96, 255)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(85, 107, 47, 255)
blue = pygame.Color(0, 0, 255)
plum = pygame.Color(139, 102, 139, 255)

# create a game window using the width and height defined above.
# use pygame.time.Clock()in the main logic of the game to change the speed of the snake

# initialize pygame
pygame.init()

# initialize the game window
pygame.display.set_caption('Slytherin')
game_window = pygame.display.set_mode((window_x, window_y))

# create frames per second controller
fps = pygame.time.Clock()

# INITIALIZE SNAKE POSITION AND ITS SIZE
# after initializing position, initialize the fruit position randomly anywhere in the defined height and width
# by setting direction to RIGHT you ensure that, whenever a user runs the program/game, the snake
#   must move right to the screen

# define snake default position
snake_position = [100, 50]

# define the first 4 blocks of the snake body
snake_body = [ [100, 50],
               [90, 50],
               [80, 50],
               [70, 50]
            ]
# fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

# set default snake direction towards right
direction = 'RIGHT'
change_to = direction

# CREATE A FUNCTION TO DISPLAY THE SCORE OF THE PLAYER
# here I'm creating a font object (font color will go here).
# then use render to create a background surface that will change whenever the score updates.
# create a rectangular object for the text surface object (where text will be refreshed)
# then display the score using blit which takes 2 arguments  screen.blit(background(x,y))

# initial score
score = 0

# display the Score function
def show_score(choice, color, font, size):
    # create the font object score_font
    score_font = pygame.font.SysFont(font, size)

    # create the display surface object score_surface
    score_surface = score_font.render('Score :' + str(score), True, color)

    # create a rectangular object for the text surface object
    score_rect = score_surface.get_rect()

    # display text
    game_window.blit(score_surface, score_rect)

# CREATE A GAME OVER FUNCTION THAT WILL REPRESENT THE SCORE AFTER THE SNAKE IS HIT BY A WALL OR ITSELF
# in the first line, create a font object to display scores.
# then create text surfaces to render scores
# after that, set the position of the text in the middle of the playable area
# display the scores using blit and update the score by updating the surface using flip().
# use sleep(2) to wait for 2 seconds before closing the window using quit()

# game over function
def game_over():
    # create font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)

    # create a text surface on which text will be drawn
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)

    # create a rectangular object for the text surface object
    game_over_rect = game_over_surface.get_rect()

    # set position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)

    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # after 2 seconds quit the program
    time.sleep(2)

    # deactivate pygame library
    pygame.quit()

    # quit the program
    quit()

# CREATE THE MAIN FUNCTION THAT WILL DO THE FOLLOWING:
#  validate keys that will be responsible for the movement of the snake, then create a special condition that the
#   snake should not be allowed to move in the opposite direction instantaneously
#  then if the snake and fruit collide, increment the core by 10 and a new fruit will then be spanned.
#  after that, check that if the snake hit a wall or not. If it hits one, call the game over function.
#  if snake hits itself, the game over function will be called.
#  finally, in the end display the scores using the show_score function created earlier.

# Main Function
while True:
    # handle key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
    # if 2 keys are pressed simultaneously, prevent snake from moving into 2 directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # snake body growing mechanism if fruits and snakes collide then scores will be incremented by 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1,(window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]

    fruit_spawn = True
    game_window.fill(sandybrown)

    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(game_window, plum, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Game over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # displaying score continuously
    show_score(1, white, 'times new roman', 20)

    # refresh game screen
    pygame.display.update()

    # frames per second / refresh rate
    fps.tick(snake_speed)

