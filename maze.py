import random

random.seed(100)


def generateLabyrinth(size, ratio):
    maze = [[' ' for _ in range(size)] for __ in range(size)]
    for i in range(int((size ** 2) * ratio)):
        maze[random.randint(0, size - 1)][random.randint(0, size - 1)] = 'x'
    maze[0][0] = ' '
    maze[size - 1][size - 1] = ' '
    return maze


def generateGraph(maze):
    mazeGraph = {}
    for rowIndex, row in enumerate(maze):
        for fieldIndex, field in enumerate(row):
            if field != 'x':
                moves = []
                if rowIndex != 0 and maze[rowIndex - 1][fieldIndex] != 'x':
                    moves.append(len(maze) * (rowIndex - 1) + fieldIndex)

                if rowIndex != len(maze) - 1 and maze[rowIndex + 1][fieldIndex] != 'x':
                    moves.append(len(maze) * (rowIndex + 1) + fieldIndex)

                if fieldIndex != 0 and maze[rowIndex][fieldIndex - 1] != 'x':
                    moves.append(len(maze) * rowIndex + fieldIndex - 1)

                if fieldIndex != len(maze) - 1 and maze[rowIndex][fieldIndex + 1] != 'x':
                    moves.append(len(maze) * rowIndex + fieldIndex + 1)

                mazeGraph[rowIndex * len(maze) + fieldIndex] = moves
    return mazeGraph


def bfs(visited, graph, node, target):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        if s == target:
            return True

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    return False


queue = []
visited = []


def generateValidMaze(size, ratio):
    isMazeValid = False
    maze = []
    while not isMazeValid:
        queue.clear()
        visited.clear()
        maze = generateLabyrinth(size, ratio)
        graph = generateGraph(maze)
        isMazeValid = bfs(visited, graph, 0, size ** 2 - 1)
    return maze
