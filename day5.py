# input data for the task

data_file_input = open('.\\inputs\\input5.txt')
data_input = data_file_input.readlines()
# print(data_input)

# part 1

# splitting data for stacks and movement
crate_pos = []
split_line_num = 0
for i in range(len(data_input)):
    if data_input[i] == '\n':
        split_line_num = i
        break
    else:
        crate_pos.append(data_input[i])
# print(crate_pos)

crate_movement = []
for i in range(split_line_num + 1, len(data_input)):
    crate_movement.append(data_input[i])
# print(crate_movement)

# making stacks as strings
column_count = 0
initial_crate_stacks = []
for i in range(len(crate_pos[-1])):
    if crate_pos[-1][i].isdigit():
        column_count = int(crate_pos[-1][i])

for i in range(column_count):
    initial_crate_stacks.append("")

for i in range(len(crate_pos)-1):
    for k in range(1,len(crate_pos[i]),4):
        if not crate_pos[i][k].isspace():
            initial_crate_stacks[int((k-1)/4)] = crate_pos[i][k] + initial_crate_stacks[int((k-1)/4)]

# print(initial_crate_stacks)
# applying movement to stacks
crate_stacks_1 = []
for i in range(len(initial_crate_stacks)):
    crate_stacks_1.append(initial_crate_stacks[i])

for i in range(len(crate_movement)):
    curr_movement = crate_movement[i].split()
    # print(crate_movement[i].split())
    move_amount = int(curr_movement[1])
    from_column = int(curr_movement[3])
    to_column = int(curr_movement[5])
    for k in range(move_amount):
        crate_stacks_1[to_column - 1] += crate_stacks_1[from_column - 1][-1]
        crate_stacks_1[from_column - 1] = crate_stacks_1[from_column - 1][-len(crate_stacks_1[from_column - 1]):-1]
    # print(crate_stacks_1)

# answer
ans = ''
for i in range(len(crate_stacks_1)):
    ans += crate_stacks_1[i][-1]
print(ans)

# part 2
crate_stacks_2 = []
for i in range(len(initial_crate_stacks)):
    crate_stacks_2.append(initial_crate_stacks[i])

for i in range(len(crate_movement)):
    curr_movement = crate_movement[i].split()
    # print(crate_movement[i].split())
    move_amount = int(curr_movement[1])
    from_column = int(curr_movement[3])
    to_column = int(curr_movement[5])
    boxes = ''
    for k in range(-abs(move_amount), 0):
        boxes += crate_stacks_2[from_column - 1][k]
    # print(boxes)
    crate_stacks_2[from_column - 1] = crate_stacks_2[from_column - 1][-len(crate_stacks_2[from_column - 1]):-abs(move_amount)]
    crate_stacks_2[to_column - 1] += boxes
    # print(crate_stacks)

# answer
ans = ''
for i in range(len(crate_stacks_2)):
    ans += crate_stacks_2[i][-1]
print(ans)
