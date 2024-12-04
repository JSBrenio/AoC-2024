left = []
right = []
with open('input.txt', 'r') as file:
    for line in file:
        line = line.split()
        left.append(int(line[0]))
        right.append(int(line[1]))

diff_list = [0] * len(left)

for i in range(len(left)):
    for j in range(len(right)):
        if left[i] == right[j]:
            diff_list[i] += right[j]
    
sum_list = sum(diff_list)

print(sum_list)