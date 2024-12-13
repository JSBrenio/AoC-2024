import re
import pprint
word_matrix = []
xmas_count = 0
XMAS = ['X', 'M', 'A', 'S']
SAMX = ['S', 'A', 'M', 'X']

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip().split()
        word_matrix.append(list(line[0]))

# print(word_matrix)
# pprint.pprint(word_matrix)

## Give up on regex
# # Find XMAS
# pattern = re.compile(r'(?=(X.*?M.*?A.*?S))')

# matches = pattern.findall(whole_text)
# print(matches)
# print(len(matches))

## Brute force
# This word search allows words to be 
# horizontal, vertical, diagonal, written backwards, 
# or even overlapping other words.
# The goal is to find all instances of 'XMAS' in the word matrix.
# 0123456789  
# MMMSXXMASM 0
# MSAMXMSMSA 1
# AMXSXMAAMM 2
# MSAMASMSMX 3
# XMASAMXAMM 4
# XXAMMXXAMA 5
# SMSMSASXSS 6
# SAXAMASAAA 7
# MAMMMXMMMM 8
# MXMXAXMASX 9

# 0123456789
# ....XXMAS. 0
# .SAMXMS... 1
# ...S..A... 2
# ..A.A.MS.X 3
# XMASAMX.MM 4
# X.....XA.A 5
# S.S.S.S.SS 6
# .A.A.A.A.A 7
# ..M.M.M.MM 8
# .X.X.XMASX 9
# 18 XMAS/SAMX in total
# 5 horizontal at row 0, 1, 4, 9
# 3 vertical at col 6, 9
# 10 SE and SW

def is_XMAS(word):
    return word == XMAS or word == SAMX

def horizontal(matrix):
    global xmas_count
    count = 0
    for row in matrix:
        # print(row)
        for i in range(len(row) - 3):
            word = row[i:i+4]
            if is_XMAS(word):
                xmas_count += 1
                count += 1
            # print(row, f"WINDOW:[{i}:{i+3}]", word, word[::-1], xmas_count)
    print("Horizontal:", count)

def vertical(matrix):
    global xmas_count
    count = 0
    for col in range(len(matrix[0])):
        string = []
        for row in range(len(matrix)):
            string.append(matrix[row][col])
        # print(string)
        for i in range(len(matrix)-3):
            word = string[i:i+4]
            # print(word, rev)
            if is_XMAS(word):
                xmas_count += 1
                count += 1
    print("Vertical:", count)

def south_east(matrix):
    global xmas_count
    count = 0
    for row in range(len(matrix)-3):
        for col in range(len(matrix[0])-3):
            word = [matrix[row][col], matrix[row+1][col+1], matrix[row+2][col+2], matrix[row+3][col+3]]
            if is_XMAS(word):
                xmas_count += 1
                count += 1
    print("SE", count)

def south_west(matrix):
    global xmas_count
    count = 0
    for i in range(len(matrix)-3):
        for j in range(3, len(matrix[0])):
            word = [matrix[i][j], matrix[i+1][j-1], matrix[i+2][j-2], matrix[i+3][j-3]]
            if is_XMAS(word):
                xmas_count += 1
                count += 1
    print("SW:", count)
                
horizontal(word_matrix)
vertical(word_matrix)
south_east(word_matrix)
south_west(word_matrix)
print(xmas_count)
# 3733 wrong - too high
# 2718 Correct