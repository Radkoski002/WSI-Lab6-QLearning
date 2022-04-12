import pygame
import sys

white = (255, 255, 255)
gray = (100, 100, 100)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)


def generate_board(maze, r_size, screen, start_square, finish_square):
    for rowIndex, row in enumerate(maze):
        for fieldIndex, field in enumerate(row):
            square = [r_size * fieldIndex + fieldIndex, r_size * rowIndex + rowIndex, r_size, r_size]
            if field == 'x':
                pygame.draw.rect(screen, red, square)
            else:
                pygame.draw.rect(screen, black, square)
    pygame.draw.rect(screen, green, start_square)
    pygame.draw.rect(screen, green, finish_square)


def Visualize(maze, startX, startY, finishX, finishY, path=None):
    width, height = 1000, 1000
    rSize = int(width / (len(maze) + 1))
    size = (rSize + 1) * len(maze), (rSize + 1) * len(maze)

    pygame.init()

    screen = pygame.display.set_mode(size)
    screen.fill(gray)

    SLEEPEVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(SLEEPEVENT, 1000)

    visualBool = True
    startSquare = [rSize * startX + startX, rSize * startY + startY, rSize, rSize]
    finishSquare = [rSize * finishX + finishX, rSize * finishY + finishY, rSize, rSize]
    generate_board(maze, rSize, screen, startSquare, finishSquare)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == SLEEPEVENT:
                if path and visualBool:
                    for point in path:
                        pointX = point % len(maze)
                        pointY = point // len(maze)
                        square = [rSize * pointX + pointX, rSize * pointY + pointY, rSize, rSize]
                        pygame.draw.rect(screen, yellow, square)
                        visualBool = False
                else:
                    generate_board(maze, rSize, screen, startSquare, finishSquare)
                    visualBool = True
        pygame.display.flip()
