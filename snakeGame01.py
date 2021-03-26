import pygame
import random
import os
import time
pygame.init()
pygame.mixer.init()

# Game variable
gameWindowWidth = 1000
gameWindowHeight = 500

Font = pygame.font.SysFont(None, 40)
Font1 = pygame.font.SysFont(None, 30)
Blue = (200,200,255)

# Game Functions
def plotSnake(surface, colour, snakeList, size):
    for x,y in snakeList:
        pygame.draw.rect(surface, colour, (x, y, size, size))
def text_screen1(text, colour, x,y):
    screen_text = Font.render(text, True, colour)
    gameWindow.blit(screen_text, (x,y))
def text_screen(text, colour, x,y):
    screen_text = Font1.render(text, True, colour)
    gameWindow.blit(screen_text, (x,y))
def highScore():
    exit_gmae = False
    while exit_gmae == False:
        with open("highScore.txt", "r") as f:
            highscore = f.read()
        gameWindow.fill(Blue)
        text_screen1("Snake Game", (0, 0, 0), 390, 5)
        text_screen("High Score: "+str(highscore), (0, 0, 0), 340, 180)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_gmae = True
        pygame.display.update()
def welcome():
    exit_gmae = False
    pygame.mixer.music.load("Root.mp3")
    pygame.mixer.music.play(50)
    while exit_gmae == False:
        gameWindow.fill(Blue)
        text_screen1("Snake Game", (0, 0, 0), 390, 5)
        text_screen("Start game(Press S)", (0, 0, 0), 340, 150)
        text_screen("High Score(Press H)", (0, 0, 0), 340, 180)
        text_screen("Made by Kushagra Chaturvedi.", (0,0,0), 700, 480)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_gmae = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    gameLoop()
                if event.key == pygame.K_h:
                    highScore()
        pygame.display.update()

# setting display window
gameWindow = pygame.display.set_mode((gameWindowWidth,gameWindowHeight))
pygame.display.set_caption("Snake Game")

#Main gameloop
def gameLoop():
    # Game variable
    exitGame = False
    Green = (0, 255, 0)
    Black = (0, 0, 0)
    White = (255, 255, 255)
    snake_x, snake_y = 255, 255
    velocity_x = 0
    velocity_y = 0
    Red = (255, 0, 0)
    food_x, food_y = random.randrange(50, 980), random.randrange(50, 480)
    score = 0
    snakeList = []
    snakeLength = 1
    gameOver = False
    if not(os.path.exists("highScore.txt")):
        with open("highScore.txt", "w") as f:
            f.write("0")
    with open("highScore.txt", "r") as f:
        highscore = f.read()
    pygame.mixer.music.load("background.mp3")
    pygame.mixer.music.play(50)

    while exitGame == False:
        if gameOver == True:
            with open("highScore.txt", "w") as f:
                f.write(str(highscore))
            gameWindow.fill(White)
            text_screen1("Game over. Press 'Space' to continue", Black, 280, 220)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitGame = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gameLoop()
        else:
            gameWindow.fill(Green)
            pygame.draw.rect(gameWindow, Red, (food_x, food_y, 10, 10))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitGame = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 1
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -1
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -1
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = 1
                        velocity_x = 0
            snakeHead = []
            snakeHead.append(snake_x)
            snakeHead.append(snake_y)
            snakeList.append(snakeHead)
            if snake_x < 0:
                snake_x = gameWindowWidth
            if snake_x > gameWindowWidth:
                snake_x = 0
            if snake_y < 0:
                snake_y = gameWindowHeight
            if snake_y > gameWindowHeight:
                snake_y = 0
            if len(snakeList) > snakeLength:
                del snakeList[0]
            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                pygame.mixer.music.load("beep.mp3")
                pygame.mixer.music.play()
                time.sleep(0.21)
                pygame.mixer.music.load("background.mp3")
                pygame.mixer.music.play(50)
                food_x, food_y = random.randrange(50, 980), random.randrange(50, 480)
                score += 10
                snakeLength += 10
                if score>int(highscore):
                    highscore = score
            if snakeHead in snakeList[0:((len(snakeList)) - 1)]:
                pygame.mixer.music.load("collision.mp3")
                pygame.mixer.music.play()
                time.sleep(1.5)
                pygame.mixer.music.load("background.mp3")
                pygame.mixer.music.play(50)
                gameOver = True
            text_screen("Score: " + str(score), Black, 5, 5)
            text_screen1("Snake Game", Black, 340, 5)
            snake_x += velocity_x
            snake_y += velocity_y
            plotSnake(gameWindow, Black, snakeList, 20)
        pygame.display.update()
welcome()