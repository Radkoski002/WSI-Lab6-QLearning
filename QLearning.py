import random
import numpy as np


def isStateTerminal(position, rewards):
    if rewards[position] == -1:
        return False
    else:
        return True


def getNextState(explorationRate, currentMove):
    if explorationRate < random.random():
        return np.argmax(currentMove)
    else:
        return random.randint(0, 3)


def getNextMove(state, currentPosition, size):
    if state == 0 and currentPosition % size != 0:
        currentPosition -= 1
    if state == 1 and currentPosition // size != size - 1:
        currentPosition += size
    if state == 2 and currentPosition // size != 0:
        currentPosition -= size
    if state == 3 and currentPosition % size != size - 1:
        currentPosition += 1
    return currentPosition


def rewardTableInitialize(maze, size, finish):
    rewards = []
    for row in maze:
        for field in row:
            if field == 'x':
                rewards.append(-(size ** 2))
            else:
                rewards.append(-1)
    rewards[finish] = size ** 2
    return rewards


def currentLearnedPath(start, rewards, qTable, size):
    path = []
    currentPosition = start
    path.append(currentPosition)
    moves = 0
    while not isStateTerminal(currentPosition, rewards) and moves < size ** 2:
        state = getNextState(0, qTable[currentPosition])
        currentPosition = getNextMove(state, currentPosition, size)
        path.append(currentPosition)
        moves += 1
    return path


def qLearning(maze, size, start, finish,
              learningRate, discountRate, explorationDecrease, iterations):
    qTable = [[0 for _ in range(4)] for __ in range(size ** 2)]
    explorationRate = 1
    minExplorationRate = 0.1
    rewards = rewardTableInitialize(maze, size, finish)

    for iteration in range(iterations):
        if explorationRate > minExplorationRate:
            explorationRate -= explorationDecrease
        moves = 0
        currentPosition = start
        while not isStateTerminal(currentPosition, rewards) and moves < size ** 2:
            state = getNextState(explorationRate, qTable[currentPosition])
            nextMove = getNextMove(state, currentPosition, size)
            reward = rewards[nextMove]
            if currentPosition == nextMove:
                reward -= 10
            oldValue = (1 - learningRate) * qTable[currentPosition][state]
            nextValue = learningRate * (reward + discountRate * max(qTable[nextMove]))
            qTable[currentPosition][state] = oldValue + nextValue

            currentPosition = nextMove
            moves += 1

    path = currentLearnedPath(start, rewards, qTable, size)
    return path
