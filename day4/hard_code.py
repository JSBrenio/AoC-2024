import pprint
word_matrix = []
xmas_count = 0
MAS = ['M', 'A', 'S']
SAM = ['S', 'A', 'M']

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip().split()
        word_matrix.append(list(line[0]))

# print(word_matrix)
# pprint.pprint(word_matrix)

# Find two MAS in the shape of an X
# M.S
# .A.
# M.S

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
# .M.S...... 0
# ..A..MSMS. 1
# .M.S.MAA.. 2
# ..A.ASMSM. 3
# .M.S.M.... 4
# .......... 5
# S.S.S.S.S. 6
# .A.A.A.A.. 7
# M.M.M.M.M. 8
# ..........
# 9 X-MAS in total

# brute force, just find 'M' or 'S' NW/NE and SW/SE 'A'

def is_MAS(word):
    return word == MAS or word == SAM

for row in range(1, len(word_matrix) - 1):
    for col in range(1, len(word_matrix[0]) - 1):
        if word_matrix[row][col] == 'A':
            word_one = [word_matrix[row - 1][col - 1], word_matrix[row][col], word_matrix[row + 1][col + 1]]
            word_two = [word_matrix[row - 1][col + 1], word_matrix[row][col], word_matrix[row + 1][col - 1]]
            if is_MAS(word_one) and is_MAS(word_two):
                xmas_count += 1

                
print(xmas_count)

# 2046 Correct