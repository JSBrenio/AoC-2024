import re

# pattern is a regular expression that matches the string "mul(1,2)"
# \d matches any digit
# + matches one or more of the preceding token
# , matches the character ','
# \ is an escape sequence; matches the character '(' and ')'
pattern = re.compile(r'mul\(\d+,\d+\)')
digits = re.compile(r'\d+') # matches any digit

to_mult = []
lines = []
with open("input.txt", 'r') as file:
    for line in file:
        lines.append(line.strip())
        
print(lines)

for line in lines:
    matches = pattern.findall(line)
    # print(matches)
    for match in matches:
        ints = digits.findall(match)
        # print(ints)
        to_mult.append(list(map(int, ints)))
        
    # print(to_mult)

result = sum([product[0] * product[1] for product in to_mult])
print(result)

# 183_788_984 is the right answer