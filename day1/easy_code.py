left = []
right = []
with open('input.txt', 'r') as file:
    for line in file:
        line = line.split()
        left.append(int(line[0]))
        right.append(int(line[1]))
        
left = sorted(left)
right = sorted(right)

diff_list = []

for i in range(len(left)):
    diff_list.append((abs(left[i] - right[i])))

sum_list = sum(diff_list)

print(sum_list)