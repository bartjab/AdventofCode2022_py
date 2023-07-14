# input data for the task

data_file_input = open('.\\inputs\\input2.txt')
data_input = data_file_input.readlines()
# print(data_input)

# part 1

rounds = []
score = 0

for i in range(len(data_input)):
    if data_input[i][0] == 'A':
        if data_input[i][2] == 'X':
            score += 1 + 3
        elif data_input[i][2] == 'Y':
            score += 2 + 6
        elif data_input[i][2] == 'Z':
            score += 3
    elif data_input[i][0] == 'B':
        if data_input[i][2] == 'X':
            score += 1
        elif data_input[i][2] == 'Y':
            score += 2 + 3
        elif data_input[i][2] == 'Z':
            score += 3 + 6
    elif data_input[i][0] == 'C':
        if data_input[i][2] == 'X':
            score += 1 + 6
        elif data_input[i][2] == 'Y':
            score += 2
        elif data_input[i][2] == 'Z':
            score += 3 + 3

print(score)

# part 2

score = 0

for i in range(len(data_input)):
    if data_input[i][0] == 'A':
        if data_input[i][2] == 'X':     # scissors
            score += 3
        elif data_input[i][2] == 'Y':   # rock
            score += 3 + 1
        elif data_input[i][2] == 'Z':   # paper
            score += 6 + 2
    elif data_input[i][0] == 'B':
        if data_input[i][2] == 'X':     # rock
            score += 1
        elif data_input[i][2] == 'Y':   # paper
            score += 3 + 2
        elif data_input[i][2] == 'Z':   # scissors
            score += 6 + 3
    elif data_input[i][0] == 'C':
        if data_input[i][2] == 'X':     # paper
            score += 2
        elif data_input[i][2] == 'Y':   # scissors
            score += 3 + 3
        elif data_input[i][2] == 'Z':   # rock
            score += 6 + 1

print(score)
