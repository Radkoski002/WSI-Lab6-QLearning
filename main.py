from Visualisation import Visualize
from QLearning import qLearning
from maze import generateValidMaze


def main():
    size = 20
    mazeRatio = 0.7
    startX = 0
    startY = 0
    finishX = 19
    finishY = 19
    learningRate = 0.9
    discountRate = 0.9
    explorationDecrease = 0.01
    iterations = 2000
    start = startY * size + startX
    finish = finishY * size + finishX
    maze = generateValidMaze(size, mazeRatio, startX, startY, finishX, finishY)
    path = qLearning(maze, size, start, finish, learningRate, discountRate, explorationDecrease, iterations)
    Visualize(maze, startX, startY, path)


if __name__ == '__main__':
    main()
