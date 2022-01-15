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


def dfs(visited, graph, node, target):
    if node == target:
        return True
    if node not in visited:
        visited.add(node)
        for neighbour in graph[node]:
            if dfs(visited, graph, neighbour, target):
                return True
            else:
                continue
    return False


def generateValidMaze(size, ratio):
    isMazeValid = False
    maze = []
    while not isMazeValid:
        visited = set()
        maze = generateLabyrinth(size, ratio)
        graph = generateGraph(maze)
        isMazeValid = dfs(visited, graph, 0, size ** 2 - 1)
    return maze
