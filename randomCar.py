import random


def randomCarMove(row, col, size):
    availableMoves = []
    if row != 0:
        availableMoves.append((row - 1, col))

    if col != 0:
        availableMoves.append((row, col - 1))

    if row != size - 1:
        availableMoves.append((row + 1, col))

    if col != size - 1:
        availableMoves.append((row, col + 1))

    move = random.choice(availableMoves)
    return move[0], move[1]
