import re

# pattern is a regular expression that matches the string "mul(1,2)"
# \d matches any digit
# + matches one or more of the preceding token
# , matches the character ','
# \ is an escape sequence; matches the character '(' and ')'
pattern = re.compile(r'mul\(\d+,\d+\)')
digits = re.compile(r'\d+') # matches any digit

# do => continue to mul, don't => don't mul
do = re.compile(r'do\(\)')
dont = re.compile(r'don\'t\(\)')

# goal: remove any muls between don't() and do()
# or only consider muls between do() and don't()

# Regex to capture mul(x,y) within or after do() up to don't(), if don't() exists.
# . matches any character except newline
# * matches zero or more of the preceding token
# ? matches zero or one of the preceding token
# (.*?) matches any character zero or more times, as few times as possible
# (?:don't\(\)|$) matches don't() or end of string
# ?: is a non-capturing group
# | is an OR operator
# $ matches the end of the string
# re.DOTALL makes . match any character, including newline
# .* means any character zero or more times 
# because . is any character and * is zero or more times
extract_dos = re.compile(r"(do\(\).*?(?:don't\(\)|$))", re.MULTILINE | re.DOTALL)

to_mult = []
lines = []
with open("input.txt", 'r') as file:
    for line in file:
        lines.append(line.strip())

# do() is enabled by default
whole_text = 'do()' + "".join(lines)

# Extract text between do() and don't()
extracted_lines = []

do_matches = extract_dos.findall(whole_text)
# print(matches)
for match in do_matches:
    extracted_lines.append(match)

# print(extracted_lines)

for line in extracted_lines:
    matches = pattern.findall(line)
    # print(matches)
    for match in matches:
        ints = digits.findall(match)
        # print(ints)
        to_mult.append(list(map(int, ints)))
        
    # print(to_mult)

result = sum([product[0] * product[1] for product in to_mult])
print(result)
print(f"{result:_}")

# Results:
# 74_210_088 wrong
# 183_788_984 wrong
# 120_208_669 wrong
# 61_282_986 wrong - close

# ANSWER: 62_098_619