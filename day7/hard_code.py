from pprint import pprint
import itertools

equations = []

with open('input.txt', 'r') as file:
    for line in file:
        equations.append(list(map(int, line.strip().replace(":", "").split())))

# pprint(equations)
        
# evaluated left to right, only use addition and multiplication and now concatenation
# 190: 10 19 = pass -> 10 * 19; 3 possibility
# 3267: 81 40 27 = pass -> 81 * 40 + 27 or 81 + 40 * 27; 9 possibilities
# 83: 17 5
# 156: 15 6 = pass -> 15 || 6; 3 possibility
# 7290: 6 8 6 15 = pass -> 6 * 8 || 6 * 15; 27 possibilities
# 161011: 16 10 13
# 192: 17 8 14 = pass -> 17 || 8 + 14; 9 possibilities
# 21037: 9 7 18 13
# 292: 11 6 16 20 = pass -> 11 + 6 * 16 + 20; 8 possibilities
# sum = 190 + 3267 + 292 = 3749

# pattern: summation of (n-1) choose r, for r = 0 to n-1; 3^(n-1) combinations
# goal: find sum of all valid equations's test values

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def concatenate(x, y):
    return int(str(x) + str(y))

operators = [add, multiply, concatenate]
# for 3 values, 9 possibilities, 3^(3-1) = 9
# combinations = [[add, add], [add, multiply], [add, concatenate],
#                 [multiply, add], [multiply, multiply], [multiply, concatenate],
#                 [concatenate, add], [concatenate, multiply], [concatenate, concatenate]]
# for 4 values, 27 possibilities, 3^(4-1) = 27
# combinations = [[add, add, add],
#                 [add, add, multiply],
#                 [add, add, concatenate],
#                 [add, multiply, add],
#                 [add, multiply, multiply], ... etc


valid_equations = []
for equation in equations:
    test_value = equation[0]
    # performs a cartesian product of operators with itself, repeat = len(equation[1:] - 1)
    combinations = list(itertools.product(operators, repeat=len(equation[1:]) - 1))
    # print(f"Testing equation: {equation[0]}: {equation[1:]}, combinations: {len(combinations)}")
    # print([[op.__name__ for op in comb] for comb in combinations])
    for comb in combinations:
        to_eval = equation[1]
        for i in range(1, len(equation) - 1):
            to_eval = comb[i - 1](to_eval, equation[i + 1])
        # print(to_eval)
        if test_value == to_eval:
            # print(f"Valid equation: {equation[0]}: {equation[1:]} with combination: {[op.__name__ for op in comb]}")
            valid_equations.append(equation)
            break
        
# pprint(valid_equations)

sum = 0
for equation in valid_equations:
    sum += equation[0]
    
print(sum)

# 145149066755184 Correct! - Took a while to run, but it works ¯\_(ツ)_/¯