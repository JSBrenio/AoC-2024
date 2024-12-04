safe_count = 0

def is_asc(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

def is_desc(arr):
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            return False
    return True

def is_one_two_three_diff(arr):
    for i in range(len(arr)-1):
        result = abs(arr[i] - arr[i+1])
        if not (result >= 1 and result <= 3):
            return False
    return True

def is_safe(arr):
    return (is_asc(arr) or is_desc(arr)) and is_one_two_three_diff(arr)
    

with open('input.txt', 'r') as file:
    for line in file:
        line = line.split()
        level = []
        for i in range(len(line)):
            level.append(int(line[i]))
        
        if is_safe(level):
            safe_count += 1
        else: # If the level is not safe, try removing one element at a time
            for i in range(len(level)):
                arr = level.copy()
                arr.pop(i)
                if is_safe(arr):
                    # print("Old", level, "New", arr, end="\n\n")
                    safe_count += 1
                    break
        
print(safe_count)