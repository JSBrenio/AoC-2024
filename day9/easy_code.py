disk_map = ""

with open('input.txt', 'r') as file:
    disk_map = file.read().replace('\n', '').strip()

# print(disk_map)

# 2333133121414131402
# format: file - free space - file - free space
# file = ID number based on current file index, free space = '.'
# after format:
# 00...111...2...333.44.5555.6666.777.888899

# move file blocks one at a time from the end of the disk to 
# the leftmost free space block (until there are no gaps remaining between file blocks)
# moving process:
# 00...111...2...333.44.5555.6666.777.888899
# 009..111...2...333.44.5555.6666.777.88889.
# 0099.111...2...333.44.5555.6666.777.8888..
# 00998111...2...333.44.5555.6666.777.888...
# 009981118..2...333.44.5555.6666.777.88....
# 0099811188.2...333.44.5555.6666.777.8.....
# 009981118882...333.44.5555.6666.777.......
# 0099811188827..333.44.5555.6666.77........
# 00998111888277.333.44.5555.6666.7.........
# 009981118882777333.44.5555.6666...........
# 009981118882777333644.5555.666............
# 00998111888277733364465555.66.............
# 0099811188827773336446555566..............

# Checksum: add up the result of multiplying each of these blocks' position 
# with the file ID number it contains. Skip free blocks.
# Calculation:
# 0 * 0 = 0, 1 * 0 = 0, 2 * 9 = 18, 3 * 9 = 27, 4 * 8 = 32 ... = 1928.

# ACCOUNT FOR MULTIPLE DIGITS IN FILE ID

def formatted_disk_map(disk):
    new_disk = list()
    current_id = 0
    for i in range(0, len(disk)):
        if i % 2 == 0:
            for _ in range(0, int(disk[i])):
                new_disk.append(current_id)
            current_id += 1
        else:
            for _ in range(0, int(disk[i])):
                new_disk.append(None)

    return new_disk

def move_file_blocks(disk):
    beg_pointer = None
    end_pointer = None
    for i in range(0, len(disk)):
        if disk[i] is None:
            beg_pointer = i
            break
    for i in range(len(disk) - 1, 0, -1):
        if disk[i] is not None:
            end_pointer = i
            break
        
    while beg_pointer < end_pointer:
        if disk[end_pointer] is None:
            end_pointer -= 1
        elif disk[beg_pointer] is None:
            # swap
            disk[beg_pointer], disk[end_pointer] = disk[end_pointer], disk[beg_pointer]
            end_pointer -= 1
            beg_pointer += 1
            # print(''.join(str(x) if x is not None else '.' for x in disk))
        else:
            beg_pointer += 1
        
    return disk

def calculate_checksum(disk):
    checksum = 0
    id = 0
    for i in range(0, len(disk)):
        if disk[i] is not None:
            checksum += id * int(disk[i])
            id += 1
    return checksum


formatted_disk = formatted_disk_map(disk_map)
# print(formatted_disk)
formatted_disk = move_file_blocks(formatted_disk)
# print(''.join(str(x) if x is not None else '.' for x in formatted_disk))
checksum = calculate_checksum(formatted_disk)

print(checksum)
# 88957760693 - answer too low
# 111786959710 - answer too low
# 6259790630969 - correct answer