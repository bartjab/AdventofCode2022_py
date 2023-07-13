import os

#input data for the task

data_file_input = open('.\\inputs\\input1.txt')
data_input = data_file_input.readlines()
#print(data_input)

#part 1

calories = []
curr_backpack = 0

for i in range(len(data_input)):
    if data_input[i] != '\n':
        curr_backpack = curr_backpack + int(data_input[i])
    else:
        calories.append(curr_backpack)
        curr_backpack = 0

#print(calories)
calories.sort(reverse=True)
print(calories[0])

#part 2 (calories are sorted in part 1)

top_sum = calories[0] + calories[1] + calories [2]
print(top_sum)
