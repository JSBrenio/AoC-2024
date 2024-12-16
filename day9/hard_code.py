disk_map = ""

with open('input.txt', 'r') as file:
    disk_map = file.read().replace('\n', '').strip()

# print(disk_map)

# 2333133121414131402
# format: file - free space - file - free space
# file = ID number based on current file index, free space = '.'
# after format:
# 00...111...2...333.44.5555.6666.777.888899

# New requirements:
# rather than move individual block, 
# compact the files on disk by moving whole files blocks instead.
# If there is no free span large enough to move a file block, skip it.
# moving process:
# 00...111...2...333.44.5555.6666.777.888899
# 0099.111...2...333.44.5555.6666.777.8888..
# 0099.1117772...333.44.5555.6666.....8888..
# 0099.111777244.333....5555.6666.....8888..
# 00992111777.44.333....5555.6666.....8888..

# Checksum: add up the result of multiplying each of these blocks' position 
# with the file ID number it contains. Skip free blocks.
# Calculation:
# 0 * 0 = 0, 1 * 0 = 0, 2 * 9 = 18, 3 * 9 = 27, 4 * 2 = 8 ... = 2858.

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

# this is ugly, but it works
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
        
    current_id = disk[end_pointer]
    while current_id > 0:
        free_span = 0
        file_span = 0
        # find the next file block
        while disk[end_pointer] is None or disk[end_pointer] != current_id:
            end_pointer -= 1
        file_span = end_pointer
        while disk[file_span] is not None and disk[file_span] == current_id:
            file_span -= 1
        file_span = abs(file_span - end_pointer)
        while beg_pointer < end_pointer:
            # print(f"Finding free space for file span {file_span} of ID: {current_id}, beg_pointer: {beg_pointer}, end_pointer: {end_pointer}")
            # find the next free space
            while disk[beg_pointer] is not None:
                beg_pointer += 1
            free_span = beg_pointer
            while disk[free_span] is None and free_span < len(disk) - 1:
                free_span += 1
            free_span = abs(beg_pointer - free_span)
            if free_span >= file_span:
                break
            else:
                beg_pointer += 1
                free_span = 0
        # print(f"Free Span: {free_span}, File Span: {file_span}, Current ID: {current_id}, Begin Pointer: {beg_pointer}, End Pointer: {end_pointer}")
        # move the file block
        if free_span >= file_span and beg_pointer < end_pointer:
            # print(f"Moving file block of size {file_span} to free space of size {free_span} of ID {current_id}")
            free_span = file_span
            #swap
            disk[beg_pointer:beg_pointer + file_span], disk[end_pointer - file_span + 1:end_pointer + 1] = disk[end_pointer - file_span + 1:end_pointer + 1], disk[beg_pointer:beg_pointer + file_span]
            
        # print(''.join(str(x) if x is not None else '.' for x in disk))
        # print(disk)
        current_id -= 1
        beg_pointer = 0
        
    return disk

def calculate_checksum(disk):
    checksum = 0
    for i in range(0, len(disk)):
        if disk[i] is not None:
            checksum += i * int(disk[i])
    return checksum


formatted_disk = formatted_disk_map(disk_map)
# print(formatted_disk)
formatted_disk = move_file_blocks(formatted_disk)
# print(''.join(str(x) if x is not None else '.' for x in formatted_disk))
checksum = calculate_checksum(formatted_disk)

print(checksum)
# 6289564433984 Correct but slow ¯\_(ツ)_/¯