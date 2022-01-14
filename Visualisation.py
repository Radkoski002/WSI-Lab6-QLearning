import pygame
import sys
from maze import generateValidMaze
from randomCar import randomCarMove

white = (255, 255, 255)
gray = (100, 100, 100)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)


def generateBoard(maze, rSize, screen):
    for rowIndex, row in enumerate(maze):
        for fieldIndex, field in enumerate(row):
            square = [rSize * (rowIndex + 1) + rowIndex, rSize * (fieldIndex + 1) + fieldIndex,
                      rSize, rSize]
            if field == 'x':
                pygame.draw.rect(screen, red, square)
            else:
                pygame.draw.rect(screen, black, square)


def Visualize(size, ratio):
    maze = generateValidMaze(size, ratio)
    size = width, height = 800, 800
    rSize = int(width / (len(maze) + 2))

    pygame.init()

    screen = pygame.display.set_mode(size)
    screen.fill(gray)

    loseCounter = 0

    RECTEVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(RECTEVENT, 100)

    square = [rSize, rSize, rSize, rSize]
    row = col = 0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == RECTEVENT:
                pygame.draw.rect(screen, black, square)
                row, col = randomCarMove(row, col, len(maze))
                if row == col == len(maze) - 1:
                    sys.exit()
                if maze[row][col] == 'x':
                    generateBoard(maze, rSize, screen)
                    row = col = 0
                    loseCounter += 1
                generateBoard(maze, rSize, screen)
                square = [rSize * (row + 1) + row, rSize * (col + 1) + col,
                          rSize, rSize]
                pygame.draw.rect(screen, yellow, square)
                pygame.display.flip()
