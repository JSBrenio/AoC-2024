import re
word_matrix = []
xmas_count = 0

with open('example.txt', 'r') as file:
    for line in file:
        line = line.strip().split()
        word_matrix.append(line)

print(word_matrix)

whole_text = "".join(["".join(line) for line in word_matrix])
print(whole_text)

# Find XMAS
pattern = re.compile(r'(?=(X.*?M.*?A.*?S))')

matches = pattern.findall(whole_text)
print(matches)
print(len(matches))

# This word search allows words to be 
# horizontal, vertical, diagonal, written backwards, 
# or even overlapping other words.
# The goal is to find all instances of 'XMAS' in the word matrix.

# forward
# for i in range(len(word_matrix)):
#     for j in range(len(word_matrix[i])):
#         if ()
#         word_matrix[i][j] = word_matrix[i][j].lower()

# # backward
# for i in range(len(word_matrix)):
#     for j in range(len(word_matrix[i])):
#         word_matrix[i][j] = word_matrix[i][j].lower()

# print(xmas_count)

# 3733 wrong - too high