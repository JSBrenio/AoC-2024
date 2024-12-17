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
# 9 trailheads, in reading order, scores of 5, 6, 5, 3, 1, 3, 5, 3, and 5. 
# sum of the scores of all trailheads is 36.

# graphing problem, find all possible paths from 0 to 9, sum the scores of the trailheads

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
    for trailhead in trailheads:
        
        i, j = trailhead
        current_path = deque([(i, j)])
        visited = set([(i, j)])
        while current_path:
            i, j = current_path.pop()
            if maze[i][j] == '9':
                trailheads[trailhead] += 1
                continue
            neighbors = find_neighbors(maze, i, j)
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    current_path.append(neighbor)
                else:
                    continue
    # print(trailheads)

trailheads = find_trailheads(maze)
# print(trailheads)
find_all_paths(maze, trailheads)
print(sum(trailheads.values()))
# 698 Correct