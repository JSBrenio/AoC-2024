from pprint import pprint
rules = []
updates = []
with open('input.txt', 'r') as file:
    for line in file:
        if '|' in line:
            rules.append([int(x) for x in line.strip().split('|')])
        elif ',' in line:
            updates.append([int(x) for x in line.strip().split(',')])
# pprint(rules)
# pprint(updates)

# The notation X|Y means that if both page number X and page number Y 
# are to be produced as part of an update, 
# page number X must be printed at some point before page number Y.
# 47|53 47 must be printed before 53
# 97|13 97 must be printed before 13
# 97|61 ... etc
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 75,47,61,53,29 - pass
# 97,61,53,29,13 - pass
# 75,29,13       - pass
# 75,97,47,61,53 - violates 97|75
# 61,13,29       - violates 29|13
# 97,13,75,29,47 - violates 75|13

# Elves also need to know the middle page number of each violated update being printed
# 75,97,47,61,53 becomes 97,75,47,61,53.
# 61,13,29 becomes 61,29,13.
# 97,13,75,29,47 becomes 97,75,47,29,13
# 47 + 29 + 47 = 123.

# create rules dict (key = page number, value = list of pages that must be printed before)
rules_dict = {}
for rule in rules:
    if rule[0] not in rules_dict:
        rules_dict[rule[0]] = []
    rules_dict[rule[0]].append(rule[1])
    
# pprint(rules_dict)

# check if updates are valid, take the invalid ones instead
invalid_updates = []
for update in updates:
    violation = False
    # print(f"Current Update: {update}")
    for i in range(len(update)):
        if update[i] in rules_dict:
            # print(f"Checking {update[i]} with rules {rules_dict[update[i]]}")
            for rule in rules_dict[update[i]]:
                if rule in update[:i]:
                    # print(f"Violation: {update} violates {update[i]}|{rule}")
                    violation = True
                    break
    if violation:
        invalid_updates.append(update)

# print("Invalid updates:")
# pprint(invalid_updates)

# correct the invalid updates
for update in invalid_updates:
    # print(f"Correcting {update}")
    i = 0
    while i < len(update):
        if update[i] in rules_dict:
            # print(f"Checking {update[i]} with rules {rules_dict[update[i]]}")
            for rule in rules_dict[update[i]]:
                for j in range(i):
                    if rule == update[j]:
                        # print(f"Fixing: {rule} should be printed after {update[i]}")
                        update[i], update[j] = update[j], update[i]
                        # print(f"Updated: {update}")
                        i = 0
                        break
        i += 1

# print("Corrected updates:")
# pprint(invalid_updates)

# find middle page numbers
sum = 0
for update in invalid_updates:
    middle = update[len(update) // 2]
    sum += middle
    
print(sum)
# 6897