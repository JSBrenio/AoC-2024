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

# goal: Number of stones after 25 'blinks'/iterations

def is_zero(n):
    return n == 0

def is_even(n):
    return len(str(n)) % 2 == 0

def transform_stone(n):
    # print(n)
    if is_zero(n):
        return [1]
    elif is_even(n):
        str_n = str(n)
        left = str_n[:len(str_n)//2]
        right = str_n[len(str_n)//2:]
        return [int(left), int(right)]
    else:
        return [n * 2024]

def transform_stones(stones, n):
    for _ in range(n):
        new_stones = []
        # print(stones)
        for stone in stones:
            # Use extend to add the values from the returned list
            new_stones.extend(transform_stone(stone))
        # print(new_stones)
        stones = new_stones
    return stones

stones = transform_stones(stones, 25)
print(len(stones))
# 190865
