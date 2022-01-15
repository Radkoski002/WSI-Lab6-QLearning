import pygame
import sys
from randomCar import randomCarMove

white = (255, 255, 255)
gray = (100, 100, 100)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)


def generateBoard(maze, rSize, screen):
    for rowIndex, row in enumerate(maze):
        for fieldIndex, field in enumerate(row):
            square = [rSize * (fieldIndex + 1) + fieldIndex, rSize * (rowIndex + 1) + rowIndex,
                      rSize, rSize]
            if field == 'x':
                pygame.draw.rect(screen, red, square)
            else:
                pygame.draw.rect(screen, black, square)


def Visualize(maze, startX, startY, path=None):
    size = width, height = 800, 800
    rSize = int(width / (len(maze) + 2))

    pygame.init()

    screen = pygame.display.set_mode(size)
    screen.fill(gray)

    loseCounter = 0

    SLEEPEVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(SLEEPEVENT, 1000)

    square = [rSize, rSize, rSize, rSize]
    row = startX
    col = startY
    visualBool = True
    generateBoard(maze, rSize, screen)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == SLEEPEVENT:
                if path and visualBool:
                    for point in path:
                        pointX = point % len(maze)
                        pointY = point // len(maze)
                        square = [rSize * (pointX + 1) + pointX, rSize * (pointY + 1) + pointY,
                                  rSize, rSize]
                        pygame.draw.rect(screen, yellow, square)
                        visualBool = False
                else:
                    generateBoard(maze, rSize, screen)
                    visualBool = True
        pygame.display.flip()
