from Visualisation import Visualize
from QLearning import q_learning
from maze import generateValidMaze
import argparse
import sys

parser = argparse.ArgumentParser(description="Simple QLearning algorithm for solving mazes")
parser.add_argument('-s', '--size', help='N parameter for NxN maze', type=int, default=8)
parser.add_argument('-mr', '--maze-ratio',
                    help='Ratio of maze obstacles to all fields (recommended <= 0.75 for smaller mazes and <= 0.5 '
                         'for bigger mazes)', type=float, default=0.5)
parser.add_argument('-sx', '--start-x', help='X param of starting point (0 <= x <= size -1)', type=int, default=0)
parser.add_argument('-sy', '--start-y', help='Y param of starting point (0 <= y <= size -1)', type=int, default=0)
parser.add_argument('-fx', '--finish-x', help='X param of final point (0 <= x <= size -1)', type=int, default=7)
parser.add_argument('-fy', '--finish-y', help='Y param of final point (0 <= y <= size -1)', type=int, default=7)
parser.add_argument('-i', '--iterations', help='Number of training iterations', type=int, default=1000)
parser.add_argument('-lr', '--learning-rate', help='Learning rate of QLearning algorithm', type=float, default=0.9)
parser.add_argument('-dr', '--discount-rate', help='Discount rate of QLearning algorithm', type=float, default=0.9)
parser.add_argument('-er', '--exploration-rate', help='Exploration to exploitation Rate', type=float, default=0.1)
parser.add_argument('-ed', '--exploration-decrease',
                    help='Value that will be substituted from explorationRate on every iteration',
                    type=float, default=0)
parser.add_argument('-me', '--min-exploration-rate', help='Cap for exploration Rate decrease', type=float, default=0)


def parse_exceptions(args):
    if args.size <= 3:
        raise ValueError('Size must be grater than 3')
    if args.maze_ratio < 0 or args.maze_ratio > 0.75:
        raise ValueError('Maze ratio must be between 0 and 0.75')
    if args.start_x >= args.size or args.start_x < 0:
        raise ValueError('x coordinate of starting point must be between 0 and (size - 1)')
    if args.start_y >= args.size or args.start_y < 0:
        raise ValueError('y coordinate of starting point must be between 0 and (size - 1)')
    if args.finish_x >= args.size or args.finish_x < 0:
        raise ValueError('x coordinate of finish point must be between 0 and (size - 1)')
    if args.finish_y >= args.size or args.finish_y < 0:
        raise ValueError('y coordinate of finish point must be between 0 and (size - 1)')
    if args.iterations <= 0:
        raise ValueError('Amount of iterations must be grater than 0')
    if args.learning_rate < 0 or args.learning_rate > 1:
        raise ValueError('Learning rate must be between 0 and 1')
    if args.discount_rate < 0 or args.discount_rate > 1:
        raise ValueError('Discount rate must be between 0 and 1')
    if args.exploration_rate < 0 or args.exploration_rate > 1:
        raise ValueError('Exploration rate must be between 0 and 1')
    if args.exploration_decrease < 0 or args.exploration_decrease > args.exploration_rate - args.min_exploration_rate:
        raise ValueError('Exploration decrease must be between 0 and (exploration_rate - min_exploration_rate)')
    if args.min_exploration_rate < 0 or args.min_exploration_rate > 1:
        raise ValueError('Minimum exploration rate must be between 0 and 1')


def main():
    sys.setrecursionlimit(1000000000)
    args = parser.parse_args()
    parse_exceptions(args)

    size = args.size
    maze_ratio = args.maze_ratio
    start_x = args.start_x
    start_y = args.start_y
    finish_x = args.finish_x
    finish_y = args.finish_y
    learning_rate = args.learning_rate
    discount_rate = args.discount_rate
    exploration_rate = args.exploration_rate
    min_exploration_rate = args.min_exploration_rate
    exploration_decrease = args.exploration_decrease
    iterations = args.iterations
    start = start_y * size + start_x
    finish = finish_y * size + finish_x

    print("Maze generator starts")
    maze = generateValidMaze(size, maze_ratio, start_x, start_y, finish_x, finish_y)

    print("Maze is generated, learning starts")
    path = q_learning(maze, size, start, finish, learning_rate, discount_rate, exploration_rate, min_exploration_rate,
                      exploration_decrease, iterations)

    print("Learning has finished")
    Visualize(maze, start_x, start_y, finish_x, finish_y, path)


if __name__ == '__main__':
    main()
