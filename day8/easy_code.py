from pprint import pprint

attenna_map = []

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip().split()
        attenna_map.append(list(line[0]))

# pprint(attenna_map)

# ............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............

# an antinode occurs at any point that is perfectly 
# in line with two antennas of the same frequency - but only when 
# the antinode is as far away as the distance between antennas. 
# This means that for any pair of antennas with the same frequency, 
# there are two antinodes, one on either side of them.
# overlapping antinodes on frequencies are counted

# 0 1 2 3 4 5 6 7 8 9 10 11
# . . . . . . # . . . . # 0 - #[(0,6), (0,11)]
# . . . # . . . . 0 . . . 1 - 0(1,8) #[(1,3)]
# . . . . # 0 . . . . # . 2 - 0(2,5) #[(2,4), (2,10)]
# . . # . . . . 0 . . . . 3 - 0(3,7) #[(3,2)]
# . . . . 0 . . . . # . . 4 - 0(4,4) #[(4,9)]
# . # . . . . A . . . . . 5 - A(5,5) #[(5,1)]
# . . . # . . . . . . . . 6 - #[(6,3)]
# # . . . . . . # . . . . 7 - #[(7,0), (7,7)]
# . . . . . . . . A . . . 8 - A(8,8)
# . . . . . . . . . A . . 9 - A(9,9)
# . . . . . . . . . . # . 10 - #[(10,10)]
# . . . . . . . . . . # . 11 - #[(11,10)]
# 14 antinodes - 13 #'s and 1 overlapping the topmost 'A'

# two A (8,8) & (9,9), distance = 1/1, two # (7,7) & (10,10), distance = 1/1

# goal: find number of distinct antinodes within the map
# plan: find all frequencies, find all antinodes, count antinodes

def map_of_frequencies(attenna_map):
    frequencies = {}
    for y in range(len(attenna_map)):
        for x in range(len(attenna_map[y])):
            if attenna_map[y][x] != '.':
                if attenna_map[y][x] in frequencies:
                    frequencies[attenna_map[y][x]].append((x, y))
                else:
                    frequencies[attenna_map[y][x]] = [(x, y)]
    return frequencies

def find_antinodes(frequencies):
    antinodes = set()
    for frequency in frequencies:
        for i in range(len(frequencies[frequency])):
            for j in range(i+1, len(frequencies[frequency])):
                x1, y1 = frequencies[frequency][i]
                x2, y2 = frequencies[frequency][j]
                dx = x2 - x1
                dy = y2 - y1
                antinodes.add((x1 - dx, y1 - dy))
                antinodes.add((x2 + dx, y2 + dy))
    return antinodes

def print_antinodes(anttena_map, antinodes):
    for (x, y) in antinodes:
        if x >= 0 and x < len(anttena_map[0]) and y >= 0 and y < len(anttena_map):
            if anttena_map[y][x] == '.':
                anttena_map[y][x] = '#'

def count_valid_antinodes(attenna_map, antinodes):
    count = 0
    for (x, y) in antinodes:
        if x >= 0 and x < len(attenna_map[0]) and y >= 0 and y < len(attenna_map):
            count += 1
    return count

frequencies = map_of_frequencies(attenna_map)
antinodes = find_antinodes(frequencies)
count = count_valid_antinodes(attenna_map, antinodes)
# print(f"frequencies = {frequencies}")
# print(f"antinodes = {antinodes}")
print(f"count = {count}")
# print_antinodes(attenna_map, antinodes)
# pprint(attenna_map)
# 249 Correct