import random
from time import sleep

import pygame
import sys
from maze import generateValidMaze


def main():
    white = (255, 255, 255)
    gray = (100, 100, 100)
    black = (0, 0, 0)
    red = (255, 0, 0)
    yellow = (255, 255, 0)
    maze = generateValidMaze(8, 0.4)
    size = width, height = 800, 800
    rSize = int(width / (len(maze) + 2))

    for row in maze:
        print(row)

    pygame.init()

    screen = pygame.display.set_mode(size)
    screen.fill(gray)
    for rowIndex, row in enumerate(maze):
        for fieldIndex, field in enumerate(row):
            square = [rSize * (rowIndex + 1) + rowIndex, rSize * (fieldIndex + 1) + fieldIndex,
                      rSize, rSize]
            if field == 'x':
                pygame.draw.rect(screen, red, square)
            else:
                pygame.draw.rect(screen, black, square)

        RECTEVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(RECTEVENT, 1000)

    square = [rSize, rSize, rSize, rSize]
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == RECTEVENT:
                pygame.draw.rect(screen, black, square)
                row = random.randint(0, len(maze) - 1)
                col = random.randint(0, len(maze) - 1)
                square = [rSize * (row + 1) + row, rSize * (col + 1) + col,
                          rSize, rSize]
                pygame.draw.rect(screen, yellow, square)

        pygame.display.flip()


if __name__ == '__main__':
    main()
