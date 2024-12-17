from collections import deque
from pprint import pprint

maze = []

with open('input.txt', 'r') as file:
    for line in file:
        maze.append(list(line.strip()))
        
# pprint(maze)

# 89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732
# trailheads start at 0, must incrementally reach 9 to be a trail

# New Condition:
# Ratings.
# A trailhead's rating is the number of distinct hiking trails which begin at that trailhead.
# 9 trailheads, in reading order, ratings of 20, 24, 10, 4, 1, 4, 5, 8, and 5.
# sum of the ratings of all trailheads is 81.

# graphing problem, find all distinct paths from 0 to 9, sum the ratings of the trailheads

def find_trailheads(maze):
    trailheads = {}
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == '0':
                trailheads[(i, j)] = 0
    return trailheads

def within_bounds(maze, i, j):
    return 0 <= i < len(maze) and 0 <= j < len(maze[i])

def find_neighbors(maze, i, j):
    neighbors = []
    curr_height = maze[i][j]
    # orthogonally adjacent
    #           up,     right,  down,   left
    moves =  [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for move in moves:
        x, y = move
        dx, dy = i + x, j + y
        if within_bounds(maze, dx, dy) and maze[dx][dy] == str(int(curr_height) + 1):
            neighbors.append((dx, dy))
    return neighbors

def find_all_paths(maze, trailheads):
    # DFS inner function
    def dfs(i, j, visited, path):
        if maze[i][j] == '9':
            distinct_paths.add(tuple(path))
            return
        visited.add((i, j))
        neighbors = find_neighbors(maze, i, j)
        for neighbor in neighbors:
            if neighbor not in visited:
                path.append(neighbor)
                dfs(neighbor[0], neighbor[1], visited, path)
                path.pop()  # Backtrack
        visited.remove((i, j))

    for trailhead in trailheads:
        distinct_paths = set()
        visited = set()
        i, j = trailhead
        path = [(i, j)]
        dfs(i, j, visited, path)
        trailheads[trailhead] = len(distinct_paths)
    # print(trailheads)

trailheads = find_trailheads(maze)
# print(trailheads)
find_all_paths(maze, trailheads)
print(sum(trailheads.values()))
# 1436 Correct