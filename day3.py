# input data for the task

data_file_input = open('.\\inputs\\input3.txt')
data_input = data_file_input.readlines()
# print(data_input)

# part 1

priority_sum = 0

for i in range(len(data_input)):
    compartment_size = len(data_input[i]) - 1
    compartment1 = data_input[i][:int(compartment_size/2)]
    compartment2 = data_input[i][int(compartment_size/2):]
    # print(compartment1 + "   " + compartment2)
    found_duplicate = False
    for n in range(len(compartment1)):
        for k in range(len(compartment2)):
            if compartment1[n] == compartment2[k]:
                found_duplicate = True
                duplicate = compartment1[n]
                if 97 <= ord(duplicate) <= 122:
                    duplicate_value = ord(duplicate) - 96
                elif 65 <= ord(duplicate) <= 90:
                    duplicate_value = ord(duplicate) - 38
                else:
                    duplicate_value = 0
                # print(duplicate + ' ' + str(duplicate_value))
                priority_sum += duplicate_value
                break
        if found_duplicate:
            break

print(priority_sum)

# part 2

priority_sum_group = 0

for i in range(0, len(data_input), 3):
    rucksack1 = data_input[i]
    rucksack2 = data_input[i + 1]
    rucksack3 = data_input[i + 2]
    # print(compartment1 + "   " + compartment2)
    found_duplicate = False
    for n in range(len(rucksack1)):
        for k in range(len(rucksack2)):
            for m in range(len(rucksack3)):
                if rucksack1[n] == rucksack2[k] == rucksack3[m]:
                    found_duplicate = True
                    duplicate = rucksack1[n]
                    if 97 <= ord(duplicate) <= 122:
                        group_duplicate_value = ord(duplicate) - 96
                    elif 65 <= ord(duplicate) <= 90:
                        group_duplicate_value = ord(duplicate) - 38
                    else:
                        group_duplicate_value = 0
                    # print(duplicate + ' ' + str(group_duplicate_value))
                    priority_sum_group += group_duplicate_value
                    break
            if found_duplicate:
                break
        if found_duplicate:
            break

print(priority_sum_group)
