from pprint import pprint
from copy import deepcopy

guard_map = []
marked_map = []

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip().split()
        guard_map.append(list(line[0]))
        marked_map.append(list(line[0]))

# pprint(guard_map)
# guard rules:
# turn right 90 degrees.
# Otherwise, take a step forward.
# goal:
# Find number of infinite loops from an obstruction

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
# 6 Different loops can be made
# ....#.....   ....#.....   ....#.....   ....#.....   ....#.....   ....#.....
# ....+---+#   ....+---+#   ....+---+#   ....+---+#   ....+---+#   ....+---+#
# ....|...|.   ....|...|.   ....|...|.   ....|...|.   ....|...|.   ....|...|.
# ..#.|...|.   ..#.|...|.   ..#.|...|.   ..#.|...|.   ..#.|...|.   ..#.|...|.
# ....|..#|.   ..+-+-+#|.   ..+-+-+#|.   ..+-+-+#|.   ..+-+-+#|.   ..+-+-+#|.
# ....|...|.   ..|.|.|.|.   ..|.|.|.|.   ..|.|.|.|.   ..|.|.|.|.   ..|.|.|.|.
# .#.O^---+.   .#+-^-+-+.   .#+-^-+-+.   .#+-^-+-+.   .#+-^-+-+.   .#+-^-+-+.
# ........#.   ......O.#.   .+----+O#.   ..|...|.#.   ....|.|.#.   .+----++#.
# #.........   #.........   #+----+...   #O+---+...   #..O+-+...   #+----++..
# ......#...   ......#...   ......#...   ......#...   ......#...   ......#O..
# 0 = new obstruction
# | up/down
# - left/right
# + intersection
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
starting_guard = deepcopy(guard)
# print(guard)

def find_route(guard_map):
    global guard
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
            guard_map[i][j] = dir[(dir.index(guard_map[i][j]) + 1) % 4]
        # pprint(guard_map)
        # print(guard)

# we'll consider a loop if the guard has visited the same position 5 times
def is_loop(guard_map, obstacle):
    global guard
    global starting_guard
    visited_count = {}
    while True:
        i, j = guard
        x, y = dir_moves[guard_map[i][j]]
        obx, oby = obstacle
        guard_map[obx][oby] = '0'
        if guard in visited_count: # loop detection
            if visited_count[guard] == 5:
                # print("LOOP")
                return True
        if i + x < 0 or i + x >= len(guard_map) or j + y < 0 or j + y >= len(guard_map[i + x]): # leave the map
            guard_map[i][j] = '.'
            # print("LEAVING MAP")
            return False
        elif guard_map[i + x][j + y] == '.': # move forward
            guard_map[i + x][j + y] = guard_map[i][j]
            guard_map[i][j] = '.'
            guard = (i + x, j + y)
            visited_count[guard] = visited_count.get(guard, 0) + 1
        elif guard_map[i + x][j + y] == '#' or guard_map[i + x][j + y] == '0': # rotate 90 deg
            # print(dir[(dir.index(guard_map[i][j]) + 1) % 4])
            guard_map[i][j] = dir[(dir.index(guard_map[i][j]) + 1) % 4]
        # pprint(guard_map)
        # print(guard)
        
find_route(guard_map)
num_pos = 0
# wherever there is an X except the guard's pos, we'll insert a 0 to test for loops
for i in range(len(marked_map)):
    for j in range(len(marked_map[i])):
        if marked_map[i][j] == 'X' and (i, j) != starting_guard:
            new_map = deepcopy(guard_map)
            guard = deepcopy(starting_guard)
            new_map[starting_guard[0]][starting_guard[1]] = '^'
            if is_loop(new_map, (i, j)):
                num_pos += 1
            
# pprint(marked_map)
print(num_pos)
# 5435 Too high
# 2008 Correct