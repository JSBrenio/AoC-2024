stones = []

with open("input.txt", "r") as file:
    stones = list(map(int, file.read().split()))

# print(stones)

# Transformation according to first applicable rule:
# - If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
# - If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. 
#   The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. 
#   (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
# - If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
# No matter how the stones change, their order is preserved, and they stay on their perfectly straight line.

# Example:
# Initial arrangement:
# 125 17

# After 1 blink:
# 253000 1 7

# After 2 blinks:
# 253 0 2024 14168

# After 3 blinks:
# 512072 1 20 24 28676032

# After 4 blinks:
# 512 72 2024 2 0 2 4 2867 6032

# After 5 blinks:
# 1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32

# After 6 blinks:
# 2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2

# new goal: Number of stones after 75 'blinks'/iterations
# easy_code is too slow to run 75 iterations => dynamic programming needed, also focus on the number of stones instead of the stones themselves

def is_zero(n):
    return n == 0

def is_even(n):
    return len(str(n)) % 2 == 0

def transform_stone(n, memo):
    if n in memo:
        return memo[n]
    
    if is_zero(n):
        result = [1]
    elif is_even(n):
        str_n = str(n)
        left = str_n[:len(str_n)//2]
        right = str_n[len(str_n)//2:]
        result = [int(left), int(right)]
    else:
        result = [n * 2024]
    
    memo[n] = result
    return result

def transform_stones(stones, n):
    memo = {}
    stone_counts = {}
    
    # Initialize stone counts
    for stone in stones:
        if stone not in stone_counts:
            stone_counts[stone] = 1
    
    for iteration in range(n):
        new_stone_counts = {}
        for stone, count in stone_counts.items():
            transformed_stones = transform_stone(stone, memo)
            for transformed_stone in transformed_stones:
                if transformed_stone not in new_stone_counts:
                    new_stone_counts[transformed_stone] = 0
                new_stone_counts[transformed_stone] += count
        stone_counts = new_stone_counts
        print(f"Iteration {iteration + 1}: {sum(stone_counts.values())} stones")
    
    return stone_counts

stones_counts = transform_stones(stones, 75)
print(sum(stones_counts.values()))
# 225404711855335 Correct