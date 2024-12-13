from pprint import pprint

guard_map = []
marked_map = []

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip().split()
        guard_map.append(list(line[0]))
        marked_map.append(list(line[0]))

pprint(guard_map)
# guard rules:
# turn right 90 degrees.
# Otherwise, take a step forward.
# goal:
# Find number of distinct locations visited by the guard.

# 0123456789
# ....#..... 0
# .........# 1
# .......... 2
# ..#....... 3
# .......#.. 4
# .......... 5
# .#..^..... 6
# ........#. 7
# #......... 8
# ......#... 9
# AFTER LEAVING THE MAP
# ....#.....
# ....XXXXX#
# ....X...X.
# ..#.X...X.
# ..XXXXX#X.
# ..X.X.X.X.
# .#XXXXXXX.
# .XXXXXXX#.
# #XXXXXXX..
# ......#X..
# 41 locations visited X

# directions
dir = ['^', '>', 'v', '<'] # rotate 90 deg = (current index + 1) % 4
dir_moves = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

# find the guard
guard = None
for i in range(len(guard_map)):
    for j in range(len(guard_map[i])):
        if guard_map[i][j] in dir:
            guard = (i, j)
            break

print(guard)

while True:
    i, j = guard
    x, y = dir_moves[guard_map[i][j]]
    
    if i + x < 0 or i + x >= len(guard_map) or j + y < 0 or j + y >= len(guard_map[i + x]): # leave the map
        guard_map[i][j] = '.'
        marked_map[i][j] = 'X'
        break
    elif guard_map[i + x][j + y] == '.': # move forward
        marked_map[i][j] = 'X'
        guard_map[i + x][j + y] = guard_map[i][j]
        guard_map[i][j] = '.'
        guard = (i + x, j + y)
    elif guard_map[i + x][j + y] == '#': # rotate 90 deg
        # print(dir[(dir.index(guard_map[i][j]) + 1) % 4])
        guard_map[i][j] = dir[(dir.index(guard_map[i][j]) + 1) % 4]
    # pprint(guard_map)
    # print(guard)
    
num_pos = 0
for i in range(len(marked_map)):
    for j in range(len(marked_map[i])):
        if marked_map[i][j] == 'X':
            num_pos += 1
            
pprint(marked_map)
print(num_pos)
# 5516 Correct