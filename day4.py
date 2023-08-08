# input data for the task

data_file_input = open('.\\inputs\\input4.txt')
data_input = data_file_input.readlines()
#print(data_input)

# part 1
fully_containing_pairs = 0
modified_data_input = []
num = ""

# changing input format to a list of 4-element lists containing ranges for both section assignment pairs
# each list contains [minrange1, maxrange1, minrange2, maxrange2]
for i in range(len(data_input)):
    modified_data_input.append([])
    for k in range(len(data_input[i])):
        if data_input[i][k].isdigit():
            num += data_input[i][k]
        else:
            modified_data_input[i].append(int(num))
            num = ""
# print(modified_data_input)
for i in range(len(modified_data_input)):
    if (modified_data_input[i][0] >= modified_data_input[i][2] and modified_data_input[i][1] <= modified_data_input[i][3]) or (modified_data_input[i][0] <= modified_data_input[i][2] and modified_data_input[i][1] >= modified_data_input[i][3]):
        fully_containing_pairs += 1
print(fully_containing_pairs)

# part 2

overlapping_pairs = 0
for i in range(len(modified_data_input)):
    if modified_data_input[i][1] >= modified_data_input[i][2] and modified_data_input[i][0] <= modified_data_input[i][3]:
        overlapping_pairs += 1
print(overlapping_pairs)
